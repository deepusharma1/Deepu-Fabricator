from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query
)

from fastapi.responses import StreamingResponse

from sqlalchemy.orm import Session
from sqlalchemy import func

from datetime import datetime

import io
import csv


from app.database.connection import get_db


from app.models.contact import ContactModel
from app.models.quotation import QuotationModel
from app.models.user import User


from app.utils.dependencies import get_current_admin



router = APIRouter(

    prefix="/admin",

    tags=["Admin Dashboard"]

)



ALLOWED_QUOTATION_STATUS = [

    "Draft",
    "Pending",
    "Approved",
    "Rejected",
    "Completed"

]



# =====================================================
# GET CONTACT QUERIES
# GET /api/v1/admin/queries
# =====================================================

@router.get("/queries")
def get_contact_queries(

    page:int = Query(1, ge=1),

    limit:int = Query(20, ge=1, le=100),

    db:Session = Depends(get_db),

    admin = Depends(get_current_admin)

):


    offset = (page - 1) * limit



    total = (

        db.query(ContactModel)

        .filter(

            ContactModel.is_deleted == False

        )

        .count()

    )



    queries = (

        db.query(ContactModel)

        .filter(

            ContactModel.is_deleted == False

        )

        .order_by(

            ContactModel.id.desc()

        )

        .offset(offset)

        .limit(limit)

        .all()

    )



    return {

        "status":"success",

        "total":total,

        "page":page,

        "limit":limit,


        "data":[


            {

                "id":q.id,

                "name":q.full_name,

                "mobile":q.mobile_number,

                "email":q.email_address,

                "requirement":q.requirement_type,

                "message":q.message,

                "status":q.status,

                "created_at":q.created_at

            }

            for q in queries

        ]

    }





# =====================================================
# GET ALL QUOTATIONS
# GET /api/v1/admin/quotations
# =====================================================

@router.get("/quotations")
def get_admin_quotations(

    page:int = Query(1, ge=1),

    limit:int = Query(20, ge=1, le=100),

    db:Session = Depends(get_db),

    admin = Depends(get_current_admin)

):


    offset=(page-1)*limit



    total=(

        db.query(QuotationModel)

        .filter(

            QuotationModel.is_deleted == False

        )

        .count()

    )



    quotations=(

        db.query(QuotationModel)

        .filter(

            QuotationModel.is_deleted == False

        )

        .order_by(

            QuotationModel.id.desc()

        )

        .offset(offset)

        .limit(limit)

        .all()

    )



    return {


        "status":"success",

        "total":total,

        "page":page,

        "limit":limit,


        "data":[


            {

                "id":q.id,

                "quotation_no":q.quotation_no,

                "customer_name":q.customer_name,

                "mobile":q.mobile_number,

                "work_type":q.work_type,

                "amount":q.grand_total,

                "status":q.status,

                "locked":q.is_locked,

                "created_at":q.created_at

            }

            for q in quotations

        ]

    }





# =====================================================
# UPDATE QUOTATION STATUS
# PATCH /api/v1/admin/quotation/{id}/status
# =====================================================

@router.patch("/quotation/{quotation_id}/status")
def update_quotation_status(

    quotation_id:int,

    status:str,

    db:Session = Depends(get_db),

    admin = Depends(get_current_admin)

):


    if status not in ALLOWED_QUOTATION_STATUS:


        raise HTTPException(

            status_code=400,

            detail="Invalid quotation status"

        )



    quotation=(


        db.query(QuotationModel)

        .filter(

            QuotationModel.id == quotation_id,

            QuotationModel.is_deleted == False

        )

        .first()

    )



    if not quotation:


        raise HTTPException(

            status_code=404,

            detail="Quotation not found"

        )



    quotation.status=status

    quotation.updated_at=datetime.utcnow()



    db.commit()



    return {


        "status":"success",

        "message":

        "Quotation status updated successfully"

    }





# =====================================================
# GET SINGLE QUOTATION DETAIL
# GET /api/v1/admin/quotation/{id}
# =====================================================

@router.get("/quotation/{quotation_id}")
def get_quotation_detail(

    quotation_id:int,

    db:Session = Depends(get_db),

    admin = Depends(get_current_admin)

):


    quotation=(


        db.query(QuotationModel)

        .filter(

            QuotationModel.id == quotation_id,

            QuotationModel.is_deleted == False

        )

        .first()

    )



    if not quotation:


        raise HTTPException(

            status_code=404,

            detail="Quotation not found"

        )



    return {


        "status":"success",

        "data":{


            "id":quotation.id,

            "quotation_no":quotation.quotation_no,

            "customer_name":quotation.customer_name,

            "company_name":quotation.company_name,

            "mobile":quotation.mobile_number,

            "email":quotation.email,

            "address":quotation.address,

            "work_type":quotation.work_type,

            "items":quotation.items_json,

            "grand_total":quotation.grand_total,

            "status":quotation.status,

            "notes":quotation.notes,

            "created_at":quotation.created_at

        }

    }

# =====================================================
# GET SINGLE CONTACT QUERY
# GET /api/v1/admin/query/{query_id}
# =====================================================

@router.get("/query/{query_id}")
def get_single_query(

    query_id:int,

    db:Session = Depends(get_db),

    admin = Depends(get_current_admin)

):


    query=(

        db.query(ContactModel)

        .filter(

            ContactModel.id == query_id,

            ContactModel.is_deleted == False

        )

        .first()

    )


    if not query:

        raise HTTPException(

            status_code=404,

            detail="Contact query not found"

        )


    return {


        "status":"success",

        "data":{


            "id":query.id,

            "name":query.full_name,

            "mobile":query.mobile_number,

            "email":query.email_address,

            "requirement":query.requirement_type,

            "message":query.message,

            "status":query.status,

            "created_at":query.created_at

        }

    }





# =====================================================
# UPDATE CONTACT QUERY STATUS
# PATCH /api/v1/admin/query/{query_id}/status
# =====================================================

@router.patch("/query/{query_id}/status")
def update_query_status(

    query_id:int,

    status:str,

    db:Session = Depends(get_db),

    admin = Depends(get_current_admin)

):


    allowed_status=[

        "New",

        "Contacted",

        "In Progress",

        "Completed",

        "Rejected"

    ]



    if status not in allowed_status:


        raise HTTPException(

            status_code=400,

            detail="Invalid status"

        )



    query=(

        db.query(ContactModel)

        .filter(

            ContactModel.id == query_id,

            ContactModel.is_deleted == False

        )

        .first()

    )



    if not query:


        raise HTTPException(

            status_code=404,

            detail="Contact query not found"

        )



    query.status=status


    query.updated_at=datetime.utcnow()



    db.commit()

    db.refresh(query)



    return {


        "status":"success",

        "message":

        "Contact status updated successfully",


        "data":{

            "id":query.id,

            "status":query.status

        }

    }





# =====================================================
# DELETE CONTACT QUERY (SOFT DELETE)
# DELETE /api/v1/admin/query/{query_id}
# =====================================================

@router.delete("/query/{query_id}")
def delete_query(

    query_id:int,

    db:Session = Depends(get_db),

    admin = Depends(get_current_admin)

):


    query=(

        db.query(ContactModel)

        .filter(

            ContactModel.id == query_id,

            ContactModel.is_deleted == False

        )

        .first()

    )



    if not query:


        raise HTTPException(

            status_code=404,

            detail="Query not found"

        )



    query.is_deleted=True


    db.commit()



    return {


        "status":"success",

        "message":

        "Contact query deleted successfully"

    }





# =====================================================
# DELETE QUOTATION (SOFT DELETE)
# DELETE /api/v1/admin/quotation/{quotation_id}
# =====================================================

@router.delete("/quotation/{quotation_id}")
def delete_quotation(

    quotation_id:int,

    db:Session = Depends(get_db),

    admin = Depends(get_current_admin)

):


    quotation=(

        db.query(QuotationModel)

        .filter(

            QuotationModel.id == quotation_id,

            QuotationModel.is_deleted == False

        )

        .first()

    )



    if not quotation:


        raise HTTPException(

            status_code=404,

            detail="Quotation not found"

        )



    quotation.is_deleted=True


    db.commit()



    return {


        "status":"success",

        "message":

        "Quotation deleted successfully"

    }





# =====================================================
# GET ALL USERS
# GET /api/v1/admin/users
# =====================================================

@router.get("/users")
def get_users(

    db:Session = Depends(get_db),

    admin = Depends(get_current_admin)

):


    users=(

        db.query(User)

        .filter(

            User.is_deleted == False

        )

        .order_by(

            User.id.desc()

        )

        .all()

    )



    return {


        "status":"success",

        "total":len(users),


        "data":[


            {

                "id":u.id,

                "username":u.username,

                "email":u.email,

                "role":u.role,

                "is_active":u.is_active,

                "created_at":u.created_at,

                "last_login":u.last_login

            }

            for u in users

        ]

    }





# =====================================================
# UPDATE USER STATUS
# PATCH /api/v1/admin/user/{user_id}/status
# =====================================================

@router.patch("/user/{user_id}/status")
def update_user_status(

    user_id:int,

    is_active:bool,

    db:Session = Depends(get_db),

    admin = Depends(get_current_admin)

):


    user=(

        db.query(User)

        .filter(

            User.id == user_id,

            User.is_deleted == False

        )

        .first()

    )



    if not user:


        raise HTTPException(

            status_code=404,

            detail="User not found"

        )



    user.is_active=is_active



    if not is_active:

        user.refresh_token=None



    db.commit()



    return {


        "status":"success",

        "message":

        "User status updated successfully"

    }

# =====================================================
# CSV BACKUP
# GET /api/v1/admin/backup
# =====================================================

@router.get("/backup")
def download_backup(

    db:Session = Depends(get_db),

    admin = Depends(get_current_admin)

):


    output = io.StringIO()


    writer = csv.writer(output)



    writer.writerow(

        [

            "DEEPU FABRICATOR BACKUP",

            datetime.now()

        ]

    )



    writer.writerow([])



    writer.writerow(

        [

            "Quotation No",

            "Customer",

            "Mobile",

            "Amount",

            "Status",

            "Created Date"

        ]

    )



    quotations=(


        db.query(QuotationModel)

        .filter(

            QuotationModel.is_deleted == False

        )

        .order_by(

            QuotationModel.id.desc()

        )

        .all()

    )




    for q in quotations:


        writer.writerow(

            [

                q.quotation_no,

                q.customer_name,

                q.mobile_number,

                q.grand_total,

                q.status,

                q.created_at

            ]

        )



    output.seek(0)



    return StreamingResponse(


        io.BytesIO(

            output.getvalue()

            .encode("utf-8-sig")

        ),


        media_type="text/csv",


        headers={


            "Content-Disposition":

            "attachment; filename=Deepu_Backup.csv"

        }

    )






# =====================================================
# DASHBOARD STATISTICS
# GET /api/v1/admin/dashboard/stats
# =====================================================


@router.get("/dashboard/stats")
def dashboard_statistics(

    db:Session = Depends(get_db),

    admin = Depends(get_current_admin)

):


    total_contacts=(

        db.query(ContactModel)

        .filter(

            ContactModel.is_deleted == False

        )

        .count()

    )



    total_quotations=(

        db.query(QuotationModel)

        .filter(

            QuotationModel.is_deleted == False

        )

        .count()

    )



    total_users=(

        db.query(User)

        .filter(

            User.is_deleted == False

        )

        .count()

    )




    approved_quotations=(

        db.query(QuotationModel)

        .filter(

            QuotationModel.status=="Approved",

            QuotationModel.is_deleted == False

        )

        .count()

    )




    pending_quotations=(

        db.query(QuotationModel)

        .filter(

            QuotationModel.status=="Pending",

            QuotationModel.is_deleted == False

        )

        .count()

    )




    completed_projects=(

        db.query(QuotationModel)

        .filter(

            QuotationModel.status=="Completed",

            QuotationModel.is_deleted == False

        )

        .count()

    )




    total_revenue=(


        db.query(

            func.sum(

                QuotationModel.grand_total

            )

        )

        .filter(

            QuotationModel.status=="Completed",

            QuotationModel.is_deleted == False

        )

        .scalar()

    )




    return {


        "status":"success",


        "data":{


            "total_contacts":

            total_contacts,


            "total_quotations":

            total_quotations,


            "total_users":

            total_users,


            "approved_quotations":

            approved_quotations,


            "pending_quotations":

            pending_quotations,


            "completed_projects":

            completed_projects,


            "total_revenue":

            total_revenue or 0

        }

    }