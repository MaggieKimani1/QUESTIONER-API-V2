import os
import psycopg2
import datetime
from instance.config import app_config
from werkzeug.security import generate_password_hash
from app.api.v2.utils.db_connection import connect
from psycopg2.extras import RealDictCursor
from app.api.v2.models.usermodel import User

user1 = User()

environment = os.environ["APP_SETTINGS"]
DATABASE_URL = app_config[environment].DATABASE_URL


class Database(object):
    """This Class has the setup for connecting to the database and creation of tables """

    def __init__(self, config_name):
        self.conn = psycopg2.connect(app_config[config_name].DATABASE_URL)
        self.cursor = self.conn.cursor()

    def createTables(self):
        """This method creates all tables if they dont exist
                                        param1:connection
                                        param2:queries
                                        param3:cursor
        """
        user_query = """CREATE TABLE if not EXISTS users(
		id Serial PRIMARY KEY NOT NULL,
		firstname varchar(40) NOT NULL,
		lastname varchar(40) NOT NULL,
		email varchar(100) UNIQUE NOT NULL,
		password varchar(500) NOT NULL,
		phoneNumber varchar(20) NOT NULL,
		username varchar(100)  NOT NULL,
		registered date NOT NULL,
		isAdmin boolean NOT NULL
		)"""

        question_query = """CREATE TABLE if not EXISTS questions(
		question_id Serial PRIMARY KEY NOT NULL,
		createdOn varchar NOT NULL,
		createdBy int REFERENCES users(id) on DELETE CASCADE,
		meetup varchar(100)  NOT NULL,
		title varchar(50) NOT NULL,
		body varchar(250) NOT NULL,
		upvotes int NOT NULL,
		downvotes int NOT NULL
		)"""

        meetup_query = """CREATE TABLE if not EXISTS meetups(
		meetup_id Serial PRIMARY KEY NOT NULL,
		createdOn varchar NOT NULL,
		location varchar(50) NOT NULL,
		topic varchar(50) NOT NULL,
		happeningOn varchar(300) NOT NULL
		)"""

        rsvp_query = """CREATE TABLE if not EXISTS rsvps(
		rsvp_id Serial PRIMARY KEY NOT NULL,
		user_id int REFERENCES users(id) on DELETE CASCADE,
		meetup_id int REFERENCES meetups(meetup_id) on DELETE CASCADE,
		response varchar(50) NOT NULL
		)"""

        fix = """CREATE EXTENSION IF NOT EXISTS citext;"""

        alteration = """ALTER TABLE users ALTER COLUMN username TYPE citext;"""

        email_alteration = """ALTER TABLE users ALTER COLUMN email TYPE citext;"""

        queries = [user_query, question_query,
                   meetup_query, rsvp_query, fix, alteration, email_alteration]
        for query in queries:
            self.cursor.execute(query)

        self.conn.commit()
        self.conn.close()

    def createAdmin(self):
        with connect() as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                if not user1.get_user_by_email(email='myadmin@gmail.com'):

                    password = generate_password_hash('Admin1')
                    registered = datetime.datetime.now()
                    cursor.execute("INSERT INTO users(firstname,lastname,email,password,phoneNumber,username,registered, isAdmin) VALUES( %s,%s,%s,%s,%s,%s,%s,%s)", (
                        'maggie', 'kimani', 'myadmin@gmail.com', password, '+25470818079', 'admin', registered, 'True'))

    def drop_tables(self):
        """Used to remove tables from database"""
        sql = [" DROP TABLE IF EXISTS questions CASCADE;",
               " DROP TABLE IF EXISTS users CASCADE;",
               " DROP TABLE IF EXISTS meetups CASCADE;",
               " DROP TABLE IF EXISTS rsvps  CASCADE;"
               ]
        for string in sql:
            self.cursor.execute(string)
        self.conn.commit()
        self.conn.close()
