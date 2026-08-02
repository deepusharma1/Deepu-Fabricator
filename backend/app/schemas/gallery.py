# backend/app/schemas/gallery.py


from pydantic import (
    BaseModel,
    Field,
    ConfigDict
)

from datetime import datetime

from typing import Optional





# =====================================================
# Base Gallery Schema
# =====================================================

class GalleryBase(BaseModel):


    title: str = Field(

        ...,

        min_length=3,

        max_length=100

    )


    category: str = Field(

        ...,

        min_length=3,

        max_length=50

    )





# =====================================================
# Create Gallery Schema
# =====================================================

class GalleryCreate(GalleryBase):


    image_url: str = Field(

        ...,

        min_length=5,

        max_length=255

    )






# =====================================================
# Update Gallery Schema
# =====================================================

class GalleryUpdate(BaseModel):


    title: Optional[str] = None


    category: Optional[str] = None


    image_url: Optional[str] = None






# =====================================================
# Gallery Response Schema
# =====================================================

class GalleryResponse(GalleryBase):


    id: int


    image_url: str


    uploaded_at: datetime


    is_deleted: bool



    model_config = ConfigDict(

        from_attributes=True

    )