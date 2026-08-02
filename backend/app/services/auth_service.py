from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from datetime import datetime, timezone

from app.models.user import User

from app.utils.jwt import (
    create_access_token,
    create_refresh_token
)

from app.utils.password import (
    hash_password,
    verify_password
)



class AuthService:



    # =====================================================
    # LOGIN AUTHENTICATION
    # =====================================================

    @staticmethod
    def authenticate_user(

        db: Session,

        username: str,

        password: str

    ):


        try:


            user = (

                db.query(User)

                .filter(

                    User.username == username

                )

                .first()

            )



            if not user:

                return None



            # Account Status Check

            if not user.is_active:

                return None



            if user.account_locked:

                return None




            # Password Verification

            if not verify_password(

                password,

                user.hashed_password

            ):



                user.failed_login_attempts += 1



                if user.failed_login_attempts >= 5:

                    user.account_locked = True



                db.commit()


                return None





            # Successful Login


            user.failed_login_attempts = 0

            user.account_locked = False


            user.last_login = datetime.now(

                timezone.utc

            )


            db.commit()




            access_token = create_access_token(

                {

                    "sub": user.username,

                    "user_id": user.id,

                    "role": user.role

                }

            )




            refresh_token = create_refresh_token(

                {

                    "sub": user.username,

                    "user_id": user.id

                }

            )




            user.refresh_token = refresh_token


            db.commit()



            return {


                "access_token": access_token,


                "refresh_token": refresh_token,


                "token_type": "bearer"

            }





        except SQLAlchemyError:


            db.rollback()

            return None





    # =====================================================
    # CREATE USER
    # =====================================================


    @staticmethod
    def create_user(

        db: Session,

        username: str,

        email: str,

        password: str,

        full_name: str = None,

        mobile_number: str = None

    ):



        try:



            existing_user = (

                db.query(User)

                .filter(

                    (User.username == username)

                    |

                    (User.email == email)

                )

                .first()

            )



            if existing_user:

                raise Exception(

                    "Username or Email already exists"

                )





            user = User(


                username=username,


                email=email,


                hashed_password=hash_password(

                    password

                ),


                full_name=full_name,


                mobile_number=mobile_number,


                role="admin",


                is_active=True,


                is_verified=True

            )





            db.add(user)


            db.commit()


            db.refresh(user)



            return user





        except Exception as error:


            db.rollback()


            raise Exception(

                f"User creation failed: {str(error)}"

            )