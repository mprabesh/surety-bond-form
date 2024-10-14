import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span

# Load a pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

# Initialize the Matcher with the shared vocabulary
matcher = Matcher(nlp.vocab)

# Define custom patterns for bond forms
patterns = [
    {
        "label": "BOND NO",
        "pattern": [{"LOWER": "bond"}, {"LOWER": "number"}, {"IS_DIGIT": True}],
    },
    {
        "label": "ISSUE_DATE",
        "pattern": [{"LOWER": "issue"}, {"LOWER": "date"}, {"IS_DIGIT": True}],
    },
    {
        "label": "MATURITY_DATE",
        "pattern": [{"LOWER": "maturity"}, {"LOWER": "date"}, {"IS_DIGIT": True}],
    },
    {
        "label": "BOND_AMOUNT",
        "pattern": [{"LOWER": "amount"}, {"IS_CURRENCY": True}, {"IS_DIGIT": True}],
    },
]

# Add patterns to the matcher
for pattern in patterns:
    matcher.add(pattern["label"], [pattern["pattern"]])


def extract_bond_fields(text):
    doc = nlp(text)
    matches = matcher(doc)
    extracted_fields = {}

    for match_id, start, end in matches:
        span = doc[start:end]
        label = nlp.vocab.strings[match_id]
        extracted_fields[label] = span.text

    return extracted_fields


# Example usage
text = """
BOND NO.
PREMIUM:

Subdivision Performance Bond
Site Improvements

KNOW ALL MEN BY THESE PRESENTS:

That we, , as Principal, and Great Midwest
Insurance Company, a corporation organized and doing business under and by the virtue of the
laws of the state of Texas and duly licensed to conduct a general surety business in the state of

, as Surety, are held and firmly bound unto
, as Obligee, in the sum of

($ ) dollars, for which payment, well and truly to be made, we bind
ourselves, our heirs, executors and successors, jointly and severally firmly by these presents.

WHEREAS, the above named Principal entered into an agreement or agreements with said Obligee
to:

NOW THEREFORE, the condition of this obligation is such that if the above Principal shall well
and truly perform said agreement or agreements during the original term thereof or of any
extension of said term that may be granted by the Obligee with or without notice to the Surety, this
obligation shall be void, otherwise it shall remain in full force and effect.

IN WITNESS WHEREOF, the seal and signature of said Principal is hereto affixed and the
corporate seal and the name of the said Surety is hereto affixed and attested by its duly authorized
Attorney-in-Fact this day of ;

Principal Great Midwest Insurance Company

Signature of Attorney-in-Fact

Signature of Authorized Officer Print Name

Print Name & Title
[SEAL]
"""
# extracted_fields = extract_bond_fields(text)
# print(extracted_fields)
# for field, value in extracted_fields.items():
#     print("Hello WOrld")
#     print(f"{field}: {value}")
