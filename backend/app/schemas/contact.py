from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    ConfigDict
)

from typing import Optional

from datetime import datetime



class ContactCreate(BaseModel):


    fullName: str = Field(
        ...,
        min_length=3
    )


    mobileNumber: str = Field(
        ...,
        min_length=10,
        max_length=15
    )


    emailAddress: Optional[EmailStr] = None


    requirementType: str = Field(
        ...,
        min_length=3
    )


    message: str = Field(
        ...,
        min_length=5
    )





class ContactResponse(BaseModel):


    id:int


    full_name:str


    mobile_number:str


    email_address:Optional[str]


    requirement_type:str


    message:str


    status:str


    created_at:datetime


    updated_at:datetime



    model_config = ConfigDict(

        from_attributes=True

    )