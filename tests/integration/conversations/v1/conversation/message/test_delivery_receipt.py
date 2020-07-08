# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class DeliveryReceiptTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.conversations.v1.conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .messages("IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .delivery_receipts("DYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://conversations.twilio.com/v1/Conversations/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Receipts/DYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "DYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "message_sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "channel_message_sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "failed",
                "error_code": 3000,
                "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2016-03-24T20:37:57Z",
                "date_updated": "2016-03-24T20:37:57Z",
                "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts/DYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.conversations.v1.conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .messages("IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .delivery_receipts("DYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.conversations.v1.conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .messages("IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .delivery_receipts.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://conversations.twilio.com/v1/Conversations/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Receipts',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "delivery_receipts"
                },
                "delivery_receipts": [
                    {
                        "sid": "DYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "message_sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "channel_message_sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "status": "failed",
                        "error_code": 3000,
                        "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2016-03-24T20:37:57Z",
                        "date_updated": "2016-03-24T20:37:57Z",
                        "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts/DYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    {
                        "sid": "DYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "message_sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "channel_message_sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "status": "failed",
                        "error_code": 3000,
                        "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2016-03-24T20:37:57Z",
                        "date_updated": "2016-03-24T20:37:57Z",
                        "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts/DYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    {
                        "sid": "DYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "message_sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "channel_message_sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "status": "failed",
                        "error_code": 3000,
                        "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2016-03-24T20:37:57Z",
                        "date_updated": "2016-03-24T20:37:57Z",
                        "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts/DYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ]
            }
            '''
        ))

        actual = self.client.conversations.v1.conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .messages("IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .delivery_receipts.list()

        self.assertIsNotNone(actual)
