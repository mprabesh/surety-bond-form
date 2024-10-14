from app import db, create_app  # Make sure to import create_app
from app.models.formdetail import (
    FormField,
)  # Ensure this points to your FormField model


def seed_data():
    # Define your dummy data
    form_fields = [
        {
            "ext1": "Additional Data 1",
            "policy": "12345678",
            "principal_address_full": "456 Elm St, Springfield, USA",
            "bonding_company": "Acme Insurance Co.",
            "obligee": "Jane Smith",
            "obligee_address_full": "789 Maple Ave, Anytown, USA",
            "amount": "$50,000",
            "project_address_full": "1234 Oak St, Metropolis, USA",
            "job_description": "Construction Project",
            "sign_date_day": 15,
            "principal_seal": "Official Seal",
            "sign_date_month": 10,
            "sign_date_year": 2024,
            "witness_signature_2": "Witness Signature 1",
            "principal_signature_1": "Principal Signature 1",
            "witness_name_2": "Witness Name 1",
            "authorized_representative": "Authorized Rep. John Smith",
            "omission": "Company Omission",
            "principal_title_1": "Principal Title",
            "witness_signature_1": "Witness Signature 2",
            "witness_name_1": "Witness Name 2",
            "if_signature_1": "If Signature",
            "agency_attorney": "Agency Attorney Bob Brown",
            "writeup_seal": "Writeup Seal",
        },
        {
            "ext1": "Additional Data 2",
            "policy": "87654321",
            "principal_address_full": "789 Oak St, Gotham, USA",
            "bonding_company": "Wayne Enterprises",
            "obligee": "Clark Kent",
            "obligee_address_full": "123 Main St, Metropolis, USA",
            "amount": "$75,000",
            "project_address_full": "456 Maple St, Smallville, USA",
            "job_description": "Renovation Project",
            "sign_date_day": 12,
            "principal_seal": "Official Seal 2",
            "sign_date_month": 5,
            "sign_date_year": 2023,
            "witness_signature_2": "Witness Signature 3",
            "principal_signature_1": "Principal Signature 3",
            "witness_name_2": "Witness Name 3",
            "authorized_representative": "Authorized Rep. Clark",
            "omission": "Company Omission 2",
            "principal_title_1": "Principal Title 2",
            "witness_signature_1": "Witness Signature 4",
            "witness_name_1": "Witness Name 4",
            "if_signature_1": "If Signature 2",
            "agency_attorney": "Agency Attorney Diana Prince",
            "writeup_seal": "Writeup Seal 2",
        },
        # Add more entries as needed
    ]

    # Add each form field to the session
    for field in form_fields:
        new_form_field = FormField(**field)
        db.session.add(new_form_field)

    # Commit the session to save data to the database
    db.session.commit()


if __name__ == "__main__":
    app = create_app()  # Create an instance of the app
    with app.app_context():
        db.create_all()  # Create tables if they do not exist
        seed_data()  # Seed the data
        print("Database seeded!")
