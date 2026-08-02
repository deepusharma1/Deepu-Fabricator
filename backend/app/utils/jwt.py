from datetime import (
    datetime,
    timedelta,
    timezone
)

from typing import (
    Optional,
    Dict,
    Any
)

import jwt


from jwt import (
    PyJWTError,
    ExpiredSignatureError
)


from app.config.settings import settings





# =====================================================
# CREATE ACCESS TOKEN
# =====================================================

def create_access_token(

    data: dict,

    expires_delta: Optional[timedelta] = None

) -> str:


    payload = data.copy()



    expire = (

        datetime.now(timezone.utc)

        +

        (

            expires_delta

            or

            timedelta(

                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES

            )

        )

    )



    payload.update({

        "exp": expire,

        "iat": datetime.now(timezone.utc),

        "type": "access_token"

    })



    return jwt.encode(

        payload,

        settings.SECRET_KEY,

        algorithm=settings.ALGORITHM

    )






# =====================================================
# CREATE REFRESH TOKEN
# =====================================================

def create_refresh_token(

    data: dict

) -> str:



    payload = data.copy()



    expire = (

        datetime.now(timezone.utc)

        +

        timedelta(

            days=30

        )

    )



    payload.update({

        "exp": expire,

        "iat": datetime.now(timezone.utc),

        "type": "refresh_token"

    })



    return jwt.encode(

        payload,

        settings.SECRET_KEY,

        algorithm=settings.ALGORITHM

    )







# =====================================================
# COMMON JWT DECODER
# =====================================================

def _decode_token(

    token: str

) -> Optional[Dict[str, Any]]:


    try:


        return jwt.decode(

            token,

            settings.SECRET_KEY,

            algorithms=[

                settings.ALGORITHM

            ]

        )



    except (

        ExpiredSignatureError,

        PyJWTError

    ):


        return None







# =====================================================
# DECODE ACCESS TOKEN
# =====================================================

def decode_access_token(

    token: str

) -> Optional[Dict[str, Any]]:


    payload = _decode_token(token)



    if not payload:

        return None



    if payload.get("type") != "access_token":

        return None



    return payload







# =====================================================
# DECODE REFRESH TOKEN
# =====================================================

def decode_refresh_token(

    token: str

) -> Optional[Dict[str, Any]]:



    payload = _decode_token(token)



    if not payload:

        return None



    if payload.get("type") != "refresh_token":

        return None



    return payload







# =====================================================
# VERIFY TOKEN
# =====================================================

def verify_token(

    token: str

) -> Optional[Dict[str, Any]]:


    return _decode_token(token)