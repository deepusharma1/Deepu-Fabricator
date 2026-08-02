# backend/app/models/quotation.py


from sqlalchemy import (

    Column,
    Integer,
    String,
    DateTime,
    Text,
    Index,
    Numeric,
    Boolean,
    JSON

)


from datetime import datetime, timezone


from app.database.connection import Base






class QuotationModel(Base):


    __tablename__ = "quotations"





    # =====================================================
    # PRIMARY KEY
    # =====================================================


    id = Column(

        Integer,

        primary_key=True,

        index=True

    )






    # =====================================================
    # QUOTATION INFORMATION
    # =====================================================


    quotation_no = Column(

        String(50),

        unique=True,

        nullable=False,

        index=True

    )



    revision_no = Column(

        Integer,

        default=1,

        nullable=False

    )








    # =====================================================
    # CUSTOMER DETAILS
    # =====================================================


    customer_name = Column(

        String(150),

        nullable=False

    )



    company_name = Column(

        String(150),

        nullable=True

    )



    mobile_number = Column(

        String(20),

        nullable=False,

        index=True

    )



    email = Column(

        String(150),

        nullable=True,

        index=True

    )



    address = Column(

        Text,

        nullable=True

    )








    # =====================================================
    # LEAD INFORMATION
    # =====================================================


    lead_source = Column(

        String(50),

        nullable=True

    )








    # =====================================================
    # WORK DETAILS
    # =====================================================


    work_type = Column(

        String(150),

        nullable=False,

        index=True

    )



    material_type = Column(

        String(100),

        nullable=True

    )



    width_ft = Column(

        Numeric(10,2),

        default=0,

        nullable=False

    )



    height_ft = Column(

        Numeric(10,2),

        default=0,

        nullable=False

    )



    total_area_sqft = Column(

        Numeric(10,2),

        default=0,

        nullable=False

    )








    # =====================================================
    # PRICE DETAILS
    # =====================================================


    rate_per_sqft = Column(

        Numeric(12,2),

        default=0,

        nullable=False

    )



    estimated_cost = Column(

        Numeric(12,2),

        default=0,

        nullable=False

    )



    labour_cost = Column(

        Numeric(12,2),

        default=0,

        nullable=False

    )



    installation_cost = Column(

        Numeric(12,2),

        default=0,

        nullable=False

    )



    transport_cost = Column(

        Numeric(12,2),

        default=0,

        nullable=False

    )



    other_charges = Column(

        Numeric(12,2),

        default=0,

        nullable=False

    )



    discount = Column(

        Numeric(12,2),

        default=0,

        nullable=False

    )



    gst_percent = Column(

        Numeric(5,2),

        default=18,

        nullable=False

    )



    gst_amount = Column(

        Numeric(12,2),

        default=0,

        nullable=False

    )



    grand_total = Column(

        Numeric(12,2),

        default=0,

        nullable=False

    )








    # =====================================================
    # ITEMS
    # =====================================================


    items_json = Column(

        JSON,

        nullable=True

    )



    notes = Column(

        Text,

        nullable=True

    )








    # =====================================================
    # COMMERCIAL TERMS
    # =====================================================


    payment_terms = Column(

        Text,

        nullable=True

    )



    delivery_time = Column(

        String(100),

        nullable=True

    )



    valid_until = Column(

        DateTime,

        nullable=True

    )








    # =====================================================
    # STATUS MANAGEMENT
    # =====================================================


    status = Column(

        String(30),

        default="Draft",

        nullable=False,

        index=True

    )



    is_locked = Column(

        Boolean,

        default=False,

        nullable=False

    )








    # =====================================================
    # PDF
    # =====================================================


    pdf_file = Column(

        String(255),

        nullable=True

    )








    # =====================================================
    # USER TRACKING
    # =====================================================


    created_by = Column(

        Integer,

        nullable=True

    )



    approved_at = Column(

        DateTime,

        nullable=True

    )








    # =====================================================
    # SOFT DELETE
    # =====================================================


    is_deleted = Column(

        Boolean,

        default=False,

        nullable=False,

        index=True

    )








    # =====================================================
    # AUDIT
    # =====================================================


    created_at = Column(

        DateTime,

        default=lambda:

        datetime.now(timezone.utc),

        nullable=False,

        index=True

    )



    updated_at = Column(

        DateTime,

        default=lambda:

        datetime.now(timezone.utc),


        onupdate=lambda:

        datetime.now(timezone.utc),


        nullable=False

    )








    def __repr__(self):


        return f"<Quotation {self.quotation_no}>"








# =====================================================
# DATABASE INDEX
# =====================================================


Index(

    "idx_quotation_status_created",

    QuotationModel.status,

    QuotationModel.created_at

)



Index(

    "idx_quotation_customer_mobile",

    QuotationModel.customer_name,

    QuotationModel.mobile_number

)