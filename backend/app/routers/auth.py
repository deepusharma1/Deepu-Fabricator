# backend/app/routers/auth.py


from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)


from sqlalchemy.orm import Session


from app.database.connection import get_db


from app.schemas.auth import (
    LoginRequest,
    TokenResponse
)


from app.services.auth_service import AuthService






router = APIRouter(

    prefix="/auth",

    tags=[
        "Authentication"
    ]

)







@router.post(

    "/login",

    response_model=TokenResponse

)
def login(

    payload: LoginRequest,

    db: Session = Depends(get_db)

):


    result = AuthService.authenticate_admin(

        db,

        payload.username,

        payload.password

    )



    if not result:


        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Invalid username or password"

        )



    return result