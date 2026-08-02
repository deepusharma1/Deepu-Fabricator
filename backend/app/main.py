# backend/app/main.py


import os


from pathlib import Path


from datetime import (

    datetime,

    timedelta,

    timezone

)


from contextlib import asynccontextmanager



from fastapi import FastAPI



from fastapi.middleware.cors import CORSMiddleware



from fastapi.staticfiles import StaticFiles



from sqlalchemy.orm import Session

from app.api.users import router as users_router




# =====================================================
# DATABASE
# =====================================================


from app.database.connection import (

    SessionLocal,

    engine,

    Base

)







# =====================================================
# MODELS
# =====================================================


from app.models.contact import ContactModel


from app.models.quotation import QuotationModel


from app.models.gallery import GalleryModel


from app.models.user import User








# =====================================================
# ROUTERS
# =====================================================


from app.api.contact import router as contact_router


from app.api.quotation import router as quotation_router


from app.api.admin import router as admin_router


from app.api.auth import router as auth_router


from app.api.gallery import router as gallery_router


from app.api.users import router as users_router







# =====================================================
# CONFIG
# =====================================================


from app.config.settings import settings




from app.utils.logger import logger








# =====================================================
# PATH CONFIG
# =====================================================


BASE_DIR = Path(__file__).resolve().parent.parent




GALLERY_PATH = (

    BASE_DIR

    /

    "static"

    /

    "uploads"

    /

    "gallery"

)




GALLERY_PATH.mkdir(

    parents=True,

    exist_ok=True

)









# =====================================================
# STORAGE CLEANER
# =====================================================


def storage_cleaner():


    db: Session = SessionLocal()



    try:



        expiry_date = (

            datetime.now(timezone.utc)

            -

            timedelta(days=90)

        )




        deleted_files = 0






        old_gallery = (



            db.query(GalleryModel)



            .filter(



                GalleryModel.uploaded_at < expiry_date



            )



            .all()



        )






        for image in old_gallery:



            if image.image_url:



                file_name = os.path.basename(

                    image.image_url

                )



                file_path = (

                    GALLERY_PATH

                    /

                    file_name

                )



                if file_path.exists():



                    file_path.unlink()



                    deleted_files += 1








        deleted_gallery = (



            db.query(GalleryModel)



            .filter(



                GalleryModel.uploaded_at < expiry_date



            )



            .delete(



                synchronize_session=False



            )



        )








        deleted_contact = (



            db.query(ContactModel)



            .filter(



                ContactModel.created_at < expiry_date



            )



            .delete(



                synchronize_session=False



            )



        )








        deleted_quote = (



            db.query(QuotationModel)



            .filter(



                QuotationModel.created_at < expiry_date



            )



            .delete(



                synchronize_session=False



            )



        )







        db.commit()





        logger.info(


            "Storage Cleaner Completed | "

            f"Gallery:{deleted_gallery} "

            f"Contact:{deleted_contact} "

            f"Quotation:{deleted_quote} "

            f"Files:{deleted_files}"


        )







    except Exception as error:



        db.rollback()



        logger.error(


            f"Storage Cleaner Failed : {error}"


        )







    finally:



        db.close()










# =====================================================
# APPLICATION LIFESPAN
# =====================================================


@asynccontextmanager
async def lifespan(app:FastAPI):


    logger.info(

        "Deepu Fabricator API Starting..."

    )



    try:



        with engine.connect():



            logger.info(

                "Database Connection Successful"

            )






        Base.metadata.create_all(

            bind=engine

        )



        logger.info(

            "Database Tables Verified"

        )





        storage_cleaner()





    except Exception as error:



        logger.error(

            f"Startup Failed : {error}"

        )



        raise error





    yield





    logger.info(

        "Deepu Fabricator API Shutdown"

    )









# =====================================================
# FASTAPI APP
# =====================================================


app = FastAPI(



    title=settings.APP_NAME,



    description="Deepu Fabricator Production API",



    version=settings.APP_VERSION,



    lifespan=lifespan



)









# =====================================================
# CORS
# =====================================================


app.add_middleware(



    CORSMiddleware,



    allow_origins=settings.ALLOWED_ORIGINS,



    allow_credentials=True,



    allow_methods=["*"],



    allow_headers=["*"]



)









# =====================================================
# STATIC FILE
# =====================================================


app.mount(



    "/static/uploads/gallery",



    StaticFiles(

        directory=str(GALLERY_PATH)

    ),



    name="gallery"



)









# =====================================================
# HEALTH CHECK
# =====================================================


@app.get("/health")
def health():


    return {



        "status":"healthy",



        "application":settings.APP_NAME,



        "version":settings.APP_VERSION



    }









# =====================================================
# ROOT
# =====================================================


@app.get("/")
def root():


    return {



        "status":"online",



        "message":

        "Deepu Fabricator Backend Running Successfully"



    }









# =====================================================
# API VERSION
# =====================================================


API_PREFIX="/api/v1"









# =====================================================
# ROUTER REGISTER
# =====================================================


app.include_router(

    contact_router,

    prefix=API_PREFIX

)



app.include_router(

    quotation_router,

    prefix=API_PREFIX

)



app.include_router(

    admin_router,

    prefix=API_PREFIX

)



app.include_router(

    auth_router,

    prefix=API_PREFIX

)



app.include_router(

    gallery_router,

    prefix=API_PREFIX

)



app.include_router(

    users_router,

    prefix=API_PREFIX

)