# backend/app/services/upload_service.py

from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.utils.file_upload import save_uploaded_file
from app.models.gallery import GalleryModel


class UploadService:

    @staticmethod
    def handle_gallery_upload(
        db: Session,
        title: str,
        category: str,
        file: UploadFile
    ):

        try:

            # Validate file exists
            if not file:
                raise HTTPException(
                    status_code=400,
                    detail="Image file is required"
                )


            # Allowed image formats
            allowed_types = [
                "image/jpeg",
                "image/png",
                "image/jpg",
                "image/webp"
            ]


            if file.content_type not in allowed_types:

                raise HTTPException(
                    status_code=400,
                    detail="Only JPG, PNG and WEBP images are allowed"
                )


            # File size validation (5 MB)
            max_file_size = 5 * 1024 * 1024

            file_content = file.file.read()

            if len(file_content) > max_file_size:

                raise HTTPException(
                    status_code=400,
                    detail="Image size must be less than 5 MB"
                )


            # Reset file pointer after reading
            file.file.seek(0)


            # Save image
            image_url = save_uploaded_file(file)


            # Save database record
            gallery_item = GalleryModel(
                title=title,
                category=category,
                image_url=image_url
            )


            db.add(gallery_item)

            db.commit()

            db.refresh(gallery_item)


            return gallery_item


        except HTTPException:
            raise


        except SQLAlchemyError as error:

            db.rollback()

            raise HTTPException(
                status_code=500,
                detail=f"Database error while saving image: {str(error)}"
            )


        except Exception as error:

            db.rollback()

            raise HTTPException(
                status_code=500,
                detail=f"Unexpected upload error: {str(error)}"
            )