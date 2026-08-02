# backend/app/utils/logger.py

import logging
import logging.handlers
from pathlib import Path


# =========================
# Log Directory Configuration
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

LOG_DIR = BASE_DIR / "logs"

LOG_DIR.mkdir(
    parents=True,
    exist_ok=True
)


LOG_FILE = LOG_DIR / "server.log"



# =========================
# Logger Configuration
# =========================

logger = logging.getLogger(
    "DeepuFabricator"
)


logger.setLevel(
    logging.INFO
)



# Avoid duplicate handlers
if not logger.handlers:


    # File Handler with Rotation
    file_handler = logging.handlers.RotatingFileHandler(

        filename=LOG_FILE,

        maxBytes=10 * 1024 * 1024,   # 10 MB

        backupCount=5,

        encoding="utf-8"

    )


    # Log Format

    formatter = logging.Formatter(

        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(message)s"

    )


    file_handler.setFormatter(
        formatter
    )


    logger.addHandler(
        file_handler
    )


    # Console Handler (Docker/Uvicorn logs)

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(
        formatter
    )


    logger.addHandler(
        console_handler
    )