from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import SQLAlchemyError
from app.models.formdetail import FormField
from app import db


class Bonddetails(Resource):
    def get(self):
        try:
            form_fields = FormField.query.all()
            print(form_fields)
            return [form_field.to_dict() for form_field in form_fields], 200

        except SQLAlchemyError as e:
            return {
                "message": "Database error occurred while retrieving form fields."
            }, 500
        except Exception as e:
            return {
                "message": "An unexpected error occurred.",
                "error": str(e),  # Include the specific error message
            }, 500

    def post(self):

        parser = reqparse.RequestParser()

        # Add arguments to the parser
        parser.add_argument("id", required=True, help="ID cannot be blank.")
        parser.add_argument("ext1", required=True, help="ext1 cannot be blank.")
        parser.add_argument("policy", required=True, help="Policy cannot be blank.")
        parser.add_argument(
            "principal_address_full",
            required=True,
            help="Principal address cannot be blank.",
        )
        parser.add_argument(
            "bonding_company", required=True, help="Bonding company cannot be blank."
        )
        parser.add_argument("obligee", required=True, help="Obligee cannot be blank.")
        parser.add_argument(
            "obligee_address_full",
            required=True,
            help="Obligee address cannot be blank.",
        )
        parser.add_argument("amount", required=True, help="Amount cannot be blank.")
        parser.add_argument(
            "project_address_full",
            required=True,
            help="Project address cannot be blank.",
        )
        parser.add_argument(
            "job_description", required=True, help="Job description cannot be blank."
        )
        parser.add_argument(
            "sign_date_day", required=True, help="Sign date day cannot be blank."
        )
        parser.add_argument(
            "principal_seal", required=True, help="Principal seal cannot be blank."
        )
        parser.add_argument(
            "sign_date_month", required=True, help="Sign date month cannot be blank."
        )
        parser.add_argument(
            "sign_date_year", required=True, help="Sign date year cannot be blank."
        )
        parser.add_argument(
            "witness_signature_2",
            required=True,
            help="Witness signature 2 cannot be blank.",
        )
        parser.add_argument(
            "principal_signature_1",
            required=True,
            help="Principal signature 1 cannot be blank.",
        )
        parser.add_argument(
            "witness_name_2", required=True, help="Witness name 2 cannot be blank."
        )
        parser.add_argument(
            "authorized_representative",
            required=True,
            help="Authorized representative cannot be blank.",
        )
        parser.add_argument("omission", required=True, help="Omission cannot be blank.")
        parser.add_argument(
            "principal_title_1", required=True, help="Principal title cannot be blank."
        )
        parser.add_argument(
            "witness_signature_1",
            required=True,
            help="Witness signature 1 cannot be blank.",
        )
        parser.add_argument(
            "witness_name_1", required=True, help="Witness name 1 cannot be blank."
        )
        parser.add_argument(
            "if_signature_1", required=True, help="If signature cannot be blank."
        )
        parser.add_argument(
            "agency_attorney", required=True, help="Agency attorney cannot be blank."
        )
        parser.add_argument(
            "writeup_seal", required=True, help="Writeup seal cannot be blank."
        )

        # Parse the arguments
        args = parser.parse_args()

        # Create a new FormField instance with the provided arguments
        new_form_field = FormField(
            id=args["id"],
            ext1=args["ext1"],
            policy=args["policy"],
            principal_address_full=args["principal_address_full"],
            bonding_company=args["bonding_company"],
            obligee=args["obligee"],
            obligee_address_full=args["obligee_address_full"],
            amount=args["amount"],
            project_address_full=args["project_address_full"],
            job_description=args["job_description"],
            sign_date_day=args["sign_date_day"],
            principal_seal=args["principal_seal"],
            sign_date_month=args["sign_date_month"],
            sign_date_year=args["sign_date_year"],
            witness_signature_2=args["witness_signature_2"],
            principal_signature_1=args["principal_signature_1"],
            witness_name_2=args["witness_name_2"],
            authorized_representative=args["authorized_representative"],
            omission=args["omission"],
            principal_title_1=args["principal_title_1"],
            witness_signature_1=args["witness_signature_1"],
            witness_name_1=args["witness_name_1"],
            if_signature_1=args["if_signature_1"],
            agency_attorney=args["agency_attorney"],
            writeup_seal=args["writeup_seal"],
        )

        # Add the new form field to the session and commit
        db.session.add(new_form_field)
        db.session.commit()

        # Return a success message
        return {"message": "Form field created successfully"}, 201
