# backend/app/services/gallery.py


import os
import uuid

from shutil import copyfileobj

from fastapi import UploadFile, HTTPException

from sqlalchemy.orm import Session

from app.models.gallery import GalleryModel



UPLOAD_DIR = "static/uploads/gallery"


ALLOWED_EXTENSIONS = {

    ".jpg",
    ".jpeg",
    ".png",
    ".webp"

}


MAX_FILE_SIZE = 5 * 1024 * 1024   # 5MB



class GalleryService:



    @staticmethod
    def create_gallery_item(

        db: Session,

        title: str,

        category: str,

        file: UploadFile

    ):


        try:


            os.makedirs(

                UPLOAD_DIR,

                exist_ok=True

            )


            # =========================
            # File Extension Validation
            # =========================


            extension = os.path.splitext(

                file.filename

            )[1].lower()



            if extension not in ALLOWED_EXTENSIONS:


                raise HTTPException(

                    status_code=400,

                    detail="Only jpg, jpeg, png and webp images allowed"

                )



            # =========================
            # File Size Validation
            # =========================


            file.file.seek(0, 2)

            file_size = file.file.tell()

            file.file.seek(0)



            if file_size > MAX_FILE_SIZE:


                raise HTTPException(

                    status_code=400,

                    detail="Image size must be less than 5MB"

                )



            # =========================
            # Unique Filename
            # =========================


            unique_filename = (

                f"{uuid.uuid4().hex}{extension}"

            )



            file_path = os.path.join(

                UPLOAD_DIR,

                unique_filename

            )



            # =========================
            # Save File
            # =========================


            with open(

                file_path,

                "wb"

            ) as buffer:


                copyfileobj(

                    file.file,

                    buffer

                )



            image_url = (

                f"/static/uploads/gallery/{unique_filename}"

            )



            # =========================
            # Database Save
            # =========================


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



        except Exception as e:


            db.rollback()


            raise HTTPException(

                status_code=500,

                detail="Gallery upload failed"

            )





    @staticmethod
    def get_all_gallery_items(

        db: Session,

        page: int = 1,

        limit: int = 20

    ):


        offset = (

            page - 1

        ) * limit



        return (

            db.query(GalleryModel)

            .order_by(

                GalleryModel.id.desc()

            )

            .offset(offset)

            .limit(limit)

            .all()

        )