# backend/app/schemas/auth.py


from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    ConfigDict
)

from typing import Optional

from datetime import datetime




# =====================================================
# LOGIN REQUEST
# =====================================================

class LoginRequest(BaseModel):

    username: str = Field(

        ...,

        min_length=3,

        max_length=100

    )


    password: str = Field(

        ...,

        min_length=6,

        max_length=100

    )





# =====================================================
# REGISTER REQUEST
# =====================================================

class RegisterRequest(BaseModel):


    username: str = Field(

        ...,

        min_length=3,

        max_length=100

    )


    email: EmailStr



    password: str = Field(

        ...,

        min_length=6,

        max_length=100

    )


    full_name: Optional[str] = None


    mobile_number: Optional[str] = None





# =====================================================
# REFRESH TOKEN REQUEST
# =====================================================

class RefreshTokenRequest(BaseModel):

    refresh_token: str





# =====================================================
# JWT TOKEN RESPONSE
# =====================================================

class TokenResponse(BaseModel):


    access_token: str


    refresh_token: Optional[str] = None


    token_type: str = "bearer"


    expires_in: Optional[int] = None





# =====================================================
# USER RESPONSE
# =====================================================

class UserResponse(BaseModel):


    id: int


    username: str


    email: str


    full_name: Optional[str] = None


    mobile_number: Optional[str] = None


    role: str


    is_active: bool


    is_verified: bool


    last_login: Optional[datetime] = None


    created_at: datetime



    model_config = ConfigDict(

        from_attributes=True

    )





# =====================================================
# CHANGE PASSWORD REQUEST
# =====================================================

class ChangePasswordRequest(BaseModel):


    old_password: str = Field(

        ...,

        min_length=6,

        max_length=100

    )


    new_password: str = Field(

        ...,

        min_length=6,

        max_length=100

    )





# =====================================================
# FORGOT PASSWORD REQUEST
# =====================================================

class ForgotPasswordRequest(BaseModel):

    email: EmailStr





# =====================================================
# RESET PASSWORD REQUEST
# =====================================================

class ResetPasswordRequest(BaseModel):


    token: str = Field(

        ...,

        min_length=10

    )


    new_password: str = Field(

        ...,

        min_length=6,

        max_length=100

    )