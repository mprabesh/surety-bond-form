from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
import os
from app import db
from app.models.formdetail import FormField

from app.utils.combine_coordinates import get_combined_form_field_data

from app.utils.pdf_write import fill_pdf_with_data
from app.assets.filldata import fields_data


# from app.utils.pdf_write import fill_pdf_with_data


class PdfProcess(Resource):
    # @jwt_required()
    def get(self):
        """List all files in the uploads directory."""
        try:
            uploads_dir = "uploads"
            # List all PDF files in the uploads directory
            files = [f for f in os.listdir(uploads_dir) if f.endswith(".pdf")]
            return files, 200
        except Exception as e:
            return {"message": f"Error retrieving files: {str(e)}"}, 500

    # @jwt_required()
    def post(self):
        try:
            file_name = request.json.get("file_name")
            uploads_dir = "uploads"
            file_path = os.path.join(uploads_dir, file_name)

            parser = reqparse.RequestParser()
            parser.add_argument("id", required=True)
            args = parser.parse_args()

            # Access the id from the parsed arguments
            id_value = args["id"]

            form_fields = db.session.query(FormField).filter_by(id=id_value).all()
            form_data = form_fields[0].to_dict()
            # print(form_data, "form_data")

            if not os.path.isfile(file_path):
                return {"message": "File not found."}, 404
            fill_data = get_combined_form_field_data(form_data)
            print("***********", fill_data, "vals")
            # here i need to combine the co-ordinates and the data to be filled in the pdf
            fill_pdf_with_data(file_path, file_name[:-4] + "_output.pdf", fill_data)
            return {
                "message": f"Processed {file_name} successfully.",
                "val": form_data,
            }, 200
        except KeyError:
            return {"message": "Missing file name."}, 400
        except Exception as e:
            return {
                "message": f"An error occurred while processing the file: {str(e)}"
            }, 500
