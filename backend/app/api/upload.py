# backend/app/api/upload.py

from fastapi import APIRouter

router = APIRouter(
    prefix="/api/upload",
    tags=["Admin Asset Gallery Storage Upload Engine"]
)


# =====================================================
# Gallery Image Upload API Temporarily Disabled
# Static Gallery Images are used from frontend assets
# Future me upload chahiye ho to niche code uncomment kare
# =====================================================


# import os
# import shutil
# from datetime import datetime
# from fastapi import HTTPException, Depends, UploadFile, File, Form
# from sqlalchemy.orm import Session
# from app.database.connection import get_db
# from app.models.gallery import GalleryModel


# UPLOAD_DIR = os.path.join(
#     os.path.dirname(os.path.dirname(__file__)),
#     "uploads",
#     "images"
# )


# if not os.path.exists(UPLOAD_DIR):
#     os.makedirs(UPLOAD_DIR, exist_ok=True)



# @router.post("/")
# async def upload_fabrication_image(
#     title: str = Form(...),
#     category: str = Form(...),
#     file: UploadFile = File(...),
#     db: Session = Depends(get_db)
# ):

#     if not file.content_type.startswith("image/"):
#         raise HTTPException(
#             status_code=400,
#             detail="Only image files allowed"
#         )


#     raw_filename = file.filename


#     timestamp = datetime.now().strftime(
#         "%Y%m%d_%H%M%S"
#     )


#     filename = (
#         f"{timestamp}_{raw_filename}"
#         .replace(" ", "_")
#     )


#     file_path = os.path.join(
#         UPLOAD_DIR,
#         filename
#     )


#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(
#             file.file,
#             buffer
#         )


#     image_url = (
#         f"/uploads/images/{filename}"
#     )


#     gallery = GalleryModel(
#         title=title,
#         category=category,
#         image_url=image_url
#     )


#     db.add(gallery)
#     db.commit()
#     db.refresh(gallery)


#     return {
#         "message": "Image uploaded successfully",
#         "id": gallery.id,
#         "image": image_url
#     }