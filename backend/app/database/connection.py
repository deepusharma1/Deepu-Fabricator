from sqlalchemy import create_engine
from sqlalchemy.orm import (
    sessionmaker,
    declarative_base
)

from app.config.settings import settings

import time
import logging


logger = logging.getLogger(__name__)


DATABASE_URL = settings.DATABASE_URL



# =====================================================
# ENGINE CONFIGURATION
# =====================================================

engine_options = {

    "echo": False

}



if DATABASE_URL.startswith("sqlite"):


    engine_options.update({

        "connect_args": {

            "check_same_thread": False

        }

    })


else:


    engine_options.update({

        "pool_pre_ping": True,

        "pool_size": 10,

        "max_overflow": 20,

        "pool_recycle": 1800,

        "pool_timeout": 30

    })





# =====================================================
# DATABASE CONNECTION RETRY
# =====================================================

MAX_RETRIES = 10


engine = None


for attempt in range(MAX_RETRIES):


    try:


        engine = create_engine(

            DATABASE_URL,

            **engine_options

        )


        with engine.connect():

            logger.info(

                "Database Connected Successfully"

            )

            break



    except Exception as error:


        logger.error(

            f"Database connection failed "
            f"{attempt + 1}/{MAX_RETRIES}: {error}"

        )



        if attempt == MAX_RETRIES - 1:

            raise error



        time.sleep(5)







# =====================================================
# SESSION FACTORY
# =====================================================


SessionLocal = sessionmaker(

    autocommit=False,

    autoflush=False,

    bind=engine

)






# =====================================================
# BASE MODEL
# =====================================================


Base = declarative_base()






# =====================================================
# DATABASE DEPENDENCY
# =====================================================


def get_db():


    db = SessionLocal()


    try:

        yield db


    finally:

        db.close()