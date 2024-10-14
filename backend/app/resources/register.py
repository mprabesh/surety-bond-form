from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from app.models.user import User
from app import db


class UserRegistration(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, help="Username cannot be blank.")
        parser.add_argument("password", required=True, help="Password cannot be blank.")
        args = parser.parse_args()

        if User.query.filter_by(username=args["username"]).first():
            return {"message": "User already exists"}, 400

        new_user = User(
            username=args["username"], password=args["password"]
        )  # For production, hash passwords!
        db.session.add(new_user)
        db.session.commit()

        return {"message": "User created successfully"}, 201
