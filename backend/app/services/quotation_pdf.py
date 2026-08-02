# backend/app/services/quotation_pdf.py

import io
import os

from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib.enums import (
    TA_CENTER,
    TA_RIGHT
)

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)


# ===============================
# CURRENCY FORMAT
# ===============================

def format_currency(value):

    try:
        return f"₹ {float(value):,.2f}"

    except Exception:
        return "₹ 0.00"



# ===============================
# SAFE TEXT
# ===============================

def safe(value):

    if value is None:
        return "-"

    return str(value)



# ===============================
# GENERATE QUOTATION PDF
# ===============================

def generate_quotation_pdf(quotation):


    buffer = io.BytesIO()



    doc = SimpleDocTemplate(

        buffer,

        pagesize=A4,

        rightMargin=35,

        leftMargin=35,

        topMargin=35,

        bottomMargin=35

    )



    styles = getSampleStyleSheet()



    title_style = ParagraphStyle(

        "TitleCustom",

        parent=styles["Title"],

        fontSize=20,

        alignment=TA_CENTER,

        spaceAfter=8

    )



    center_style = ParagraphStyle(

        "CenterCustom",

        parent=styles["Normal"],

        alignment=TA_CENTER,

        fontSize=10

    )



    right_style = ParagraphStyle(

        "RightCustom",

        parent=styles["Normal"],

        alignment=TA_RIGHT

    )



    heading_style = ParagraphStyle(

        "HeadingCustom",

        parent=styles["Heading3"],

        fontSize=12

    )



    story=[]



    # ===============================
    # COMPANY HEADER
    # ===============================


    logo_path="app/static/logo.png"


    if os.path.exists(logo_path):

        logo = Image(

            logo_path,

            width=70,

            height=70

        )


        logo.hAlign="CENTER"


        story.append(logo)

        story.append(
            Spacer(1,8)
        )



    story.append(

        Paragraph(

            "DEEPU FABRICATOR",

            title_style

        )

    )


    story.append(

        Paragraph(

            "MS Gate | Grill | Railing | Shed | Fabrication Work",

            center_style

        )

    )


    story.append(

        Paragraph(

            """
            Address: Your Business Address<br/>
            Mobile: **********<br/>
            Email: yourmail@example.com<br/>
            GST No: **************
            """,

            center_style

        )

    )


    story.append(
        Spacer(1,15)
    )


    story.append(

        Paragraph(

            "<b>QUOTATION</b>",

            title_style

        )

    )


    story.append(
        Spacer(1,10)
    )

        # ===============================
    # QUOTATION INFORMATION
    # ===============================


    quotation_info = [

        [
            "Quotation No",
            safe(quotation.quotation_no)
        ],

        [
            "Quotation Date",
            quotation.created_at.strftime("%d-%m-%Y")
            if quotation.created_at
            else datetime.now().strftime("%d-%m-%Y")
        ],

        [
            "Valid Until",
            quotation.valid_until.strftime("%d-%m-%Y")
            if quotation.valid_until
            else "-"
        ],

        [
            "Revision No",
            safe(quotation.revision_no)
        ],

        [
            "Work Type",
            safe(quotation.work_type)
        ]

    ]



    quotation_table = Table(

        quotation_info,

        colWidths=[130,280]

    )



    quotation_table.setStyle(

        TableStyle([


            (
                "GRID",
                (0,0),
                (-1,-1),
                0.5,
                colors.black
            ),


            (
                "BACKGROUND",
                (0,0),
                (0,-1),
                colors.lightgrey
            )

        ])

    )


    story.append(
        quotation_table
    )


    story.append(
        Spacer(1,15)
    )



    # ===============================
    # CUSTOMER DETAILS
    # ===============================


    story.append(

        Paragraph(

            "<b>Customer Details</b>",

            heading_style

        )

    )


    customer_data=[


        [
            "Customer Name",
            safe(quotation.customer_name)
        ],


        [
            "Company Name",
            safe(quotation.company_name)
        ],


        [
            "Mobile Number",
            safe(quotation.mobile_number)
        ],


        [
            "Email",
            safe(quotation.email)
        ],


        [
            "Address",
            safe(quotation.address)
        ]

    ]



    customer_table = Table(

        customer_data,

        colWidths=[130,280]

    )



    customer_table.setStyle(

        TableStyle([


            (
                "GRID",
                (0,0),
                (-1,-1),
                0.5,
                colors.black
            ),


            (
                "BACKGROUND",
                (0,0),
                (0,-1),
                colors.whitesmoke
            )

        ])

    )



    story.append(

        customer_table

    )


    story.append(

        Spacer(1,20)

    )




    # ===============================
    # ITEM DETAILS
    # ===============================


    story.append(

        Paragraph(

            "<b>Material / Work Details</b>",

            heading_style

        )

    )



    item_data=[


        [

            "S.No",

            "Material",

            "Description",

            "Qty",

            "Rate",

            "Amount"

        ]

    ]



    serial=1



    if quotation.items_json:


        for item in quotation.items_json:


            item_data.append(

                [

                    str(serial),

                    safe(
                        item.get(
                            "material_name",
                            ""
                        )
                    ),


                    safe(
                        item.get(
                            "description",
                            ""
                        )
                    ),


                    safe(
                        item.get(
                            "quantity",
                            0
                        )
                    ),


                    format_currency(

                        item.get(
                            "rate",
                            0
                        )

                    ),


                    format_currency(

                        item.get(
                            "amount",
                            0
                        )

                    )

                ]

            )


            serial += 1



    item_table = Table(

        item_data,

        colWidths=[35,90,140,40,55,70],

        repeatRows=1

    )



    item_table.setStyle(

        TableStyle([


            (
                "GRID",
                (0,0),
                (-1,-1),
                0.5,
                colors.black
            ),


            (
                "BACKGROUND",
                (0,0),
                (-1,0),
                colors.lightgrey
            )

        ])

    )



    story.append(

        item_table

    )


    story.append(

        Spacer(1,20)

    )
        # ===============================
    # COST SUMMARY
    # ===============================


    story.append(

        Paragraph(

            "<b>Price Summary</b>",

            heading_style

        )

    )



    summary_data=[


        [
            "Estimated Cost",
            format_currency(
                quotation.estimated_cost
            )
        ],


        [
            "Labour Cost",
            format_currency(
                quotation.labour_cost
            )
        ],


        [
            "Installation Cost",
            format_currency(
                quotation.installation_cost
            )
        ],


        [
            "Transport Cost",
            format_currency(
                quotation.transport_cost
            )
        ],


        [
            "Other Charges",
            format_currency(
                quotation.other_charges
            )
        ],


        [
            "Discount",
            format_currency(
                quotation.discount
            )
        ],


        [
            "GST",
            f"{quotation.gst_percent}%  "
            f"{format_currency(quotation.gst_amount)}"
        ],


        [
            "GRAND TOTAL",
            format_currency(
                quotation.grand_total
            )
        ]

    ]



    summary_table = Table(

        summary_data,

        colWidths=[180,230]

    )



    summary_table.setStyle(

        TableStyle([


            (
                "GRID",
                (0,0),
                (-1,-1),
                0.5,
                colors.black
            ),


            (
                "BACKGROUND",
                (0,-1),
                (-1,-1),
                colors.lightgrey
            ),


            (
                "FONT",
                (0,-1),
                (-1,-1),
                "Helvetica-Bold"
            )

        ])

    )



    story.append(

        summary_table

    )


    story.append(

        Spacer(1,20)

    )




    # ===============================
    # BANK DETAILS
    # ===============================


    story.append(

        Paragraph(

            "<b>Bank Account Details</b>",

            heading_style

        )

    )



    bank_details = """

    Account Name : ***************<br/>
    Bank Name : ***************<br/>
    Account Number : ***************<br/>
    IFSC Code : ***************<br/>
    UPI ID : ***************

    """



    bank_table = Table(

        [

            [

                Paragraph(

                    bank_details,

                    styles["Normal"]

                )

            ]

        ],

        colWidths=[410]

    )



    bank_table.setStyle(

        TableStyle([


            (
                "BOX",
                (0,0),
                (-1,-1),
                0.5,
                colors.black
            )

        ])

    )



    story.append(

        bank_table

    )



    story.append(

        Spacer(1,15)

    )





    # ===============================
    # TERMS & CONDITIONS
    # ===============================


    story.append(

        Paragraph(

            "<b>Terms & Conditions</b>",

            heading_style

        )

    )



    terms = """

    • 50% advance payment required before work start.<br/>
    • Remaining payment after completion of work.<br/>
    • Material quality will be as discussed with customer.<br/>
    • Any extra work will be charged separately.<br/>
    • Final measurement will be considered at site.

    """



    story.append(

        Paragraph(

            terms,

            styles["Normal"]

        )

    )


    story.append(

        Spacer(1,15)

    )



    story.append(

        Paragraph(

            "<b>Payment Terms:</b> "
            +
            safe(
                quotation.payment_terms
                or
                "50% Advance Payment"
            ),

            styles["Normal"]

        )

    )


    story.append(

        Paragraph(

            "<b>Delivery Time:</b> "
            +
            safe(
                quotation.delivery_time
                or
                "As per schedule"
            ),

            styles["Normal"]

        )

    )


    story.append(

        Spacer(1,20)

    )

        # ===============================
    # CUSTOMER NOTE
    # ===============================


    story.append(

        Paragraph(

            """
            <b>Note:</b><br/>
            Final quotation amount may vary after final site measurement
            and customer requirement discussion.
            """,

            styles["Normal"]

        )

    )


    story.append(

        Spacer(1,30)

    )



    # ===============================
    # SIGNATURE SECTION
    # ===============================


    signature_data=[


        [

            "Customer Signature",

            "For DEEPU FABRICATOR"

        ],


        [

            "\n\n\n",

            "\n\n\n"

        ],


        [

            "Authorized Sign",

            "Authorized Sign"

        ]

    ]



    signature_table = Table(

        signature_data,

        colWidths=[200,200]

    )



    signature_table.setStyle(

        TableStyle([

            (
                "ALIGN",
                (0,0),
                (-1,-1),
                "CENTER"
            )

        ])

    )



    story.append(

        signature_table

    )


    story.append(

        Spacer(1,20)

    )



    # ===============================
    # FOOTER
    # ===============================


    story.append(

        Paragraph(

            """
            Thank you for choosing DEEPU FABRICATOR.<br/>
            Quality Work | Reliable Service | Customer Satisfaction
            """,

            center_style

        )

    )



    # ===============================
    # BUILD PDF
    # ===============================


    doc.build(

        story

    )



    buffer.seek(0)



    return buffer
