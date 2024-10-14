import re


def identify_form(text):
    # Define regex patterns for different form types
    form_patterns = {
        "FormType1": re.compile(r"[Ee][Jj][Dd][Cc]"),
        "FormType2": re.compile(r"(?i)Great Midwest Insurance Company"),
        "FormType3": re.compile(r"(?i)American Institute of Architects"),
    }

    # Identify the form type
    form_type = "Unknown"
    for form_name, pattern in form_patterns.items():
        if pattern.search(text):
            form_type = form_name
            break
    print(form_type)
    return form_type
