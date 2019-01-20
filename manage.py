import os
import psycopg2
from flask import Flask
from instance.config import app_config


environment = os.environ["APP_SETTINGS"]
DATABASE_URL = app_config[environment].DATABASE_URL


class Database(object):
    """This Class has the setup for connecting to the database and creation of tables """

    def connection(self):
        """This method creates a connection to the class
           param:connection
           return:connection
        """
        conn = psycopg2.connect(DATABASE_URL)
        return conn

    def createTables(self):
        """This method creates all tables if they dont exist
                        param1:connection
                        param2:queries
                        param3:cursor
        """

        conn = self.connection()
        cur = conn.cursor()

        user_query = """CREATE TABLE if not EXISTS users(
		id Serial PRIMARY KEY NOT NULL,
		firstname varchar(40) NOT NULL,
		lastname varchar(40) NOT NULL,
		email varchar(100) NOT NULL,
		othername varchar(40) NOT NULL,
		phoneNumber int NOT NULL,
		username varchar(100)  NOT NULL,
		registered date NOT NULL,
		isAdmin boolean NOT NULL
		)"""

        question_query = """CREATE TABLE if not EXISTS questions(
		question_id Serial PRIMARY KEY NOT NULL,
		createdOn date NOT NULL,
		createdBy int REFERENCES users(user_id) on DELETE CASCADE,
		meetup varchar(100)  NOT NULL,
		title varchar(50) NOT NULL,
		body varchar(250) NOT NULL,
		votes int NOT NULL
		)"""

        meetup_query = """CREATE TABLE if not EXISTS meetups(
		meetup_id Serial PRIMARY KEY NOT NULL,
		createdOn date NOT NULL,
		location varchar(50) NOT NULL,
		images varchar(50) NOT NULL,
		topic varchar(50) NOT NULL,
		happeningOn date NOT NULL,
		tags varchar(50) NOT NULL
		)"""

        rsvp_query = """CREATE TABLE if not EXISTS rsvps(
		rsvp_id Serial PRIMARY KEY NOT NULL,
		user_id int REFERENCES users(user_id) on DELETE CASCADE,
		meetup_id int REFERENCES meetups(meetup_id) on DELETE CASCADE,
		response varchar(50) NOT NULL
		)"""

        queries = [user_query, question_query, meetup_query, rsvp_query]
        for query in queries:
            cur.execute(query)

        conn.commit()
        conn.close()
