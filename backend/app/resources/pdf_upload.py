from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
import os
from werkzeug.utils import secure_filename
from app.utils.pdf_utils import (
    allowed_file,
    extract_text_from_pdf,
    identify_form,
)
from app.utils.extract_form_type import identify_form


class PdfUpload(Resource):
    # @jwt_required()
    def post(self):
        try:
            if "file" not in request.files:
                return {"message": "No file part"}, 400

            file = request.files["file"]

            if file.filename == "":
                return {"message": "No selected file"}, 400

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filename = filename.replace(" ", "_")  # Replace spaces with underscores
                filename = "".join(
                    c for c in filename if c.isalnum() or c in ("_", ".")
                )  # Remove unwanted characters
                try:
                    file.save(os.path.join("uploads", filename))
                    text = extract_text_from_pdf(os.path.join("uploads", filename))
                    identify_form(text)

                    return {
                        "status": "success",
                        "message": f"{filename} uploaded successfully",
                        "extracted-text": f"{text}",
                    }, 200
                except OSError as e:
                    return {"message": f"File saving error: {str(e)}"}, 500
            else:
                return {"message": "Invalid file type"}, 400
        except KeyError as e:
            return {"message": f"Missing file part: {str(e)}"}, 400
        except Exception as e:
            return {"message": f"An unexpected error occurred: {str(e)}"}, 500
