from flask import Flask,Blueprint
from flask_restful import Api


from instance.config import app_config
from manage import Database


my_db = Database()
def create_app(config_name):
	app = Flask(__name__)

	app.config.from_object(app_config[config_name])

	'''Import and register the blueprint from the factory'''
	from app.api.v2 import app_v2
	app.register_blueprint(app_v2)

		
	my_db.createTables()
	return app
