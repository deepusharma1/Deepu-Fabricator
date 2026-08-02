import bcrypt





# =====================================================
# PASSWORD HASH
# =====================================================


def hash_password(

    password: str

) -> str:


    if not password:


        raise ValueError(

            "Password cannot be empty"

        )



    if len(password) < 6:


        raise ValueError(

            "Password must be minimum 6 characters"

        )



    try:


        salt = bcrypt.gensalt(

            rounds=12

        )



        hashed = bcrypt.hashpw(

            password.encode("utf-8"),

            salt

        )



        return hashed.decode(

            "utf-8"

        )



    except Exception as error:


        raise RuntimeError(

            f"Password hashing failed: {str(error)}"

        )







# =====================================================
# PASSWORD VERIFY
# =====================================================


def verify_password(

    plain_password: str,

    hashed_password: str

) -> bool:


    try:


        if not plain_password or not hashed_password:

            return False



        return bcrypt.checkpw(

            plain_password.encode("utf-8"),

            hashed_password.encode("utf-8")

        )



    except Exception:


        return False