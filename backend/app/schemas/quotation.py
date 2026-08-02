# backend/app/schemas/quotation.py


from pydantic import (

    BaseModel,

    Field,

    ConfigDict

)


from typing import (

    Optional,

    List

)


from datetime import datetime







# =====================================================
# QUOTATION ITEM SCHEMA
# =====================================================


class QuotationItemSchema(BaseModel):


    material_name: str = Field(

        ...,

        min_length=1,

        max_length=100

    )



    description: Optional[str] = None



    quantity: float = Field(

        default=1,

        gt=0

    )



    unit: str = "Nos"



    rate: float = Field(

        default=0,

        ge=0

    )



    amount: float = Field(

        default=0,

        ge=0

    )









# =====================================================
# CREATE QUOTATION SCHEMA
# =====================================================


class QuotationCreate(BaseModel):


    customer_name: str = Field(

        ...,

        min_length=2,

        max_length=150

    )



    company_name: Optional[str] = (

        "DEEPU FABRICATOR"

    )



    mobile_number: str = Field(

        ...,

        min_length=10,

        max_length=15

    )



    email: Optional[str] = None



    address: Optional[str] = None





    lead_source: Optional[str] = None





    work_type: str = (

        "Steel Gate / Grill"

    )





    material_type: Optional[str] = None





    width_ft: float = Field(

        default=0,

        ge=0

    )



    height_ft: float = Field(

        default=0,

        ge=0

    )



    rate_per_sqft: float = Field(

        default=0,

        ge=0

    )







    items: List[QuotationItemSchema] = Field(

        default_factory=list

    )







    labour_cost: float = Field(

        default=0,

        ge=0

    )



    installation_cost: float = Field(

        default=0,

        ge=0

    )



    transport_cost: float = Field(

        default=0,

        ge=0

    )



    other_charges: float = Field(

        default=0,

        ge=0

    )



    discount: float = Field(

        default=0,

        ge=0

    )





    gst_percent: float = Field(

        default=18,

        ge=0

    )





    notes: Optional[str] = None



    payment_terms: Optional[str] = (

        "50% Advance Payment"

    )



    delivery_time: Optional[str] = (

        "As per project schedule"

    )









# =====================================================
# UPDATE QUOTATION SCHEMA
# =====================================================


class QuotationUpdate(BaseModel):


    customer_name: Optional[str] = None



    company_name: Optional[str] = None



    mobile_number: Optional[str] = None



    email: Optional[str] = None



    address: Optional[str] = None



    work_type: Optional[str] = None



    status: Optional[str] = None



    notes: Optional[str] = None



    payment_terms: Optional[str] = None



    delivery_time: Optional[str] = None



    is_locked: Optional[bool] = None







# =====================================================
# RESPONSE SCHEMA
# =====================================================


class QuotationResponse(BaseModel):


    id: int



    quotation_no: str



    revision_no: int





    customer_name: str



    company_name: Optional[str] = None



    mobile_number: str



    email: Optional[str] = None



    address: Optional[str] = None





    lead_source: Optional[str] = None





    work_type: str



    material_type: Optional[str] = None





    width_ft: float



    height_ft: float



    total_area_sqft: float





    rate_per_sqft: float





    estimated_cost: float



    labour_cost: float



    installation_cost: float



    transport_cost: float



    other_charges: float



    discount: float





    gst_percent: float



    gst_amount: float



    grand_total: float





    items_json: Optional[list] = None





    notes: Optional[str] = None





    payment_terms: Optional[str] = None



    delivery_time: Optional[str] = None



    valid_until: Optional[datetime] = None





    status: str



    is_locked: bool





    pdf_file: Optional[str] = None





    created_by: Optional[int] = None



    approved_at: Optional[datetime] = None





    is_deleted: bool





    created_at: datetime



    updated_at: datetime






    model_config = ConfigDict(

        from_attributes=True

    )