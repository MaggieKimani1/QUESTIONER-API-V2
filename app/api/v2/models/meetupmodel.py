import datetime
from app.api.v2.utils.db_connection import connect
from psycopg2.extras import RealDictCursor
from instance.config import app_config
# from manage import Database
import psycopg2
import os


# db = Database()
environment = os.environ["APP_SETTINGS"]
DATABASE_URL = app_config[environment].DATABASE_URL


class Meetups():
    """This class holds data for all meetups"""

    def create_meetup(self, location=None, topic=None, happeningOn=None):
        """Model for posting a meetup"""
        createdOn = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        with connect() as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:

                result = cursor.execute("INSERT INTO meetups (createdOn, location, topic, happeningOn) VALUES(%s,%s,%s,%s)",
                                        (createdOn, location, topic, happeningOn))

                return cursor.fetchone(result)

    def check_meetup(self, topic):
        '''Get meetup by topic'''
        try:
            with connect() as connection:
                with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                    cursor.execute(
                        "SELECT * FROM meetups WHERE topic = %s", (topic,))
                    result = cursor.fetchone()
                    return result
        except:
            pass

    def get_all_meetups(self):
        """Get all meetups"""
        with connect() as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute("SELECT * FROM meetups")
                result = cursor.fetchall()
                return result

    def get_specific_meetup(self, meetup_id):
        """Get meetup by meetup_id"""
        with connect() as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    "SELECT * FROM meetups WHERE meetup_id = %s", (meetup_id,))
                result = cursor.fetchone()
                return result

    def delete_meetup(self, meetup_id):
        """Delete all meetups"""
        with connect() as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    "DELETE FROM meetups WHERE meetup_id = %s", (meetup_id,))
