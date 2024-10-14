from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from app.models.user import User
from app import db


class UserLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, help="Username cannot be blank.")
        parser.add_argument("password", required=True, help="Password cannot be blank.")
        args = parser.parse_args()

        user = User.query.filter_by(username=args["username"]).first()
        if (
            user and user.password == args["password"]
        ):  # For production, use hashed passwords!
            access_token = create_access_token(identity=user.id)
            return {
                "success": True,
                "token": access_token,
                "username": args["username"],
            }, 200
        return {"message": "Invalid credentials"}, 401
