from flask import Blueprint
from flask_restful import Api
from app.api.v2.views.meetups import AllMeetupsApi, SingleMeetupApi
from app.api.v2.views.questions import AllQuestionsApi
from app.api.v2.views.users import AllUsersApi, SingleUserApi


"""create variable called api_v1 that defines the blueprint and registers it in the application factory"""
app_v2 = Blueprint('api_v2', __name__, url_prefix='/api/v2')
api_v2 = Api(app_v2, catch_all_404s=True)

api_v2.add_resource(AllMeetupsApi, '/meetups', '/meetups/upcoming')
api_v2.add_resource(SingleMeetupApi, '/meetups/<meetup_id>',
                    '/meetups/<id>/rsvps')
api_v2.add_resource(AllQuestionsApi, '/meetups/<meetup_id>/questions')
# api_v1.add_resource(SingleQuestion, '/questions/<question_id>')
api_v2.add_resource(AllUsersApi, '/auth')
api_v2.add_resource(SingleUserApi, '/auth/login')
