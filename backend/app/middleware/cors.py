# backend/app/middleware/cors.py


from fastapi.middleware.cors import CORSMiddleware

from app.config.settings import settings





def add_cors_middleware(app):

    app.add_middleware(

        CORSMiddleware,

        # Development + Production domains
        allow_origins=settings.ALLOWED_ORIGINS,

        allow_credentials=True,

        allow_methods=["*"],

        allow_headers=["*"],

    )