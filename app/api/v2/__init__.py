from flask import Blueprint
from flask_restful import Api
from app.api.v2.views.meetups import MeetupsEndpoints, MeetupEndpoint
from app.api.v2.views.questions import QuestionsEndpoint, QuestionEndpoint
from app.api.v2.views.users import Registration, Login
from app.api.v2.views.rsvps import RSVPEndpoint


"""create variable called api_v1 that defines the blueprint and registers it in the application factory"""
app_v2 = Blueprint('api_v2', __name__, url_prefix='/api/v2')
api_v2 = Api(app_v2, catch_all_404s=True)

api_v2.add_resource(MeetupsEndpoints, '/meetups', '/meetups/upcoming')
api_v2.add_resource(MeetupEndpoint, '/meetups/<int:meetup_id>',
                    '/meetups/<int:meetup_id>/rsvps')
api_v2.add_resource(QuestionsEndpoint, '/meetups/<int:meetup_id>/questions')
api_v2.add_resource(
    QuestionEndpoint, '/meetups/<int:meetup_id>/questions/<int:question_id>')
api_v2.add_resource(Registration, '/auth/signup')
api_v2.add_resource(Login, '/auth/login')
api_v2.add_resource(RSVPEndpoint, '/meetups/<int:meetup_id>/rsvp')
