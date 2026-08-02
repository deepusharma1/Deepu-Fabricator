from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from datetime import datetime, timezone
import uuid

from app.models.quotation import QuotationModel
from app.schemas.quotation import (
    QuotationCreate,
    QuotationUpdate
)



class QuotationService:



    # =====================================================
    # CREATE QUOTATION
    # =====================================================

    @staticmethod
    def save_quotation(
        db: Session,
        data: QuotationCreate
    ):

        try:


            quotation_no = (

                "DF-"

                + datetime.now().strftime("%Y%m%d")

                + "-"

                + str(uuid.uuid4())[:6].upper()

            )



            items_data = [

                item.model_dump()

                for item in data.items

            ]



            material_total = sum(

                float(item.get("amount",0))

                for item in items_data

            )



            total_area = (

                float(data.width_ft)

                *

                float(data.height_ft)

            )



            estimated_cost = (

                material_total

                + float(data.labour_cost)

                + float(data.installation_cost)

                + float(data.transport_cost)

                + float(data.other_charges)

                - float(data.discount)

            )


            if estimated_cost < 0:

                estimated_cost = 0



            gst_amount = (

                estimated_cost

                *

                float(data.gst_percent)

                /

                100

            )



            grand_total = (

                estimated_cost

                +

                gst_amount

            )




            quotation = QuotationModel(


                quotation_no=quotation_no,


                revision_no=1,



                customer_name=data.customer_name,


                company_name=data.company_name,


                mobile_number=data.mobile_number,


                email=data.email,


                address=data.address,



                lead_source=data.lead_source,



                work_type=data.work_type,


                material_type=data.material_type,



                width_ft=data.width_ft,


                height_ft=data.height_ft,


                total_area_sqft=total_area,



                rate_per_sqft=data.rate_per_sqft,



                estimated_cost=estimated_cost,



                labour_cost=data.labour_cost,


                installation_cost=data.installation_cost,


                transport_cost=data.transport_cost,


                other_charges=data.other_charges,



                discount=data.discount,



                gst_percent=data.gst_percent,


                gst_amount=gst_amount,



                grand_total=grand_total,



                items_json=items_data,



                notes=data.notes,



                payment_terms=data.payment_terms,


                delivery_time=data.delivery_time,



                status="Draft"


            )



            db.add(quotation)

            db.commit()

            db.refresh(quotation)



            return quotation



        except SQLAlchemyError as error:


            db.rollback()


            raise Exception(

                f"Database error: {str(error)}"

            )



        except Exception as error:


            db.rollback()


            raise Exception(

                f"Quotation creation failed: {str(error)}"

            )
            # =====================================================
    # GET ALL QUOTATIONS
    # =====================================================

    @staticmethod
    def get_all_quotations(
        db: Session
    ):


        return (

            db.query(QuotationModel)

            .filter(

                QuotationModel.is_deleted.is_(False)

            )

            .order_by(

                QuotationModel.id.desc()

            )

            .all()

        )





    # =====================================================
    # GET SINGLE QUOTATION BY ID
    # =====================================================

    @staticmethod
    def get_quotation_by_id(

        db: Session,

        quotation_id: int

    ):


        return (

            db.query(QuotationModel)

            .filter(

                QuotationModel.id == quotation_id,

                QuotationModel.is_deleted.is_(False)

            )

            .first()

        )





    # =====================================================
    # UPDATE QUOTATION
    # =====================================================

    @staticmethod
    def update_quotation(

        db: Session,

        quotation_id: int,

        data: QuotationUpdate

    ):


        try:


            quotation = (

                db.query(QuotationModel)

                .filter(

                    QuotationModel.id == quotation_id,

                    QuotationModel.is_deleted.is_(False)

                )

                .first()

            )



            if not quotation:

                return None




            # Locked quotation cannot update

            if quotation.is_locked:

                raise Exception(

                    "Quotation is locked and cannot be updated"

                )





            update_data = data.model_dump(

                exclude_unset=True

            )



            for key, value in update_data.items():


                setattr(

                    quotation,

                    key,

                    value

                )





            quotation.updated_at = datetime.now(

                timezone.utc

            )



            db.commit()

            db.refresh(quotation)



            return quotation





        except SQLAlchemyError as error:


            db.rollback()


            raise Exception(

                f"Quotation update database error: {str(error)}"

            )





    # =====================================================
    # SOFT DELETE QUOTATION
    # =====================================================

    @staticmethod
    def delete_quotation(

        db: Session,

        quotation_id: int

    ):


        try:


            quotation = (

                db.query(QuotationModel)

                .filter(

                    QuotationModel.id == quotation_id

                )

                .first()

            )



            if not quotation:

                return False





            quotation.is_deleted = True



            quotation.updated_at = datetime.now(

                timezone.utc

            )



            db.commit()



            return True





        except SQLAlchemyError as error:


            db.rollback()


            raise Exception(

                f"Quotation delete error: {str(error)}"

            )