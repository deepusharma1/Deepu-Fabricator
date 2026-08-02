from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    Boolean,
    Index
)

from datetime import datetime, timezone

from app.database.connection import Base



class ContactModel(Base):

    __tablename__ = "contacts"



    # =========================
    # Primary Key
    # =========================

    id = Column(

        Integer,

        primary_key=True,

        index=True

    )



    # =========================
    # Contact Information
    # =========================

    full_name = Column(

        String(100),

        nullable=False

    )


    mobile_number = Column(

        String(15),

        nullable=False,

        index=True

    )


    email_address = Column(

        String(150),

        nullable=True,

        index=True

    )


    requirement_type = Column(

        String(100),

        nullable=False

    )


    message = Column(

        Text,

        nullable=False

    )



    # =========================
    # Status Management
    # =========================

    status = Column(

        String(20),

        default="New",

        nullable=False,

        index=True

    )


    # =========================
    # Soft Delete
    # =========================

    is_deleted = Column(

        Boolean,

        default=False,

        nullable=False,

        index=True

    )



    # =========================
    # Audit Fields
    # =========================

    created_at = Column(

        DateTime,

        default=lambda:

        datetime.now(timezone.utc),

        nullable=False,

        index=True

    )


    updated_at = Column(

        DateTime,

        default=lambda:

        datetime.now(timezone.utc),


        onupdate=lambda:

        datetime.now(timezone.utc),


        nullable=False

    )





    def __repr__(self):

        return (

            f"<Contact {self.full_name}>"

        )





# =========================
# Database Index
# =========================

Index(

    "idx_contact_status_created",

    ContactModel.status,

    ContactModel.created_at

)


Index(

    "idx_contact_deleted_status",

    ContactModel.is_deleted,

    ContactModel.status

)