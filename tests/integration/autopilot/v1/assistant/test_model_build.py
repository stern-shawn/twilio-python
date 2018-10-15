# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class ModelBuildTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .model_builds(sid="UGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://autopilot.twilio.com/v1/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/ModelBuilds/UGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ModelBuilds/UGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "enqueued",
                "assistant_sid": "UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "sid": "UGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "unique_name",
                "build_duration": null,
                "error_code": null
            }
            '''
        ))

        actual = self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .model_builds(sid="UGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .model_builds.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://autopilot.twilio.com/v1/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/ModelBuilds',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "key": "model_builds",
                    "url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ModelBuilds?PageSize=50&Page=0",
                    "first_page_url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ModelBuilds?PageSize=50&Page=0",
                    "next_page_url": null,
                    "previous_page_url": null,
                    "page_size": 50
                },
                "model_builds": []
            }
            '''
        ))

        actual = self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .model_builds.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "key": "model_builds",
                    "url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ModelBuilds?PageSize=50&Page=0",
                    "first_page_url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ModelBuilds?PageSize=50&Page=0",
                    "next_page_url": null,
                    "previous_page_url": null,
                    "page_size": 50
                },
                "model_builds": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ModelBuilds/UGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "status": "failed",
                        "assistant_sid": "UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-07-30T20:00:00Z",
                        "sid": "UGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "unique_name": "unique_name",
                        "build_duration": null,
                        "error_code": 23001
                    }
                ]
            }
            '''
        ))

        actual = self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .model_builds.list()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .model_builds.create()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://autopilot.twilio.com/v1/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/ModelBuilds',
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ModelBuilds/UGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "enqueued",
                "assistant_sid": "UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "sid": "UGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "unique_name",
                "build_duration": null,
                "error_code": null
            }
            '''
        ))

        actual = self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .model_builds.create()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .model_builds(sid="UGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://autopilot.twilio.com/v1/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/ModelBuilds/UGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ModelBuilds/UGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "completed",
                "assistant_sid": "UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "sid": "UGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "unique_name",
                "build_duration": 100,
                "error_code": null
            }
            '''
        ))

        actual = self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .model_builds(sid="UGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .model_builds(sid="UGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://autopilot.twilio.com/v1/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/ModelBuilds/UGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .model_builds(sid="UGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)
