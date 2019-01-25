from flask import Flask, request, jsonify, json
from flask_restful import Resource
from app.api.v2.models.questionsmodel import Questions
from app.api.v2.models.meetupmodel import Meetups
from flask_expects_json import expects_json
from app.api.v2.utils.json_schema import question_schema
from flask_jwt_extended import get_jwt_identity, jwt_required

meetup = Meetups()
question = Questions()


class QuestionsEndpoint(Resource):
    '''Endpoint for all questions functionality'''

    @expects_json(question_schema)
    # @jwt_required
    def post(self, meetup_id):
        """Endpoint for posting a question for a specific meetup"""
        meetup = Meetups()

        try:
            meetup_id = int(meetup_id)
        except:
            return{"message": "The id has to be an integer"}, 400
        meetup_available = meetup.get_specific_meetup(meetup_id)

        if not meetup_available:
            return {"message": "You cannot post a question to an unavailable meetup", "status": 400}, 400

        data = request.get_json()
        if not data:
            return{"message": "Question body cannot be empty", "status": 400}, 400

        createdBy = data["createdBy"]
        meetup = meetup_id
        title = data["title"]
        body = data["body"]
        upvotes = data["upvotes"]
        downvotes = data["downvotes"]

        if not isinstance(meetup, int):
            return {"message": "Meetup_id must be an integer", "status": 400}, 400
        if not title or title.isspace():
            return {"message": "topic cannot be blank", "status": 400}, 400
        if not body or body.isspace():
            return {"message": "body must be provided", "status": 400}, 400

        new_question = question.create_question(createdBy,
                                                meetup, title, body, upvotes, downvotes)

        return {"data": new_question, "status": 400, "message": "Question posted successfully"}, 201

    def get(self, meetup_id):
        """Endpoint for geting all question records"""

        question1 = question.get_all_questions(meetup_id)
        if question1:
            return {"status": 200, "data": question1, "message": "These are the available meetups"}, 200
        return {"message": "No meetup found", "status": 404}, 404


class QuestionEndpoint(Resource):
    """Class handling all manipulations for a specific question resource"""

    def get(self, meetup_id, question_id):
        """Endpoint for geting one question"""
        meetup = Meetups()

        try:
            meetup_id = int(meetup_id)
        except:
            return{"message": "The id has to be an integer"}, 400
        meetup_available = meetup.get_specific_meetup(meetup_id)

        if not meetup_available:
            return {"message": "You cannot get a question to an unavailable meetup", "status": 400}, 400

        question1 = question.get_specific_question(question_id)
        print(question1)
        if question1:
            return {"status": 200, "data": question1, "message": "This is the available question"}, 200
        else:
            return {"message": "No question found", "status": 404}, 404
