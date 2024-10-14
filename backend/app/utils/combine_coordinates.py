# # app/utils.py

# # Define the coordinates in a dictionary
# from app.assets.Form3positions import Form3_coordinates


import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


from app.assets.Form3positions import Form3_coordinates


def get_combined_form_field_data(form_data):
    print(form_data, "1489278934782374872738467")

    mapping = {
        "ext1": "ext1",
        "onds[policy": "policy",
        "rincipals[address][full": "principal_address_full",
        "onding_companies[full_prin_bus": "bonding_company",
        "onds[obligee": "obligee",
        "bligee[address][full": "obligee_address_full",
        "onds[amount": "amount",
        "onds[project][address][full": "project_address_full",
        "onds[job_description": "job_description",
        "onds[sign_date_day": "sign_date_day",
        "rincipal[seal": "principal_seal",
        "onds[sign_date_month": "sign_date_month",
        "onds[sign_date_year_4_digit": "sign_date_year",
        "itness[signature][2": "witness_signature_2",
        "rincipal[signature][1": "principal_signature_1",
        "itness[Name][2": "witness_name_2",
        "rincipals[authorized_representative": "authorized_representative",
        "omm": "omission",
        "rincipal[title][1": "principal_title_1",
        "itness[signature][1": "witness_signature_1",
        "itness[Name][1": "witness_name_1",
        "if[signature][1": "if_signature_1",
        "gency[attorney": "agency_attorney",
        "riteup[seal": "writeup_seal",
    }
    output = {}

    for key, coordinates in Form3_coordinates.items():
        api_key = mapping.get(key)
        if api_key:
            output[key] = {
                "value": form_data[api_key],
                "x0": coordinates["x0"],
                "y0": coordinates["y0"],
            }

    return output
