
from psycopg2.extras import RealDictCursor
from instance.config import app_config
from app.api.v2.utils.db_connection import connect
import psycopg2
import os
import datetime

environment = os.environ["APP_SETTINGS"]
DATABASE_URL = app_config[environment].DATABASE_URL


class Comments():
    """This class holds data for all comments"""

    def create_comment(self, user_id=None, question_id=None):
        """Model for posting a comment"""
        createdOn = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        with connect() as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:

                cursor.execute("INSERT INTO comments (user_id, question_id, createdOn) VALUES(%s,%s,%s) RETURNING user_id, question_id, createdOn",
                               (user_id, question_id, createdOn))
                comment_created = cursor.fetchone()

                return comment_created
