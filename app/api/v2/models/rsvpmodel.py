from psycopg2.extras import RealDictCursor
from instance.config import app_config
from app.api.v2.utils.db_connection import connect
import psycopg2
import os
import datetime

environment = os.environ["APP_SETTINGS"]
DATABASE_URL = app_config[environment].DATABASE_URL


class Rsvps():
    """This class holds data for all Rsvp records"""

    def create_rsvp(self,  user_id=None, meetup_id=None, response=None):
        """Model for posting an rsvp"""
        with connect() as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute("INSERT INTO rsvps (user_id,meetup_id,response) VALUES(%s,%s,%s) RETURNING user_id, meetup_id, response",
                               (user_id, meetup_id, response))
                rsvp = cursor.fetchone()
                return rsvp
