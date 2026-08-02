from fastapi import (
    Depends,
    HTTPException,
    status
)

from fastapi.security import OAuth2PasswordBearer


from app.utils.jwt import decode_access_token






# =====================================================
# JWT Bearer Token Reader
# =====================================================

oauth2_scheme = OAuth2PasswordBearer(

    tokenUrl="/api/v1/auth/login"

)








# =====================================================
# Current Logged In User
# =====================================================

def get_current_user(

    token: str = Depends(oauth2_scheme)

):


    payload = decode_access_token(token)



    if not payload:


        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Invalid or expired token",

            headers={

                "WWW-Authenticate": "Bearer"

            }

        )





    username = payload.get("sub")

    user_id = payload.get("user_id")

    role = payload.get("role")





    if not username or not user_id:


        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Invalid token payload"

        )





    return {


        "username": username,


        "user_id": user_id,


        "role": role


    }









# =====================================================
# Admin Only Access
# =====================================================

def get_current_admin(

    current_user: dict = Depends(get_current_user)

):


    if current_user.get("role") != "admin":


        raise HTTPException(

            status_code=status.HTTP_403_FORBIDDEN,

            detail="Admin access required"

        )



    return current_user