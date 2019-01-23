from flask import Flask, request, jsonify
from flask_restful import Resource
from app.api.v2.models.usermodel import User
from flask_jwt_extended import create_access_token, jwt_required
from flask_expects_json import expects_json
from app.api.v2.utils.json_schema import signup_schema, login_schema


class AllUsersApi(Resource):
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
        email = data["email"]
        phoneNumber = data["phoneNumber"]

        if not firstname or firstname.isspace():
            return {"message": "firstname must be provided", "status": 400}, 400
        if not lastname or lastname.isspace():
            return {"message": "lastname must be provided", "status": 400}, 400
        if not username or username.isspace():
            return {"message": "username must be provided", "status": 400}, 400
        if not password or password.isspace():
            return {"message": "password must be provided", "status": 400}, 400
        if not email or email.isspace():
            return {"message": "email must be provided", "status": 400}, 400
        if not phoneNumber or phoneNumber.isspace():
            return {"message": "tags must be provided", "status": 400}, 400

        user1 = User(firstname, lastname, password,
                     email, phoneNumber, username)
        user1.create_account()
        added_user = {"firstname": firstname, "lastname": lastname,
                      "email": email, "phoneNumber": phoneNumber, "username": username}
        return{"status": 201, "data": added_user, "message": "user created"}, 201


class SingleUserApi(Resource):
    @expects_json(login_schema)
    def post(self):
        """This method posts user data for a login"""

        data = request.get_json()

        if not data:
            return {'message': 'please enter data to login'}
        email = data.get('email')
        password = data.get('password')

        if not email or email.isspace():
            return {"message": "email must be provided", "status": 400}, 400
        if not password or password.isspace():
            return {"message": "password must be provided", "status": 400}, 400
        user = User(email=email, password=password)

        if not user.verify_user():
            return ({"message": "wrong email or password", "status": 401}), 401
        logged_user = user.verify_user()
        token = create_access_token(identity=logged_user["email"])
        return {"message": "{} successfully logged in".format(logged_user['username']), "token": token, "status": 201}, 201
