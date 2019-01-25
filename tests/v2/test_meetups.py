import unittest
import json
from app import create_app
from .base import TestBase


class MeetupsTestCase(TestBase):

    def login(self):
        '''Method logins a user and returns token'''
        self.client.post(
            'api/v2/auth/signup', data=json.dumps(self.correct_user), content_type="application/json")
        response = self.client.post(
            'api/v2/auth/login', data=json.dumps(self.login_user), content_type='application/json')
        token = json.loads(response.data)['token']
        return token

    def test_create_meetup(self):
        '''Test if admin can create a meetup'''
        token = self.login()
        response = self.client.post('api/v2/meetups',
                                    data=json.dumps(self.data),
                                    headers={'Content-Type': 'application/json',
                                             'Authorization': 'Bearer ' + token})
        expected = "Meetup posted sucessfully"
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json.get('message'), expected)

    # def test_get_all_meetups(self):
    #     '''Test if user can get all meetup records'''
    #     self.client().post(
    #         'api/v2/meetups', data=json.dumps(self.data), content_type="application/json")
    #     response = self.client().get('api/v1/meetups/upcoming',
    #                                  content_type="application/json")
    #     expected = "These are the available meetups"
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json.get("message"), expected)

    # def test_unavailable_meetups(self):
    #     '''Test if user can get all meetup records'''
    #     response = self.client().get(
    #         'api/v2/meetups/upcoming', content_type="application/json")
    #     expected = "No meetup found"
    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(response.json.get("message"), expected)

    # def test_get_one_meetup(self):
    #     '''Test if the user can get a specific meetup record'''
    #     self.client().post(
    #         'api/v2/meetups', data=json.dumps(self.data), content_type="application/json")
    #     response = self.client().get(
    #         'api/v2/meetups/1', content_type="application/json")
    #     expected = "meetup retrieved"
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json.get("message"), expected)

    # def test_rsvp(self):
    #     '''Tests if a user can be able to rsvp to a specific meetup'''
    #     data = {
    #         "response": "yes"
    #     }
    #     self.client().post(
    #         'api/v/2meetups', data=json.dumps(self.data), content_type="application/json")
    #     response = self.client().post(
    #         'api/v2/meetups/1/rsvps', data=json.dumps(data), content_type="application/json")
    #     expected = "RSVP saved for this meetup"
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(response.json.get("message"), expected)
