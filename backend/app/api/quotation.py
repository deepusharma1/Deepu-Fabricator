from datetime import (
    datetime,
    timedelta,
    timezone
)


from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query
)


from fastapi.responses import StreamingResponse


from sqlalchemy.orm import Session


from app.database.connection import get_db


from app.models.quotation import QuotationModel


from app.schemas.quotation import (
    QuotationCreate,
    QuotationUpdate
)


from app.services.quotation_pdf import generate_quotation_pdf


from app.utils.dependencies import get_current_admin





router = APIRouter(

    prefix="/quotation",

    tags=["Quotation"]

)





# =====================================================
# ALLOWED STATUS
# =====================================================

ALLOWED_STATUS = [

    "Draft",

    "Pending",

    "Approved",

    "Rejected",

    "Completed"

]






# =====================================================
# CREATE QUOTATION
# POST /api/v1/quotation/create
# =====================================================


@router.post("/create")
def create_quotation(

    payload: QuotationCreate,

    current_admin: dict = Depends(get_current_admin),

    db: Session = Depends(get_db)

):


    try:


        subtotal = 0


        items_data = []



        for item in payload.items:


            amount = (

                item.quantity

                *

                item.rate

            )


            subtotal += amount



            items_data.append({

                "material_name": item.material_name,

                "description": item.description,

                "quantity": item.quantity,

                "unit": item.unit,

                "rate": item.rate,

                "amount": amount

            })





        if payload.width_ft > 0 and payload.height_ft > 0:

            total_area = (

                payload.width_ft

                *

                payload.height_ft

            )

        else:

            total_area = 0






        extra_charge = (

            payload.labour_cost

            +

            payload.installation_cost

            +

            payload.transport_cost

            +

            payload.other_charges

        )





        taxable_amount = (

            subtotal

            +

            extra_charge

            -

            payload.discount

        )




        if taxable_amount < 0:

            taxable_amount = 0





        gst_amount = (

            taxable_amount

            *

            payload.gst_percent

            /

            100

        )





        grand_total = (

            taxable_amount

            +

            gst_amount

        )





        quotation_no = (

            "DF-"

            +

            datetime.now().strftime(

                "%Y%m%d%H%M%S"

            )

        )





        quotation = QuotationModel(


            quotation_no=quotation_no,


            revision_no=1,


            customer_name=payload.customer_name,


            company_name=payload.company_name,


            mobile_number=payload.mobile_number,


            email=payload.email,


            address=payload.address,


            lead_source=payload.lead_source,


            work_type=payload.work_type,


            material_type=payload.material_type,


            width_ft=payload.width_ft,


            height_ft=payload.height_ft,


            total_area_sqft=total_area,


            rate_per_sqft=payload.rate_per_sqft,


            estimated_cost=subtotal,


            labour_cost=payload.labour_cost,


            installation_cost=payload.installation_cost,


            transport_cost=payload.transport_cost,


            other_charges=payload.other_charges,


            discount=payload.discount,


            gst_percent=payload.gst_percent,


            gst_amount=gst_amount,


            grand_total=grand_total,


            items_json=items_data,


            notes=payload.notes,


            payment_terms=payload.payment_terms,


            delivery_time=payload.delivery_time,


            valid_until=(

                datetime.now(timezone.utc)

                +

                timedelta(days=30)

            ),


            status="Draft"

        )





        db.add(quotation)


        db.commit()


        db.refresh(quotation)





        return {


            "status":"success",


            "message":"Quotation created successfully",


            "data":{

                "id":quotation.id,

                "quotation_no":quotation.quotation_no,

                "grand_total":quotation.grand_total,

                "status":quotation.status

            }

        }





    except Exception as error:


        db.rollback()


        raise HTTPException(

            status_code=500,

            detail=str(error)

        )







# =====================================================
# GET ALL QUOTATIONS
# GET /api/v1/quotation/list
# =====================================================


@router.get("/list")
def get_all_quotations(

    page:int = Query(

        1,

        ge=1

    ),


    limit:int = Query(

        20,

        ge=1,

        le=100

    ),


    current_admin: dict = Depends(get_current_admin),


    db:Session = Depends(get_db)

):


    offset = (

        page - 1

    ) * limit





    total = (

        db.query(QuotationModel)

        .filter(

            QuotationModel.is_deleted == False

        )

        .count()

    )





    quotations = (

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

                "revision_no":q.revision_no,

                "customer_name":q.customer_name,

                "mobile_number":q.mobile_number,

                "work_type":q.work_type,

                "grand_total":q.grand_total,

                "status":q.status,

                "created_at":q.created_at

            }


            for q in quotations


        ]


    }
# =====================================================
# GET SINGLE QUOTATION DETAIL
# GET /api/v1/quotation/detail/{quotation_id}
# =====================================================


@router.get("/detail/{quotation_id}")
def get_single_quotation(

    quotation_id:int,

    current_admin: dict = Depends(get_current_admin),

    db:Session = Depends(get_db)

):


    quotation = (

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


            "revision_no":quotation.revision_no,


            "customer_name":quotation.customer_name,


            "company_name":quotation.company_name,


            "mobile_number":quotation.mobile_number,


            "email":quotation.email,


            "address":quotation.address,


            "work_type":quotation.work_type,


            "material_type":quotation.material_type,


            "items":quotation.items_json,


            "estimated_cost":quotation.estimated_cost,


            "labour_cost":quotation.labour_cost,


            "installation_cost":quotation.installation_cost,


            "transport_cost":quotation.transport_cost,


            "other_charges":quotation.other_charges,


            "discount":quotation.discount,


            "gst_percent":quotation.gst_percent,


            "gst_amount":quotation.gst_amount,


            "grand_total":quotation.grand_total,


            "status":quotation.status,


            "is_locked":quotation.is_locked,


            "notes":quotation.notes,


            "created_at":quotation.created_at


        }


    }








# =====================================================
# UPDATE QUOTATION
# PATCH /api/v1/quotation/{quotation_id}
# =====================================================


@router.patch("/{quotation_id}")
def update_quotation(


    quotation_id:int,


    payload:QuotationUpdate,


    current_admin: dict = Depends(get_current_admin),


    db:Session = Depends(get_db)


):


    quotation = (


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





    if quotation.is_locked:


        raise HTTPException(


            status_code=400,


            detail="Quotation is locked"

        )





    update_data = payload.model_dump(

        exclude_unset=True

    )





    if "status" in update_data:


        if update_data["status"] not in ALLOWED_STATUS:


            raise HTTPException(

                status_code=400,

                detail="Invalid quotation status"

            )





    for key,value in update_data.items():


        setattr(

            quotation,

            key,

            value

        )





    quotation.updated_at = datetime.now(

        timezone.utc

    )





    db.commit()


    db.refresh(quotation)





    return {


        "status":"success",


        "message":"Quotation updated successfully"


    }








# =====================================================
# DELETE QUOTATION (SOFT DELETE)
# DELETE /api/v1/quotation/{quotation_id}
# =====================================================


@router.delete("/{quotation_id}")
def delete_quotation(


    quotation_id:int,


    current_admin: dict = Depends(get_current_admin),


    db:Session = Depends(get_db)


):


    quotation = (


        db.query(QuotationModel)


        .filter(

            QuotationModel.id == quotation_id

        )


        .first()


    )





    if not quotation:


        raise HTTPException(


            status_code=404,


            detail="Quotation not found"


        )





    quotation.is_deleted = True



    quotation.updated_at = datetime.now(

        timezone.utc

    )




    db.commit()





    return {


        "status":"success",


        "message":"Quotation deleted successfully"


    }

# =====================================================
# STATUS UPDATE
# PATCH /api/v1/quotation/status/{id}
# =====================================================


@router.patch("/status/{quotation_id}")
def update_status(

    quotation_id:int,

    status:str,

    current_admin: dict = Depends(get_current_admin),

    db:Session = Depends(get_db)

):


    if status not in ALLOWED_STATUS:


        raise HTTPException(

            status_code=400,

            detail="Invalid status"

        )





    quotation = (


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





    quotation.status = status



    quotation.updated_at = datetime.now(

        timezone.utc

    )





    db.commit()





    return {


        "status":"success",


        "message":"Status updated successfully"


    }









# =====================================================
# DOWNLOAD PDF
# GET /api/v1/quotation/pdf/{id}
# =====================================================


@router.get("/pdf/{quotation_id}")
def download_pdf(


    quotation_id:int,


    current_admin: dict = Depends(get_current_admin),


    db:Session = Depends(get_db)

):


    quotation = (


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





    pdf = generate_quotation_pdf(

        quotation

    )





    return StreamingResponse(


        pdf,


        media_type="application/pdf",


        headers={


            "Content-Disposition":


            f"attachment; filename={quotation.quotation_no}.pdf"


        }


    )









# =====================================================
# CREATE REVISION
# POST /api/v1/quotation/revision/{id}
# =====================================================


@router.post("/revision/{quotation_id}")
def create_revision(


    quotation_id:int,


    current_admin: dict = Depends(get_current_admin),


    db:Session = Depends(get_db)

):


    old = (


        db.query(QuotationModel)


        .filter(


            QuotationModel.id == quotation_id,


            QuotationModel.is_deleted == False


        )


        .first()


    )





    if not old:


        raise HTTPException(

            status_code=404,

            detail="Quotation not found"

        )





    if old.is_locked:


        raise HTTPException(

            status_code=400,

            detail="Locked quotation revision not allowed"

        )







    new_quote = QuotationModel(


        **{


            column.name:getattr(old,column.name)


            for column in QuotationModel.__table__.columns


            if column.name not in [


                "id",


                "created_at",


                "updated_at"


            ]


        },


        revision_no=old.revision_no + 1,


        status="Draft"


    )





    db.add(new_quote)


    db.commit()


    db.refresh(new_quote)





    return {


        "status":"success",


        "message":"Revision created successfully",


        "data":{


            "id":new_quote.id,


            "revision_no":new_quote.revision_no


        }


    }

    
# =====================================================
# LOCK QUOTATION
# PATCH /api/v1/quotation/lock/{quotation_id}
# =====================================================


@router.patch("/lock/{quotation_id}")
def lock_quotation(


    quotation_id:int,


    current_admin: dict = Depends(get_current_admin),


    db:Session = Depends(get_db)


):


    quotation = (

        db.query(QuotationModel)

        .filter(

            QuotationModel.id == quotation_id

        )

        .first()

    )





    if not quotation:


        raise HTTPException(

            status_code=404,

            detail="Quotation not found"

        )





    quotation.is_locked = True


    quotation.updated_at = datetime.now(

        timezone.utc

    )





    db.commit()





    return {


        "status":"success",


        "message":"Quotation locked successfully"


    }









# =====================================================
# UNLOCK QUOTATION
# PATCH /api/v1/quotation/unlock/{quotation_id}
# =====================================================


@router.patch("/unlock/{quotation_id}")
def unlock_quotation(


    quotation_id:int,


    current_admin: dict = Depends(get_current_admin),


    db:Session = Depends(get_db)


):


    quotation = (


        db.query(QuotationModel)


        .filter(


            QuotationModel.id == quotation_id

        )


        .first()


    )





    if not quotation:


        raise HTTPException(

            status_code=404,

            detail="Quotation not found"

        )





    quotation.is_locked = False


    quotation.updated_at = datetime.now(

        timezone.utc

    )





    db.commit()





    return {


        "status":"success",


        "message":"Quotation unlocked successfully"


    }