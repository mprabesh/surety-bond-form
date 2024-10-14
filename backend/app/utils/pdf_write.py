import fitz  # PyMuPDF
import os


def fill_pdf_with_data(input_pdf_path, output_filename, fields_data):
    # Open the PDF file
    pdf_document = fitz.open(input_pdf_path)

    DOWNLOAD_DIRECTORY = "downloads"

    # Create the downloads directory if it doesn't exist
    if not os.path.exists(DOWNLOAD_DIRECTORY):
        os.makedirs(DOWNLOAD_DIRECTORY)
    # Create the full path for the output PDF
    output_pdf_path = os.path.join(DOWNLOAD_DIRECTORY, output_filename)

    # Get the height of the first page (assuming all pages have the same height)
    page_height = pdf_document[0].rect.height

    # Get the first page of the document
    first_page = pdf_document[0]

    # Loop through each field and its coordinates
    for field_name, coordinates in fields_data.items():
        # Get the coordinates
        x0 = coordinates["x0"]
        y0 = coordinates["y0"]
        # Invert y-coordinate
        y0_inverted = page_height - y0
        value = str(
            coordinates.get("value", "")
        )  # Get the value to insert and ensure it's a string

        # Define the text properties
        text_size = 12  # Font size
        text_color = (0, 0, 0)  # RGB color (black)

        # Add text to the first page at the specified coordinates
        first_page.insert_text(
            (x0, y0_inverted), value, fontsize=text_size, color=text_color
        )

    # Save the modified PDF to a new file

    pdf_document.save(output_pdf_path)

    # Close the PDF document
    pdf_document.close()


# # Example usage
# input_pdf_path = "input.pdf"  # Change this to your actual PDF file path
# output_pdf_path = "filled_form.pdf"  # Output PDF path

# # Define the fields with their coordinates and values to fill
# fields_data = {
#     "ext1": {"x0": 79.3323, "y0": 745.109, "value": "John Doe"},
#     "onds[policy": {"x0": 447.609, "y0": 707.143, "value": "12345678"},
#     "rincipals[address][full": {
#         "x0": 43.5139,
#         "y0": 628.65,
#         "value": "456 Elm St, Springfield, USA",
#     },
#     "onding_companies[full_prin_bus": {
#         "x0": 321.534,
#         "y0": 629.85,
#         "value": "Acme Insurance Co.",
#     },
#     "onds[obligee": {"x0": 43.8341, "y0": 585.807, "value": "Jane Smith"},
#     "bligee[address][full": {
#         "x0": 43.5139,
#         "y0": 550.837,
#         "value": "789 Maple Ave, Anytown, USA",
#     },
#     "onds[amount": {"x0": 125.694, "y0": 532.676, "value": "$50,000"},
#     "onds[project][address][full": {
#         "x0": 262.902,
#         "y0": 454.594,
#         "value": "1234 Oak St, Metropolis, USA",
#     },
#     "onds[job_description": {
#         "x0": 43.8341,
#         "y0": 454.594,
#         "value": "Construction Project",
#     },
#     "onds[sign_date_day": {"x0": 143.276, "y0": 188.313, "value": "15"},
#     "rincipal[seal": {"x0": 467.6, "y0": 161.372, "value": "Official Seal"},
#     "onds[sign_date_month": {"x0": 223.908, "y0": 188.313, "value": "10"},
#     "onds[sign_date_year_4_digit": {"x0": 367.188, "y0": 188.313, "value": "2024"},
#     "itness[signature][2": {
#         "x0": 95.6416,
#         "y0": 155.128,
#         "value": "Witness Signature 1",
#     },
#     "rincipal[signature][1": {
#         "x0": 348.091,
#         "y0": 146.778,
#         "value": "Principal Signature 1",
#     },
#     "itness[Name][2": {"x0": 87.8832, "y0": 142.753, "value": "Witness Name 1"},
#     "rincipals[authorized_representative": {
#         "x0": 347.846,
#         "y0": 133.62,
#         "value": "Authorized Rep. John Smith",
#     },
#     "omm": {"x0": 455.322, "y0": 133.62, "value": "Company Omission"},
#     "rincipal[title][1": {"x0": 462.195, "y0": 133.62, "value": "Principal Title"},
#     "itness[signature][1": {
#         "x0": 94.6407,
#         "y0": 101.34,
#         "value": "Witness Signature 2",
#     },
#     "itness[Name][1": {"x0": 85.9952, "y0": 88.1757, "value": "Witness Name 2"},
#     "if[signature][1": {"x0": 355.015, "y0": 88.7949, "value": "If Signature"},
#     "gency[attorney": {
#         "x0": 339.157,
#         "y0": 73.1899,
#         "value": "Agency Attorney Bob Brown",
#     },
#     "riteup[seal": {"x0": 467.601, "y0": 59.2499, "value": "Writeup Seal"},
#     "ext1": {"x0": 473.721, "y0": 73.0359, "value": "Additional Data"},
# }

# # Fill the PDF
# # fill_pdf_with_data(input_pdf_path, output_pdf_path, fields_data)
