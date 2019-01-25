from flask import Flask, request, jsonify, json
import datetime
from flask_restful import Resource
from app.api.v2.models.questionsmodel import Questions
from app.api.v2.models.meetupmodel import Meetups
from app.api.v2.models.commentsmodel import Comments
from flask_expects_json import expects_json
from app.api.v2.utils.json_schema import question_schema
from flask_jwt_extended import get_jwt_identity, jwt_required

meetup = Meetups()
question = Questions()
comment = Comments()


class CommentsEndpoint(Resource):
    '''Endpoint for all questions functionality'''

    # @expects_json(question_schema)
    # @jwt_required
    def post(self, meetup_id, question_id):
        """Endpoint for posting a comment for a specific question"""
        meetup = Meetups()

        try:
            meetup_id = int(meetup_id)
        except:
            return{"message": "The id has to be an integer"}, 400
        meetup_available = meetup.get_specific_meetup(meetup_id)

        if not meetup_available:
            return {"message": "You cannot post a question to an unavailable meetup", "status": 400}, 400

        question1 = question.get_specific_question(question_id)
        if question1:

            data = request.get_json()
            if not data:
                return{"message": "Comment body cannot be empty", "status": 400}, 400

            question_id = question_id
            user_id = data["user_id"]
            body = data["body"]

            if not isinstance(question_id, int):
                return {"message": "question_id must be an integer", "status": 400}, 400
            if not isinstance(user_id, int):
                return {"message": "user_id must be an integer", "status": 400}, 400

            if not body or body.isspace():
                return {"message": "body must be provided", "status": 400}, 400

            new_comment = comment.create_comment(
                user_id, question_id)

            return {"data": new_comment, "status": 400, "message": "comment posted successfully"}, 201
