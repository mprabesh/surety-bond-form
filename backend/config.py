import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_jwt_secret_key")
    UPLOAD_FOLDER = "uploads/"
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limit to 16MB per file


config = Config()
