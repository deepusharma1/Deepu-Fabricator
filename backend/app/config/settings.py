from typing import List

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)



class Settings(BaseSettings):


    # =========================
    # Application
    # =========================

    APP_NAME: str = (
        "Deepu Fabricator API Portal"
    )


    APP_VERSION: str = "1.6.0"


    ENVIRONMENT: str = "production"


    PORT: int = 8000





    # =========================
    # JWT Configuration
    # =========================

    SECRET_KEY: str


    ALGORITHM: str = "HS256"


    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440


    REFRESH_TOKEN_EXPIRE_DAYS: int = 30






    # =========================
    # Database
    # =========================

    DATABASE_URL: str






    # =========================
    # Admin Authentication
    # =========================

    ADMIN_USERNAME: str = "admin"


    ADMIN_PASSWORD_HASH: str






    # =========================
    # CORS
    # =========================

    ALLOWED_ORIGINS: List[str] = [

        "http://localhost:5173",

        "http://localhost:3000",

        "https://deepufabricator.com",

        "https://www.deepufabricator.com"

    ]







    # =========================
    # File Upload
    # =========================

    MAX_UPLOAD_SIZE_MB: int = 5


    ALLOWED_IMAGE_TYPES: List[str] = [

        "image/jpeg",

        "image/png",

        "image/webp"

    ]



    UPLOAD_DIRECTORY: str = (

        "static/uploads/gallery"

    )







    # =========================
    # Security
    # =========================

    MAX_LOGIN_ATTEMPTS: int = 5


    SESSION_TIMEOUT_MINUTES: int = 30






    # =========================
    # Pydantic Config
    # =========================

    model_config = SettingsConfigDict(

        env_file=".env",

        env_file_encoding="utf-8",

        case_sensitive=True,

        extra="ignore"

    )






settings = Settings()