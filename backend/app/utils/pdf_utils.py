import pytesseract
from pdf2image import convert_from_path


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

ALLOWED_EXTENSIONS = {"pdf"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def extract_text_from_pdf(file_path):
    # Convert PDF pages to images
    images = convert_from_path(
        file_path, poppler_path=r"C:\Program Files\poppler-24.07.0\Library\bin"
    )

    # Initialize a variable to hold all extracted text
    text = ""

    # Loop through each page image and extract text using Tesseract OCR
    for img in images:
        text += pytesseract.image_to_string(img)

    return text


### identifying the form


def identify_form(pdf_docs):
    # Open the PDF file
    # pdf_document = fitz.open("input.pdf")
    # Select the first page of the PDF
    page = pdf_docs[0]

    # Extract the interactive form fields from the page
    form_fields = page.get_form_fields()

    # Print the form fields
    for field in form_fields:
        print(field)

    # Close the PDF document
    pdf_docs.close()


#### writing on the pdf documents

import fitz  # PyMuPDF
import os


def write_text_over_pdf(input_pdf_path, output_pdf_path, text, position, page_number=0):
    # Open the PDF file
    pdf_document = fitz.open(input_pdf_path)

    # Select the page to write on
    page = pdf_document[page_number]

    # Define the text properties
    text_position = position  # (x, y) coordinates
    text_size = 12  # Font size
    text_color = (0, 0, 0)  # RGB color (black)

    # Add text to the page
    page.insert_text(text_position, text, fontsize=text_size, color=text_color)

    # Save the modified PDF to a new file
    pdf_document.save(output_pdf_path)

    # Close the PDF document
    pdf_document.close()


# # Example usage
# input_pdf_path = "input.pdf"
# output_pdf_path = "output.pdf"
# text = "This is a sample text."
# position = (300, 100)  # (x, y) coordinates on the page

# write_text_over_pdf(input_pdf_path, output_pdf_path, text, position)


# if os.path.exists(input_pdf_path):
#     print("File exists!")
# else:
#     print("File does not exist.")


# import fitz  # PyMuPDF

# # Open the PDF
# pdf_document = fitz.open("input.pdf")

# # Get the first page (or loop through multiple pages)
# for page_num in range(len(pdf_document)):
#     page = pdf_document.load_page(page_num)
#     # Get form fields for the page
#     for field in page.widgets():
#         print(f"{field.field_name}")

# import PyPDF2

# # Open the PDF and inspect the fields
# with open("input.pdf", "rb") as input_pdf_file:
#     pdf_reader = PyPDF2.PdfReader(input_pdf_file)
#     fields = pdf_reader.get_fields()
#     for field_name in fields:
#         print(f"Field name: {field_name}")


# import PyPDF2

# # Open the PDF and inspect the fields
# input_pdf_path = "input.pdf"
# with open(input_pdf_path, "rb") as input_pdf_file:
#     pdf_reader = PyPDF2.PdfReader(input_pdf_file)
#     fields = pdf_reader.get_fields()
#     if fields:
#         print("Fillable fields found:")
#         for field_name in fields:
#             print(f"Field name: {field_name}")
#     else:
#         print("No fillable fields found.")


# import pdfrw


# def get_field_coordinates(input_pdf_path):
#     # Read the PDF
#     pdf = pdfrw.PdfReader(input_pdf_path)

#     # Initialize a list to store field information
#     field_info = []

#     # Loop through the fields in the first page
#     for page in pdf.pages:
#         if "/Annots" in page:
#             for annotation in page["/Annots"]:
#                 if annotation["/Subtype"] == "/Widget":
#                     field_name = annotation.get("/T")
#                     rect = annotation.get("/Rect")

#                     if field_name and rect:
#                         # rect contains [x0, y0, x1, y1]
#                         field_info.append(
#                             {
#                                 "name": field_name,
#                                 "coordinates": {
#                                     "x0": rect[0],
#                                     "y0": rect[1],
#                                     "x1": rect[2],
#                                     "y1": rect[3],
#                                 },
#                             }
#                         )

#     return field_info


# input_pdf_path = "input.pdf"  # Change this to your actual PDF file path

# # Get the coordinates of the fields
# coordinates = get_field_coordinates(input_pdf_path)

# # Print the field names and their coordinates
# for field in coordinates:
#     print(f"Field Name: {field['name']}, Coordinates: {field['coordinates']}")

import PyPDF2


def extract_form_field_coordinates(pdf_path):
    # Open the PDF file
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        # Loop through all pages and extract form fields
        for page_number in range(len(reader.pages)):
            page = reader.pages[page_number]

            # Check if the page has any annotations
            if "/Annots" in page:
                annotations = page["/Annots"]
                for annotation in annotations:
                    # Dereference the annotation
                    annotation_obj = annotation.get_object()

                    # Check if the annotation is a widget
                    if annotation_obj["/Subtype"] == "/Widget":
                        # Get field name
                        field_name = annotation_obj.get("/T")
                        if field_name:
                            # Convert to string and remove any surrounding parentheses
                            field_name = (
                                field_name.decode("utf-8")
                                if isinstance(field_name, bytes)
                                else field_name
                            )
                            field_name = field_name.strip()[
                                1:-1
                            ]  # Remove parentheses if present

                            # Get coordinates
                            rect = annotation_obj.get("/Rect")
                            if rect:
                                x0, y0, x1, y1 = rect
                                coordinates = {
                                    "Field Name": field_name,
                                    "Coordinates": {
                                        "x0": x0,
                                        "y0": y0,
                                        "x1": x1,
                                        "y1": y1,
                                    },
                                }
                                print(coordinates)


# Example usage
# pdf_path = "input.pdf"  # Change this to your actual PDF file path
# extract_form_field_coordinates(pdf_path)
