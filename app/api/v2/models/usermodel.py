import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.api.v2.utils.db_connection import connect
from psycopg2.extras import RealDictCursor
import psycopg2
from instance.config import app_config
import os

environment = os.environ["APP_SETTINGS"]
DATABASE_URL = app_config[environment].DATABASE_URL


class User():
    """User class defining methods related to the class"""

    def __init__(self, firstname=None, lastname=None, password=None, email=None, phoneNumber=None, username=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.phoneNumber = phoneNumber
        self.username = username
        self.registered = datetime.datetime.now()
        self.isAdmin = False

    def create_account(self):
        """ save a new user """

        password = generate_password_hash(self.password)
        with connect() as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:

                cursor.execute("INSERT INTO users (firstname, lastname, password, email, phoneNumber, username, registered, isAdmin) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                               (self.firstname, self.lastname, password, self.email, self.phoneNumber, self.username, self.registered, self.isAdmin))

    def get_user_by_email(self, email):
        """This method gets one user from the system """
        with connect() as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    "SELECT * FROM users WHERE email =%s;", (email,))
                result = cursor.fetchone()
                return result

    def verify_user(self):
        """Verify login details"""
        with connect() as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    "SELECT * FROM users where email =%s", (self.email,))
                result = cursor.fetchone()
                if not result:
                    return "user not found", 404
                valid_login = check_password_hash(
                    result["password"], self.password)
                if not valid_login:
                    return "Wrong password", 404
                return result

    def get_user_by_id(self, id):
        """getting one user by their id"""
        with connect() as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    "SELECT * FROM users WHERE id = %d", (id,))
                result = cursor.fetchone()
                return result
