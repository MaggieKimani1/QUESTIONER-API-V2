from flask import Flask, request, jsonify
from flask_restful import Resource
from app.api.v2.models.meetupmodel import Meetups
from flask_expects_json import expects_json
from app.api.v2.utils.json_schema import meetup_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

meetup = Meetups()


class MeetupsEndpoints(Resource):
    """Endpoint for all meetups functionality"""

    @expects_json(meetup_schema)
    @jwt_required
    def post(self):
        """This endpoint creates a meetup record"""

        # current_user = get_jwt_identity()
        # if current_user == "myadmin@gmail.com":

        data = request.get_json()

        if not data:
            return {"message": "Please provide the required details", "status": 400}, 400

        location = data["location"]
        topic = data["topic"]
        happeningOn = data["happeningOn"]

        if not location or location.isspace():
            return {"message": "location must be provided", "status": 400}, 400
        if not topic or topic.isspace():
            return {"message": "topic must be provided", "status": 400}, 400
        if not happeningOn or happeningOn.isspace():
            return {"message": "happeningOn must be provided", "status": 400}, 400

        if meetup.check_meetup(topic):
            return {"message": "meetup already exists", "status": 400}, 400

        meetup_record = meetup.create_meetup(location, topic, happeningOn)

        if meetup_record:
            return {"status": 201, "data": meetup_record, "message": "Meetup posted sucessfully"}, 201
        return {"message": "Meetup failed to post"}, 400
        # return {"message": "This service is only available for the admin"}, 400

    def get(self):
        """Endpoint for geting all meetup records"""

        meetups = meetup.get_all_meetups()
        if meetups:
            return {"status": 200, "data": meetups, "message": "These are the available meetups"}, 200
        return {"message": "No meetup found", "status": 404}, 404


class MeetupEndpoint(Resource):
    '''Endpoint for single meetup functionality'''
    @jwt_required
    def get(self, meetup_id):
        '''Fetching a single meetup'''
        try:
            meetup_id = int(meetup_id)
        except:
            return{"message": "The meetup_id has to be an integer"}, 400

        meetup_available = meetup.get_specific_meetup(meetup_id)

        if meetup_available:
            return {"status": 200, "data": meetup_available, "message": "meetup retrieved"}, 200
        return {"message": "That meetup_id does not exist", "status": 404}, 404

    @jwt_required
    def delete(self, meetup_id):
        """Deleting a product"""
        meetup1 = meetup.get_specific_meetup(meetup_id)
        if meetup1:
            meetup.delete_meetup(meetup_id)
            return {"message": "Meetup deleted successfully"}
        return {"message": "The meetup you're trying to delete isn't available"}, 400
