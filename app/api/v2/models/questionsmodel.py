
from psycopg2.extras import RealDictCursor
from instance.config import app_config
from app.api.v2.utils.db_connection import connect
import psycopg2
import os
import datetime

# db = Database()
environment = os.environ["APP_SETTINGS"]
DATABASE_URL = app_config[environment].DATABASE_URL


class Questions():
    """This class holds data for all questions"""

    # def __init__(self):
    #     self.connection = psycopg2.connect(DATABASE_URL)
    #     self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def create_question(self, createdBy=None, meetup=None, title=None, body=None, upvotes=None, downvotes=None):
        """Model for posting a question"""
        createdOn = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        with connect() as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:

                cursor.execute("INSERT INTO questions (createdOn, createdBy, meetup, title, body, upvotes, downvotes) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                               (createdOn, createdBy, meetup, title, body, upvotes, downvotes))

                return {"message": "question added!"}

    def get_all_questions(self):
        """Get all questions"""
        with connect() as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute("SELECT * FROM questions")
                result = cursor.fetchall()
                return result

    def get_specific_question(self, question_id):
        """Get specific question"""
        with connect() as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    "SELECT * FROM questions WHERE question_id=%s", (question_id,))
                result = cursor.fetchone()
                return result
