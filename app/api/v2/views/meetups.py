from flask import Flask, request, jsonify
from flask_restful import Resource
from app.api.v2.models.meetupmodel import Meetups
from flask_expects_json import expects_json
from app.api.v2.utils.json_schema import meetup_schema

meetup = Meetups()


class AllMeetupsApi(Resource):
    """Endpoint for all meetups functionality"""

    @expects_json(meetup_schema)
    def post(self):
        """This endpoint creates a meetup record"""
        data = request.get_json()

        if not data:
            return {"message": "Please provide the required details", "status": 400}, 400

        location = data["location"]
        topic = data["topic"]
        happeningOn = data["happeningOn"]
        tags = data["tags"]

        if not location or location.isspace():
            return {"message": "location must be provided", "status": 400}, 400
        if not topic or topic.isspace():
            return {"message": "topic must be provided", "status": 400}, 400
        if not happeningOn or happeningOn.isspace():
            return {"message": "happeningOn must be provided", "status": 400}, 400
        if not tags:
            return {"message": "tags must be provided", "status": 400}, 400

        if meetup.check_meetup(topic):
            return {"message": "meetup already exists", "status": 400}, 400

        meetup_record = meetup.create_meetup(
            location, topic, happeningOn, tags)
        if meetup_record:
            return {"status": 201, "data": meetup_record, "message": "Meetup posted sucessfully"}, 201
        return {"message": "Meetup failed to post"}, 400

    def get(self):
        """Endpoint for geting all meetup records"""

        meetups = meetup.get_all_meetups()
        if meetups:
            return {"status": 200, "data": meetups, "message": "These are the available meetups"}, 200
        return {"message": "No meetup found", "status": 404}, 404


class SingleMeetupApi(Resource):
    '''Endpoint for single meetup functionality'''

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
