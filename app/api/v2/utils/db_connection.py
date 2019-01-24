import os
import psycopg2

from instance.config import app_config

environment = os.environ["APP_SETTINGS"]
DATABASE_URL = app_config[environment].DATABASE_URL


def connect():
    """This method creates a connection to the class
       param:connection
       return:connection
    """
    return psycopg2.connect(DATABASE_URL)
