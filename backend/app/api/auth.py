# backend/app/api/auth.py


from datetime import datetime, timedelta, timezone

import secrets


from fastapi import (

    APIRouter,

    Depends,

    HTTPException,

    status

)


from sqlalchemy.orm import Session



from app.database.connection import get_db


from app.models.user import User



from app.schemas.auth import (

    LoginRequest,

    RegisterRequest,

    TokenResponse,

    UserResponse,

    RefreshTokenRequest,

    ChangePasswordRequest,

    ForgotPasswordRequest,

    ResetPasswordRequest

)



from app.services.auth_service import AuthService



from app.utils.dependencies import get_current_user



from app.utils.jwt import (

    decode_refresh_token,

    create_access_token

)



from app.utils.password import (

    hash_password,

    verify_password

)







router = APIRouter(

    prefix="/auth",

    tags=["Authentication"]

)









# =====================================================
# LOGIN
# POST /api/v1/auth/login
# =====================================================


@router.post(

    "/login",

    response_model=TokenResponse

)
def login(


    payload: LoginRequest,


    db: Session = Depends(get_db)


):


    try:


        result = AuthService.authenticate_user(


            db,


            payload.username.strip(),


            payload.password


        )




        if not result:



            raise HTTPException(


                status_code=status.HTTP_401_UNAUTHORIZED,


                detail="Invalid username or password"


            )




        return result





    except HTTPException:

        raise



    except Exception as error:



        raise HTTPException(


            status_code=500,


            detail=str(error)


        )









# =====================================================
# REGISTER
# POST /api/v1/auth/register
# =====================================================


@router.post(

    "/register",

    response_model=UserResponse,

    status_code=201

)
def register(



    payload: RegisterRequest,


    db: Session = Depends(get_db)



):


    try:



        username_exist = (


            db.query(User)


            .filter(


                User.username == payload.username


            )


            .first()


        )





        if username_exist:


            raise HTTPException(


                status_code=400,


                detail="Username already exists"


            )







        email_exist = (



            db.query(User)



            .filter(



                User.email == payload.email.lower()



            )



            .first()



        )






        if email_exist:


            raise HTTPException(


                status_code=400,


                detail="Email already exists"


            )








        user = AuthService.create_user(


            db,


            payload.username.strip(),


            payload.email.lower(),


            payload.password,


            payload.full_name,


            payload.mobile_number


        )






        return user






    except HTTPException:

        raise



    except Exception as error:



        raise HTTPException(


            status_code=400,


            detail=str(error)


        )









# =====================================================
# CURRENT USER
# GET /api/v1/auth/me
# =====================================================


@router.get(

    "/me",

    response_model=UserResponse

)
def profile(



    current_user:dict = Depends(get_current_user),


    db:Session = Depends(get_db)



):



    user = (



        db.query(User)



        .filter(



            User.id == current_user["user_id"]



        )



        .first()



    )





    if not user:


        raise HTTPException(


            status_code=404,


            detail="User not found"


        )





    return user










# =====================================================
# REFRESH TOKEN
# POST /api/v1/auth/refresh
# =====================================================


@router.post(

    "/refresh",

    response_model=TokenResponse

)
def refresh_token(



    payload:RefreshTokenRequest,


    db:Session = Depends(get_db)



):



    data = decode_refresh_token(


        payload.refresh_token


    )




    if not data:


        raise HTTPException(


            status_code=401,


            detail="Invalid refresh token"


        )






    user_id = data.get("user_id")





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







    if user.refresh_token != payload.refresh_token:



        raise HTTPException(


            status_code=401,


            detail="Refresh token expired"


        )







    access_token = create_access_token(



        {


            "sub":user.username,


            "user_id":user.id,


            "role":user.role



        }



    )






    return {



        "access_token":access_token,


        "refresh_token":payload.refresh_token,


        "token_type":"bearer"



    }









# =====================================================
# LOGOUT
# POST /api/v1/auth/logout
# =====================================================


@router.post("/logout")
def logout(



    current_user:dict = Depends(get_current_user),


    db:Session = Depends(get_db)



):



    user = db.query(User).filter(


        User.id == current_user["user_id"]


    ).first()





    if user:


        user.refresh_token = None


        db.commit()





    return {



        "status":"success",


        "message":"Logout successful"



    }









# =====================================================
# CHANGE PASSWORD
# =====================================================


@router.put("/change-password")
def change_password(



    payload:ChangePasswordRequest,


    current_user:dict = Depends(get_current_user),


    db:Session = Depends(get_db)



):



    user = db.query(User).filter(


        User.id == current_user["user_id"]


    ).first()





    if not user:


        raise HTTPException(


            status_code=404,


            detail="User not found"


        )







    if not verify_password(



        payload.old_password,


        user.hashed_password



    ):



        raise HTTPException(


            status_code=400,


            detail="Old password incorrect"


        )






    user.hashed_password = hash_password(


        payload.new_password


    )



    user.refresh_token = None



    db.commit()





    return {



        "status":"success",


        "message":"Password changed successfully"



    }









# =====================================================
# FORGOT PASSWORD
# =====================================================


@router.post("/forgot-password")
def forgot_password(



    payload:ForgotPasswordRequest,


    db:Session = Depends(get_db)



):



    user = db.query(User).filter(


        User.email == payload.email.lower()


    ).first()





    if not user:


        raise HTTPException(


            status_code=404,


            detail="Email not registered"


        )






    token = secrets.token_urlsafe(32)



    user.reset_token = token



    user.reset_token_expiry = (


        datetime.now(timezone.utc)


        +


        timedelta(minutes=15)


    )




    db.commit()





    return {



        "status":"success",


        "message":"Reset token generated",


        "reset_token":token


    }









# =====================================================
# RESET PASSWORD
# =====================================================


@router.post("/reset-password")
def reset_password(



    payload:ResetPasswordRequest,


    db:Session = Depends(get_db)



):



    user = db.query(User).filter(


        User.reset_token == payload.token


    ).first()






    if not user:


        raise HTTPException(


            status_code=400,


            detail="Invalid reset token"


        )







    if user.reset_token_expiry < datetime.now(timezone.utc):



        raise HTTPException(


            status_code=400,


            detail="Token expired"


        )






    user.hashed_password = hash_password(


        payload.new_password


    )



    user.reset_token = None


    user.reset_token_expiry = None


    user.refresh_token = None




    db.commit()





    return {



        "status":"success",


        "message":"Password reset successful"



    }