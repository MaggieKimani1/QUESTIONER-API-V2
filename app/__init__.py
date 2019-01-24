from flask import Flask, Blueprint
from flask_restful import Api
from instance.config import app_config
from manage import Database
from flask_jwt_extended import JWTManager


def create_app(config_name='development'):
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    app.config.from_object(app_config[config_name])
    app.config['JWT_SECRET_KEY'] = 'secrbjvbbnbcgbhxfbmet'
    JWTManager(app)
    my_db = Database(config_name)
    '''Import and register the blueprint from the factory'''
    from app.api.v2 import app_v2
    app.register_blueprint(app_v2)

    my_db.createTables()
    # my_db.createAdmin()

    return app
