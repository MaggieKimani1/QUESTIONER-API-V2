import datetime
from manage import Database
from psycopg2.extras import RealDictCursor
from instance.config import app_config
import psycopg2
import os

db = Database()
environment = os.environ["APP_SETTINGS"]
DATABASE_URL = app_config[environment].DATABASE_URL


class Meetups():
    """This class holds data for all meetups"""

    def __init__(self):
        self.connection = psycopg2.connect(DATABASE_URL)
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def create_meetup(self, location=None, topic=None, happeningOn=None, tags=None):
        """Model for posting a meetup"""
        createdOn = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")

        self.cursor.execute("INSERT INTO meetups (createdOn, location, topic, happeningOn, tags) VALUES(%s,%s,%s,%s,%s)",
                            (createdOn, location, topic, happeningOn, tags))

        self.connection.commit()

        return {"message": "meetup added!"}

    def check_meetup(self, topic):
        '''Get meetup by topic'''
        try:
            self.cursor.execute(
                "SELECT * FROM meetups WHERE topic = %s", (topic,))
            result = self.cursor.fetchone()
            return result
        except:
            pass

    def get_all_meetups(self):
        """Get all meetups"""
        self.cursor.execute("SELECT * FROM meetups")
        result = self.cursor.fetchall()
        return result

    def get_specific_meetup(self, meetup_id):
        """Get meetup by meetup_id"""
        self.cursor.execute(
            "SELECT * FROM meetups WHERE meetup_id = %s", (meetup_id,))
        result = self.cursor.fetchone()
        return result

    def delete_meetup(self, meetup_id):
        """Delete all meetups"""
        self.cursor.execute(
            "DELETE FROM meetups WHERE meetup_id = %s", (meetup_id,))

        self.connection.commit()
