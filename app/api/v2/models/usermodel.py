import datetime
from manage import Database
from werkzeug.security import generate_password_hash, check_password_hash

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
        self.connection = psycopg2.connect(DATABASE_URL)
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def create_account(self):
        """ save a new user """

        password = generate_password_hash(self.password)
        self.cursor.execute("INSERT INTO users (firstname, lastname, password, email, phoneNumber, username, registered, isAdmin) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                            (self.firstname, self.lastname, password, self.email, self.phoneNumber, self.username, self.registered, self.isAdmin))
        self.connection.commit()

    def get_user_by_email(self):
        """This method gets one user from the system """

        self.cursor.execute(
            "SELECT * FROM users where email =%s", (self.email,))
        result = self.cursor.fetchone()
        return result

    def verify_user(self):
        """Verify login details"""
        self.cursor.execute(
            "SELECT password FROM users where email =%s", (self.email,))
        result = self.cursor.fetchone()
        if not result:
            return "user not found"
        valid_login = check_password_hash(result["password"], self.password)
        return valid_login
