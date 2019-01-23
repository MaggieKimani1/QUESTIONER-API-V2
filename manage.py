import os
import psycopg2
from flask import Flask
from instance.config import app_config
from werkzeug.security import generate_password_hash


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
		happeningOn varchar(300) NOT NULL,
		tags varchar(50) NOT NULL
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
            cur.execute(query)

        conn.commit()
        conn.close()

        # def create_admin(self):
        #     """This method creates the default users
        # 	   :param1:names.
        #        :param2:email.
        #        :param3:role.
        #        :param4:password.
        #     """
        #     conn = self.connection()
        #     cur = conn.cursor()
        #     if not self.select_one_user("admin@quickwear.com"):

        #         password = generate_password_hash('@Admin1')
        #         cur.execute("INSERT INTO users(email,names,password,role) VALUES(%s,%s,%s,%s)",
        #                     ('admin@quickwear.com', 'Sammy Njau', password, 'admin'))
        #         conn.commit()
        #         conn.close()
    def drop_tables(self):
        """Used to remove tables from database"""
        conn = self.connection()
        cur = conn.cursor()
        sql = [" DROP TABLE IF EXISTS questions CASCADE",
               " DROP TABLE IF EXISTS users CASCADE",
               " DROP TABLE IF EXISTS meetups CASCADE",
               " DROP TABLE IF EXISTS rsvps  CASCADE"
               ]
        for string in sql:
            cur.execute(string)
        conn.commit()
        conn.close()
