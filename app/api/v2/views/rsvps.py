from flask import Flask, request, jsonify, json
from flask_restful import Resource
from app.api.v2.models.meetupmodel import Meetups
from app.api.v2.models.rsvpmodel import Rsvps
from flask_expects_json import expects_json
from app.api.v2.utils.json_schema import rsvp_schema
from flask_jwt_extended import get_jwt_identity, jwt_required

rsvp = Rsvps()
meetup = Meetups()


class RSVPEndpoint(Resource):
    '''Endpoint for all questions functionality'''

    @expects_json(rsvp_schema)
    # @jwt_required
    def post(self, meetup_id):
        '''Post an RSVP'''
        try:
            meetup_id = int(meetup_id)
        except:
            return{"message": "The id has to be an integer"}, 400
        meetup_available = Meetups().get_specific_meetup(meetup_id)
        if not meetup_available:
            return {"message": "You cannot RSVP an unavailable meetup"}, 400

        data = request.get_json()
        if not data:
            {"message": "Please submit your RSVP", "status": 400}, 400
        user_id = data['user_id']
        meetup_id = meetup_id
        response = data['response']

        if (response == "yes" or response == "no" or response == "maybe"):
            new_rsvp = rsvp.create_rsvp(user_id, meetup_id, response)
            return {"status": 201, "data": new_rsvp, "message": "RSVP saved for this meetup"}, 201
        else:
            return {"message": "response should be a yes, no or maybe", "status": 400}, 400
