import unittest
import os
import json
from app import create_app
from instance.config import app_config
from manage import Database
import datetime


class TestBase(unittest.TestCase):
    """This class holds data shared among tests"""

    def setUp(self):
        """The setUp method is the method that initialize the variables to be used by the test methods"""
        self.app = create_app(config_name="development")
        self.db = Database("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        """Auth variables"""
        self.correct_user = {
            "firstname": "Maggie",
            "lastname": "Kimani",
            "email": "Maggiekim42@gmail.com",
            "password": "Nyambura",
            "confirm_password": "Nyambura",
            "phoneNumber": "0708818079",
            "username": "maggiekimani1",
            "registered": datetime.datetime.now().strftime("%y-%m-%d-%H-%M"),
            "isAdmin": False
        }

        self.no_firstname_user = {
            "firstname": "",
            "lastname": "Kimani",
            "email": "Maggiekim@gmail.com",
            "password": "Nyambura",
            "confirm_password": "Nyambura",
            "phoneNumber": "0708818079",
            "username": "maggiekimani1",
            "registered": datetime.datetime.now().strftime("%y-%m-%d-%H-%M"),
            "isAdmin": False
        }
        self.no_lastname_user = {
            "firstname": "Maggie",
            "lastname": "",
            "email": "Maggie42@gmail.com",
            "password": "Nyambura",
            "confirm_password": "Nyambura",
            "phoneNumber": "0708818079",
            "username": "maggiekimani1",
            "registered": datetime.datetime.now().strftime("%y-%m-%d-%H-%M"),
            "isAdmin": False
        }
        self.blank_email_user = {
            "firstname": "Maggie",
            "lastname": "Kimani",
            "email": "",
            "password": "Nyambura",
            "confirm_password": "Nyambura",
            "phoneNumber": "0708818079",
            "username": "maggiekimani1",
            "registered": datetime.datetime.now().strftime("%y-%m-%d-%H-%M"),
            "isAdmin": False
        }
        self.login_user = {
            "email": "Maggiekim42@gmail.com",
            "password": "Nyambura"

        }

    def tearDown(self):
        '''Method to clear all tables before another test is undertaken'''
        self.db.drop_tables()
        self.app_context.pop()
