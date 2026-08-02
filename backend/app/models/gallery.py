from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    Text,
    Index
)

from datetime import datetime, timezone

from app.database.connection import Base



class GalleryModel(Base):

    __tablename__ = "gallery"


    # =========================
    # Primary Key
    # =========================

    id = Column(

        Integer,

        primary_key=True,

        index=True

    )


    # =========================
    # Gallery Information
    # =========================

    title = Column(

        String(150),

        nullable=False

    )


    category = Column(

        String(100),

        nullable=False,

        index=True

    )


    description = Column(

        Text,

        nullable=True

    )


    image_url = Column(

        String(300),

        nullable=False,

        index=True

    )


    # =========================
    # Status Management
    # =========================

    status = Column(

        String(20),

        default="Active",

        nullable=False

    )


    is_deleted = Column(

        Boolean,

        default=False,

        nullable=False,

        index=True

    )


    # =========================
    # Audit Fields
    # =========================

    uploaded_at = Column(

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

        return f"<Gallery {self.title}>"




# =========================
# Database Index
# =========================


Index(

    "idx_gallery_status_created",

    GalleryModel.status,

    GalleryModel.uploaded_at

)


Index(

    "idx_gallery_category_active",

    GalleryModel.category,

    GalleryModel.is_deleted

)