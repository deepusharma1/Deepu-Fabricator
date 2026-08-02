# backend/app/utils/file_upload.py

import os
import uuid
from pathlib import Path
from shutil import copyfileobj

from fastapi import UploadFile, HTTPException


# =========================
# Upload Directory Config
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

UPLOAD_DIR = BASE_DIR / "static" / "uploads" / "gallery"


# =========================
# Allowed File Types
# =========================

ALLOWED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp"
}


# =========================
# Maximum File Size
# =========================

MAX_FILE_SIZE = 5 * 1024 * 1024   # 5 MB



# =========================
# Save Uploaded Image
# =========================

def save_uploaded_file(
    file: UploadFile
) -> str:


    try:

        # Validate filename
        if not file.filename:

            raise HTTPException(
                status_code=400,
                detail="Invalid file name"
            )


        # Check extension
        extension = Path(
            file.filename
        ).suffix.lower()


        if extension not in ALLOWED_EXTENSIONS:

            raise HTTPException(
                status_code=400,
                detail="Only JPG, JPEG, PNG and WEBP images are allowed"
            )



        # Check file size

        file_content = file.file.read()


        if len(file_content) > MAX_FILE_SIZE:

            raise HTTPException(
                status_code=400,
                detail="File size must be less than 5MB"
            )


        # Reset file pointer

        file.file.seek(0)



        # Create upload directory

        UPLOAD_DIR.mkdir(
            parents=True,
            exist_ok=True
        )



        # Generate unique filename

        unique_filename = (
            f"{uuid.uuid4()}{extension}"
        )



        file_path = (
            UPLOAD_DIR /
            unique_filename
        )



        # Save file

        with open(
            file_path,
            "wb"
        ) as buffer:

            copyfileobj(
                file.file,
                buffer
            )



        return (
            f"/static/uploads/gallery/{unique_filename}"
        )



    except HTTPException:

        raise



    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"File upload failed: {str(error)}"
        )