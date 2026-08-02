# backend/app/middleware/exception_handler.py


from fastapi import (
    Request,
    HTTPException
)


from fastapi.responses import JSONResponse


from app.utils.logger import logger






# =========================
# Global Exception Handler
# =========================


async def global_exception_handler(

    request: Request,

    exc: Exception

):


    logger.error(

        f"URL: {request.url.path} | "
        f"Method: {request.method} | "
        f"Error: {str(exc)}"

    )



    return JSONResponse(

        status_code=500,

        content={


            "status": "error",


            "message":

            "Internal server error. Please try again later."


        }

    )









# =========================
# HTTP Exception Handler
# =========================


async def http_exception_handler(

    request: Request,

    exc: HTTPException

):


    logger.warning(

        f"HTTP Error | "
        f"URL: {request.url.path} | "
        f"Status: {exc.status_code} | "
        f"Detail: {exc.detail}"

    )



    return JSONResponse(

        status_code=exc.status_code,


        content={


            "status": "fail",


            "detail": exc.detail


        }

    )