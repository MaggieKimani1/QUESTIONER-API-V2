import unittest
from .base import TestBase
import json


class TestUsers(TestBase):
    def test_user_signup(self):
        response = self.client.post(
            'api/v2/auth', data=json.dumps(self.correct_user), content_type="application/json")
        expected = "user created"
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json.get('message'), expected)

    def test_login(self):
        self.client.post(
            'api/v2/auth', data=json.dumps(self.correct_user), content_type="application/json")
        response = self.client.post(
            'api/v2/auth/login', data=json.dumps(self.login_user), content_type='application/json')
        token = json.loads(response.get_data())["token"]
        return token
