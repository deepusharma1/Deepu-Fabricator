# backend/app/middleware/auth.py


from fastapi import (
    Request,
    HTTPException,
    status
)


from app.utils.jwt import decode_access_token






async def admin_auth_middleware(

    request: Request

):


    auth_header = request.headers.get(
        "Authorization"
    )



    if not auth_header:


        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Authorization token missing"

        )





    if not auth_header.startswith(
        "Bearer "
    ):


        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Invalid token format"

        )





    token = auth_header.replace(
        "Bearer ",
        ""
    )





    payload = decode_access_token(

        token

    )





    if payload is None:


        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Invalid or expired token"

        )





    # Admin role check

    if payload.get("role") != "admin":


        raise HTTPException(

            status_code=status.HTTP_403_FORBIDDEN,

            detail="Admin access required"

        )





    request.state.user = payload



    return payload