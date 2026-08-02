# backend/app/api/contact.py


from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session


from app.database.connection import get_db


from app.schemas.contact import (
    ContactCreate,
    ContactResponse
)


from app.services.contact_service import (
    ContactService
)


from app.utils.logger import logger





router = APIRouter(

    prefix="/contact",

    tags=[
        "Contact"
    ]

)






# =====================================================
# CREATE CONTACT QUERY
# POST /api/v1/contact/
# =====================================================


@router.post(
    "/",
    response_model=ContactResponse,
    status_code=status.HTTP_201_CREATED
)
def create_contact(

    payload: ContactCreate,

    db: Session = Depends(get_db)

):


    try:


        contact = ContactService.save_message(

            db,

            payload

        )


        return contact





    except ValueError as error:


        logger.warning(

            f"Contact validation failed : {error}"

        )


        raise HTTPException(

            status_code=status.HTTP_400_BAD_REQUEST,

            detail=str(error)

        )





    except Exception as error:


        db.rollback()


        logger.error(

            f"Contact creation failed : {error}"

        )


        raise HTTPException(

            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,

            detail="Contact submission failed"

        )