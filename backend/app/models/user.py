from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    Index
)

from datetime import datetime, timezone

from app.database.connection import Base



class User(Base):

    __tablename__ = "users"



    # =========================
    # Primary Key
    # =========================

    id = Column(
        Integer,
        primary_key=True
    )



    # =========================
    # User Information
    # =========================

    username = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )


    email = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )


    full_name = Column(
        String(150),
        nullable=True
    )


    mobile_number = Column(
        String(20),
        nullable=True
    )



    # =========================
    # Authentication
    # =========================

    hashed_password = Column(
        String(255),
        nullable=False
    )


    refresh_token = Column(
        String(500),
        nullable=True
    )



    # =========================
    # Role Management
    # =========================

    role = Column(
        String(30),
        default="admin",
        nullable=False,
        index=True
    )



    # =========================
    # Account Status
    # =========================

    is_active = Column(
        Boolean,
        default=True,
        nullable=False
    )


    is_verified = Column(
        Boolean,
        default=False,
        nullable=False
    )


    is_deleted = Column(
        Boolean,
        default=False,
        nullable=False
    )



    # =========================
    # Login Security
    # =========================

    last_login = Column(
        DateTime,
        nullable=True
    )


    failed_login_attempts = Column(
        Integer,
        default=0,
        nullable=False
    )


    account_locked = Column(
        Boolean,
        default=False,
        nullable=False
    )



    # =========================
    # Audit Fields
    # =========================

    created_at = Column(
        DateTime,
        default=lambda:
        datetime.now(timezone.utc),
        nullable=False
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

        return f"<User {self.username}>"





# =========================
# Database Index
# =========================

Index(
    "idx_user_role_status",
    User.role,
    User.is_active
)


Index(
    "idx_user_email_username",
    User.email,
    User.username
)


Index(
    "idx_user_active_deleted",
    User.is_active,
    User.is_deleted
)
# =========================
# Password Reset Support
# =========================

reset_token = Column(

    String(500),

    nullable=True

)


reset_token_expiry = Column(

    DateTime,

    nullable=True

)