from manage import Database
from psycopg2.extras import RealDictCursor
from instance.config import app_config
import psycopg2
import os
import datetime

db = Database()
environment = os.environ["APP_SETTINGS"]
DATABASE_URL = app_config[environment].DATABASE_URL


class Questions():
    """This class holds data for all questions"""

    def __init__(self):
        self.connection = psycopg2.connect(DATABASE_URL)
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def create_question(self, createdBy=None, meetup=None, title=None, body=None, upvotes=None, downvotes=None):
        """Model for posting a meetup"""
        createdOn = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")

        self.cursor.execute("INSERT INTO questions (createdOn, createdBy, meetup, title, body, upvotes, downvotes) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                            (createdOn, createdBy, meetup, title, body, upvotes, downvotes))

        self.connection.commit()

        return {"message": "question added!"}

    def get_all_questions(self):
        """Get all meetups"""
        self.cursor.execute("SELECT * FROM questions")
        result = self.cursor.fetchall()
        return result
