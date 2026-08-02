from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.models.contact import ContactModel
from app.schemas.contact import ContactCreate

from datetime import datetime, timezone



class ContactService:


    # =====================================================
    # CREATE CONTACT MESSAGE
    # =====================================================

    @staticmethod
    def save_message(
        db: Session,
        data: ContactCreate
    ):


        try:


            contact = ContactModel(


                full_name=data.fullName,


                mobile_number=data.mobileNumber,


                email_address=data.emailAddress,


                requirement_type=data.requirementType,


                message=data.message,


                status="New"


            )



            db.add(contact)


            db.commit()


            db.refresh(contact)



            return contact




        except SQLAlchemyError as error:


            db.rollback()


            raise Exception(

                f"Database error while saving contact: {str(error)}"

            )



        except Exception as error:


            db.rollback()


            raise Exception(

                f"Contact creation failed: {str(error)}"

            )





    # =====================================================
    # GET ALL CONTACTS
    # =====================================================


    @staticmethod
    def get_all_contacts(
        db: Session
    ):


        return (

            db.query(ContactModel)

            .order_by(

                ContactModel.id.desc()

            )

            .all()

        )





    # =====================================================
    # GET CONTACT BY ID
    # =====================================================


    @staticmethod
    def get_contact_by_id(

        db: Session,

        contact_id:int

    ):


        return (

            db.query(ContactModel)

            .filter(

                ContactModel.id == contact_id

            )

            .first()

        )





    # =====================================================
    # UPDATE STATUS
    # =====================================================


    @staticmethod
    def update_status(

        db:Session,

        contact_id:int,

        status:str

    ):


        contact = (

            db.query(ContactModel)

            .filter(

                ContactModel.id == contact_id

            )

            .first()

        )


        if not contact:

            return None



        contact.status = status


        contact.updated_at = datetime.now(
            timezone.utc
        )


        db.commit()


        db.refresh(contact)



        return contact