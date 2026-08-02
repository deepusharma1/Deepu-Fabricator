# backend/app/api/gallery.py


import os

from datetime import datetime, timezone

from pathlib import Path


from fastapi import (

    APIRouter,

    Depends,

    HTTPException,

    UploadFile,

    File,

    Query

)


from fastapi.responses import JSONResponse


from sqlalchemy.orm import Session



from app.database.connection import get_db


from app.models.gallery import GalleryModel


from app.utils.dependencies import get_current_admin






router = APIRouter(

    prefix="/gallery",

    tags=[

        "Gallery Management"

    ]

)





# =====================================================
# UPLOAD DIRECTORY
# =====================================================


BASE_DIR = Path(__file__).resolve().parent.parent.parent


UPLOAD_DIR = (

    BASE_DIR

    /

    "static"

    /

    "uploads"

    /

    "gallery"

)



UPLOAD_DIR.mkdir(

    parents=True,

    exist_ok=True

)









# =====================================================
# UPLOAD IMAGE
# POST /api/v1/gallery/upload
# =====================================================


@router.post("/upload")
def upload_gallery_image(


    title:str,


    file:UploadFile = File(...),


    db:Session = Depends(get_db),


    admin = Depends(get_current_admin)


):



    allowed_extensions = [


        ".jpg",

        ".jpeg",

        ".png",

        ".webp"


    ]




    extension = Path(file.filename).suffix.lower()



    if extension not in allowed_extensions:


        raise HTTPException(

            status_code=400,

            detail="Only jpg, jpeg, png, webp allowed"

        )





    filename = (

        datetime.now()

        .strftime("%Y%m%d%H%M%S")

        +

        extension

    )





    file_path = UPLOAD_DIR / filename




    try:



        with open(file_path,"wb") as buffer:


            buffer.write(

                file.file.read()

            )






        image_url = (

            f"/static/uploads/gallery/{filename}"

        )






        gallery = GalleryModel(


            title=title,


            image_url=image_url,


            uploaded_at=datetime.now(timezone.utc)


        )




        db.add(gallery)


        db.commit()


        db.refresh(gallery)





        return {



            "status":"success",


            "message":"Image uploaded successfully",


            "data":{


                "id":gallery.id,

                "title":gallery.title,

                "image_url":gallery.image_url


            }



        }





    except Exception as error:



        db.rollback()



        if file_path.exists():

            file_path.unlink()



        raise HTTPException(

            status_code=500,

            detail=str(error)

        )









# =====================================================
# GET ALL GALLERY
# GET /api/v1/gallery
# =====================================================


@router.get("/")
def get_gallery(



    page:int = Query(1,ge=1),


    limit:int = Query(20,ge=1,le=100),


    db:Session = Depends(get_db)



):



    offset=(page-1)*limit






    total=(



        db.query(GalleryModel)



        .count()



    )








    images=(



        db.query(GalleryModel)



        .order_by(



            GalleryModel.id.desc()



        )



        .offset(offset)



        .limit(limit)



        .all()



    )






    return {



        "status":"success",


        "total":total,


        "page":page,


        "limit":limit,



        "data":[



            {



                "id":img.id,


                "title":img.title,


                "image_url":img.image_url,


                "uploaded_at":img.uploaded_at



            }


            for img in images



        ]



    }









# =====================================================
# GET SINGLE IMAGE
# GET /api/v1/gallery/{id}
# =====================================================


@router.get("/{gallery_id}")
def get_gallery_image(



    gallery_id:int,


    db:Session = Depends(get_db)



):



    image=(



        db.query(GalleryModel)



        .filter(



            GalleryModel.id == gallery_id



        )



        .first()



    )






    if not image:



        raise HTTPException(


            status_code=404,


            detail="Image not found"


        )






    return {



        "status":"success",


        "data":{


            "id":image.id,


            "title":image.title,


            "image_url":image.image_url,


            "uploaded_at":image.uploaded_at


        }



    }









# =====================================================
# DELETE IMAGE
# DELETE /api/v1/gallery/{id}
# =====================================================


@router.delete("/{gallery_id}")
def delete_gallery_image(



    gallery_id:int,


    db:Session = Depends(get_db),


    admin = Depends(get_current_admin)



):



    image=(



        db.query(GalleryModel)



        .filter(



            GalleryModel.id == gallery_id



        )



        .first()



    )





    if not image:



        raise HTTPException(


            status_code=404,


            detail="Image not found"


        )






    try:



        if image.image_url:



            filename=os.path.basename(


                image.image_url


            )



            file_path=UPLOAD_DIR / filename



            if file_path.exists():

                file_path.unlink()






        db.delete(image)


        db.commit()





        return {



            "status":"success",


            "message":"Image deleted successfully"



        }





    except Exception as error:



        db.rollback()



        raise HTTPException(


            status_code=500,


            detail=str(error)


        )