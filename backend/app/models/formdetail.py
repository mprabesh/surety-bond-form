from app import db  # Import the db object


class FormField(db.Model):
    __tablename__ = "form_fields"  # Specify the table name

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    ext1 = db.Column(db.String, nullable=False)  # Additional Data
    policy = db.Column(db.String, nullable=False)  # Policy Number
    principal_address_full = db.Column(db.String, nullable=False)  # Principal Address
    bonding_company = db.Column(db.String, nullable=False)  # Bonding Company
    obligee = db.Column(db.String, nullable=False)  # Obligee Name
    obligee_address_full = db.Column(db.String, nullable=False)  # Obligee Address
    amount = db.Column(db.String, nullable=False)  # Amount
    project_address_full = db.Column(db.String, nullable=False)  # Project Address
    job_description = db.Column(db.String, nullable=False)  # Job Description
    sign_date_day = db.Column(db.Integer, nullable=False)  # Signing Day
    principal_seal = db.Column(db.String, nullable=False)  # Principal Seal
    sign_date_month = db.Column(db.Integer, nullable=False)  # Signing Month
    sign_date_year = db.Column(db.Integer, nullable=False)  # Signing Year
    witness_signature_2 = db.Column(db.String, nullable=False)  # Witness Signature 2
    principal_signature_1 = db.Column(
        db.String, nullable=False
    )  # Principal Signature 1
    witness_name_2 = db.Column(db.String, nullable=False)  # Witness Name 2
    authorized_representative = db.Column(
        db.String, nullable=False
    )  # Authorized Representative
    omission = db.Column(db.String, nullable=False)  # Omission
    principal_title_1 = db.Column(db.String, nullable=False)  # Principal Title
    witness_signature_1 = db.Column(db.String, nullable=False)  # Witness Signature 1
    witness_name_1 = db.Column(db.String, nullable=False)  # Witness Name 1
    if_signature_1 = db.Column(db.String, nullable=False)  # If Signature
    agency_attorney = db.Column(db.String, nullable=False)  # Agency Attorney
    writeup_seal = db.Column(db.String, nullable=False)  # Writeup Seal

    def __repr__(self):
        return f"<FormField {self.id}: {self.ext1}, {self.policy}>"

    def to_dict(self):
        return {
            "id": self.id,
            "ext1": self.ext1,
            "policy": self.policy,
            "principal_address_full": self.principal_address_full,
            "bonding_company": self.bonding_company,
            "obligee": self.obligee,
            "obligee_address_full": self.obligee_address_full,
            "amount": self.amount,
            "project_address_full": self.project_address_full,
            "job_description": self.job_description,
            "sign_date_day": self.sign_date_day,
            "principal_seal": self.principal_seal,
            "sign_date_month": self.sign_date_month,
            "sign_date_year": self.sign_date_year,
            "witness_signature_2": self.witness_signature_2,
            "principal_signature_1": self.principal_signature_1,
            "witness_name_2": self.witness_name_2,
            "authorized_representative": self.authorized_representative,
            "omission": self.omission,
            "principal_title_1": self.principal_title_1,
            "witness_signature_1": self.witness_signature_1,
            "witness_name_1": self.witness_name_1,
            "if_signature_1": self.if_signature_1,
            "agency_attorney": self.agency_attorney,
            "writeup_seal": self.writeup_seal,
        }
