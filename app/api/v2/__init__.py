from flask import Blueprint
from flask_restful import Api
# from app.api.v1.views.meetups import AllMeetupsApi, SingleMeetupApi
# from app.api.v1.views.questions import AllQuestionsApi, SingleQuestion
# from app.api.v1.views.users import AllUsersApi


"""create variable called api_v1 that defines the blueprint and registers it in the application factory"""
app_v2 = Blueprint('api_v2', __name__, url_prefix='/api/v2')
api_v2 = Api(app_v2, catch_all_404s=True)

# api_v1.add_resource(AllMeetupsApi, '/meetups', '/meetups/upcoming')
# api_v1.add_resource(SingleMeetupApi, '/meetups/<id>',
#                     '/meetups/<id>/rsvps')
# api_v1.add_resource(AllQuestionsApi, '/meetups/<id>/questions')
# api_v1.add_resource(SingleQuestion, '/questions/<question_id>')
# api_v1.add_resource(AllUsersApi, '/auth')