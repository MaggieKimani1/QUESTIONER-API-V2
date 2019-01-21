from flask import Flask, request, jsonify
from flask_restful import Resource
from app.api.v2.models.usermodel import User
from flask_jwt_extended import create_access_token, jwt_required


class AllUsersApi(Resource):
    '''Endpoint for all users functionality'''

    def post(self):
        data = request.get_json()

        if not data:
            return "Data must be in JSON format", 404

        firstname = data["firstname"]
        lastname = data["lastname"]
        password = data["password"]
        confirm_password = data["confirm_password"]
        email = data["email"]
        phoneNumber = data["phoneNumber"]
        username = data["username"]

        if password != confirm_password:
            return {"message": "Passwords do not match"}

        user1 = User(firstname, lastname, password,
                     email, phoneNumber, username)

        if user1:
            user = user1.create_account()
            return{"status": 201, "data": user, "message": "user created"}, 201
        else:
            return 'Could not create an account', 400


class SingleUserApi(Resource):
    def post(self):
        """This method posts user data for a login"""

        data = request.get_json()

        if not data:
            return {'message': 'please enter data to login'}
        email = data.get('email')
        password = data.get('password')
        user = User(email=email, password=password)

        if not user.verify_user():
            return ({"message": "wrong email or password", "status": 401}), 401
        logged_user = user.verify_user()
        token = create_access_token(identity=logged_user["email"])

        return {"message": "{} successfully logged in".format(logged_user['username']), "token": token, "status": 201}, 201
