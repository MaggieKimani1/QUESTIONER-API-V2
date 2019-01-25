
from psycopg2.extras import RealDictCursor
from instance.config import app_config
from app.api.v2.utils.db_connection import connect
import psycopg2
import os
import datetime

environment = os.environ["APP_SETTINGS"]
DATABASE_URL = app_config[environment].DATABASE_URL


class Questions():
    """This class holds data for all questions"""

    def create_question(self, createdBy=None, meetup=None, title=None, body=None, upvotes=None, downvotes=None):
        """Model for posting a question"""
        createdOn = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        with connect() as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:

                cursor.execute("INSERT INTO questions (createdOn, createdBy, meetup, title, body, upvotes, downvotes) VALUES(%s,%s,%s,%s,%s,%s,%s) RETURNING question_id, meetup, createdOn, createdBy",
                               (createdOn, createdBy, meetup, title, body, upvotes, downvotes))
                question_created = cursor.fetchone()

                return question_created

    def get_all_questions(self, meetup_id):
        """Get all questions"""
        with connect() as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    "SELECT * FROM questions WHERE meetup_id = %s", (meetup_id,))
                result = cursor.fetchall()
                return result

    def get_specific_question(self, question_id):
        """Get specific question"""
        with connect() as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    "SELECT * FROM questions WHERE question_id=%s", (question_id,))
                result = cursor.fetchone()
                print('Hello')
                return result
