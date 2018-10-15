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


class QueryTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .queries(sid="UHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://autopilot.twilio.com/v1/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Queries/UHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "language": "language",
                "date_created": "2015-07-30T20:00:00Z",
                "model_build_sid": "UGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "query": "query",
                "date_updated": "2015-07-30T20:00:00Z",
                "status": "status",
                "sample_sid": "UFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "assistant_sid": "UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "results": {
                    "task": {
                        "name": "name",
                        "task_sid": "UDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "confidence": 0.9
                    },
                    "entities": [
                        {
                            "name": "name",
                            "value": "value",
                            "type": "type"
                        }
                    ]
                },
                "url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queries/UHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "UHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "source_channel": "voice"
            }
            '''
        ))

        actual = self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .queries(sid="UHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .queries.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://autopilot.twilio.com/v1/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Queries',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "queries": [],
                "meta": {
                    "previous_page_url": null,
                    "next_page_url": null,
                    "first_page_url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queries?PageSize=50&Page=0",
                    "page": 0,
                    "key": "queries",
                    "url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queries?PageSize=50&Page=0",
                    "page_size": 50
                }
            }
            '''
        ))

        actual = self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .queries.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "queries": [
                    {
                        "language": "language",
                        "date_created": "2015-07-30T20:00:00Z",
                        "model_build_sid": "UGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "query": "query",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "status": "status",
                        "sample_sid": "UFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "assistant_sid": "UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "results": {
                            "task": {
                                "name": "name",
                                "task_sid": "UDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                "confidence": 0.9
                            },
                            "entities": [
                                {
                                    "name": "name",
                                    "value": "value",
                                    "type": "type"
                                }
                            ]
                        },
                        "url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queries/UHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sid": "UHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "source_channel": null
                    }
                ],
                "meta": {
                    "previous_page_url": null,
                    "next_page_url": null,
                    "first_page_url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queries?PageSize=50&Page=0",
                    "page": 0,
                    "key": "queries",
                    "url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queries?PageSize=50&Page=0",
                    "page_size": 50
                }
            }
            '''
        ))

        actual = self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .queries.list()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .queries.create(language="language", query="query")

        values = {'Language': "language", 'Query': "query", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://autopilot.twilio.com/v1/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Queries',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "language": "language",
                "date_created": "2015-07-30T20:00:00Z",
                "model_build_sid": "UGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "query": "query",
                "date_updated": "2015-07-30T20:00:00Z",
                "status": "status",
                "sample_sid": "UFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "assistant_sid": "UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "results": {
                    "task": {
                        "name": "name",
                        "task_sid": "UDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "confidence": 0.9
                    },
                    "entities": [
                        {
                            "name": "name",
                            "value": "value",
                            "type": "type"
                        }
                    ]
                },
                "url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queries/UHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "UHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "source_channel": "voice"
            }
            '''
        ))

        actual = self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .queries.create(language="language", query="query")

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .queries(sid="UHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://autopilot.twilio.com/v1/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Queries/UHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "language": "language",
                "date_created": "2015-07-30T20:00:00Z",
                "model_build_sid": "UGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "query": "query",
                "date_updated": "2015-07-30T20:00:00Z",
                "status": "status",
                "sample_sid": "UFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "assistant_sid": "UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "results": {
                    "task": {
                        "name": "name",
                        "task_sid": "UDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "confidence": 0.9
                    },
                    "entities": [
                        {
                            "name": "name",
                            "value": "value",
                            "type": "type"
                        }
                    ]
                },
                "url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queries/UHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "UHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "source_channel": "sms"
            }
            '''
        ))

        actual = self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .queries(sid="UHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .queries(sid="UHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://autopilot.twilio.com/v1/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Queries/UHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.autopilot.v1.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .queries(sid="UHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)
