from flask import Flask, request, jsonify
from flask_restful import Resource
from app.api.v2.models.usermodel import User
from flask_jwt_extended import create_access_token, jwt_required
from flask_expects_json import expects_json
from app.api.v2.utils.json_schema import signup_schema, login_schema
from app.api.v2.utils.validators import Validations
from werkzeug.security import check_password_hash

validator = Validations()


class Registration(Resource):
    '''Endpoint for all users functionality'''
    @expects_json(signup_schema)
    def post(self):
        data = request.get_json()

        if not data:
            return "Please provide the required details", 404

        firstname = data["firstname"]
        lastname = data["lastname"]
        password = data["password"]
        username = data["username"]
        email = data["email"].lower()
        phoneNumber = data["phoneNumber"]

        # user_details = [firstname, lastname, username, phoneNumber]
        # for item in user_details:
        #     if ' ' in item:
        #         return {"Cannot have whitespaces"}

        if not validator.validate_email(email):
            return {"message": "Please enter a valid email"}
        if not validator.validate_password(password):
            return{"message": "Password should be atleast 6characters long, have an uppercase and lowercase letter, a special character and a number"}
        if not firstname or firstname.isspace():
            return {"message": "firstname must be provided", "status": 400}, 400
        if not lastname or lastname.isspace():
            return {"message": "lastname must be provided", "status": 400}, 400
        if not username or username.isspace():
            return {"message": "username must be provided", "status": 400}, 400
        if not phoneNumber or phoneNumber.isspace():
            return {"message": "tags must be provided", "status": 400}, 400

        print(User.get_user_by_email(self, email))
        if User.get_user_by_email(self, email):
            return {"message": "Email already exists"}, 409
        User(firstname, lastname, password, email,
             username, phoneNumber).create_account()
        added_user = {"firstname": firstname, "lastname": lastname,
                      "email": email, "phoneNumber": phoneNumber, "username": username}
        return{"status": 201, "data": added_user, "message": "user created"}, 201


class Login(Resource):
    @expects_json(login_schema)
    def post(self):
        """This method posts user data for a login"""

        data = request.get_json()

        if not data:
            return {'message': 'please enter data to login'}
        email = data["email"]
        password = data["password"]

        if not email or email.isspace():
            return {"message": "email must be provided", "status": 400}, 400
        if not password or password.isspace():
            return {"message": "password must be provided", "status": 400}, 400
        user = User.get_user_by_email(self, email)
        print(user['password'])
        if not user:
            return {"message": "Invalid email", "status": 401}, 401

        if not check_password_hash(user['password'], password):
            return {"message": "Invalid password"}, 401

        token = create_access_token(identity=user["email"])
        return {"message": "{} successfully logged in".format(user["username"]), "token": token, "status": 201}, 201
