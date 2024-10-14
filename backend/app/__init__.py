from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_cors import CORS


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    CORS(app)

    app.config.from_object(config)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///your_database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize JWT
    jwt = JWTManager(app)

    # Initialize API
    api = Api(app)

    db.init_app(app)

    # Import resources and add routes
    from app.resources.pdf_upload import PdfUpload
    from app.models.user import User  # Import User model
    from app.resources.login import UserLogin
    from app.resources.register import UserRegistration
    from app.resources.fillpdf import PdfProcess
    from app.resources.information import Bonddetails

    api.add_resource(PdfUpload, "/api/upload")
    api.add_resource(UserLogin, "/api/login")
    api.add_resource(UserRegistration, "/api/register")
    api.add_resource(PdfProcess, "/api/process")
    api.add_resource(Bonddetails, "/api/bondinfo")

    return app
