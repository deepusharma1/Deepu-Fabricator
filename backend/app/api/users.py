from datetime import datetime, timezone

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query
)

from sqlalchemy.orm import Session


from app.database.connection import get_db

from app.models.user import User

from app.utils.dependencies import get_current_admin



router = APIRouter(

    prefix="/users",

    tags=[

        "User Management"

    ]

)





ALLOWED_ROLES = [

    "admin",

    "manager",

    "employee"

]







# =====================================================
# GET ALL USERS
# GET /api/v1/users
# =====================================================


@router.get("/")
def get_all_users(

    page: int = Query(1, ge=1),

    limit: int = Query(20, ge=1, le=100),

    db: Session = Depends(get_db),

    admin = Depends(get_current_admin)

):


    offset = (page - 1) * limit



    total = (

        db.query(User)

        .filter(

            User.is_deleted == False

        )

        .count()

    )




    users = (

        db.query(User)

        .filter(

            User.is_deleted == False

        )

        .order_by(

            User.id.desc()

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


                "id":user.id,

                "username":user.username,

                "email":user.email,

                "full_name":user.full_name,

                "mobile_number":user.mobile_number,

                "role":user.role,

                "is_active":user.is_active,

                "is_verified":getattr(

                    user,

                    "is_verified",

                    False

                ),

                "last_login":user.last_login,

                "created_at":user.created_at


            }


            for user in users


        ]

    }









# =====================================================
# GET SINGLE USER
# GET /api/v1/users/{user_id}
# =====================================================


@router.get("/{user_id}")
def get_user(

    user_id:int,

    db:Session = Depends(get_db),

    admin = Depends(get_current_admin)

):


    user = (

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



    return {


        "status":"success",

        "data":{


            "id":user.id,

            "username":user.username,

            "email":user.email,

            "full_name":user.full_name,

            "mobile_number":user.mobile_number,

            "role":user.role,

            "is_active":user.is_active,

            "created_at":user.created_at


        }

    }









# =====================================================
# UPDATE USER STATUS
# PATCH /api/v1/users/{user_id}/status
# =====================================================


@router.patch("/{user_id}/status")
def update_user_status(

    user_id:int,

    is_active:bool,

    db:Session = Depends(get_db),

    admin = Depends(get_current_admin)

):


    user = (

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



    user.is_active = is_active


    if not is_active:

        user.refresh_token = None



    user.updated_at = datetime.now(timezone.utc)



    db.commit()



    return {


        "status":"success",

        "message":"User status updated successfully"


    }









# =====================================================
# UPDATE ROLE
# PATCH /api/v1/users/{user_id}/role
# =====================================================


@router.patch("/{user_id}/role")
def update_user_role(

    user_id:int,

    role:str,

    db:Session = Depends(get_db),

    admin = Depends(get_current_admin)

):


    if role not in ALLOWED_ROLES:


        raise HTTPException(

            status_code=400,

            detail="Invalid role"

        )




    user = (

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



    user.role = role


    user.updated_at = datetime.now(timezone.utc)



    db.commit()



    return {


        "status":"success",

        "message":"User role updated successfully"


    }









# =====================================================
# DELETE USER (SOFT DELETE)
# DELETE /api/v1/users/{user_id}
# =====================================================


@router.delete("/{user_id}")
def delete_user(

    user_id:int,

    db:Session = Depends(get_db),

    admin = Depends(get_current_admin)

):


    user = (

        db.query(User)

        .filter(

            User.id == user_id

        )

        .first()

    )



    if not user:


        raise HTTPException(

            status_code=404,

            detail="User not found"

        )




    user.is_deleted = True

    user.is_active = False

    user.refresh_token = None


    user.updated_at = datetime.now(timezone.utc)



    db.commit()



    return {


        "status":"success",

        "message":"User deleted successfully"


    }