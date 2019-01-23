from flask import Flask, request, jsonify, json
from flask_restful import Resource
from app.api.v2.models.questionsmodel import Questions
from app.api.v2.models.meetupmodel import Meetups
from flask_expects_json import expects_json
from app.api.v2.utils.json_schema import question_schema

meetup = Meetups()
question = Questions()


class AllQuestionsApi(Resource):
    '''Endpoint for all questions functionality'''
    @expects_json(question_schema)
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

        user_id = data["user_id"]
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

        new_question = question.create_question(user_id,
                                                meetup, title, body, upvotes, downvotes)

        return {"data": new_question, "status": 400, "message": "Question posted successfully"}, 201

    def get(self, meetup_id):
        """Endpoint for geting all question records"""
        meetup = Meetups()

        try:
            meetup_id = int(meetup_id)
        except:
            return{"message": "The id has to be an integer"}, 400
        meetup_available = meetup.get_specific_meetup(meetup_id)

        if not meetup_available:
            return {"message": "You cannot post a question to an unavailable meetup", "status": 400}, 400

        questions = question.get_all_questions()
        if questions:
            return {"status": 200, "data": questions, "message": "These are the available questions"}, 200
        return {"message": "No meetup found", "status": 404}, 404
