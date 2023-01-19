"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version

from twilio.base.page import Page

# 


class RecordingContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, conference_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'conference_sid': conference_sid, 'sid': sid,  }
        self._uri = '/Accounts/${account_sid}/Conferences/${conference_sid}/Recordings/${sid}.json'
        
    
    def delete(self):
        
        

        """
        Deletes the RecordingInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the RecordingInstance

        :returns: The fetched RecordingInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return RecordingInstance(self._version, payload, account_sid=self._solution['account_sid'], conference_sid=self._solution['conference_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return RecordingInstance(self._version, payload, account_sid=self._solution['account_sid'], conference_sid=self._solution['conference_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.RecordingContext>'



class RecordingInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str, conference_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'api_version' : payload.get('api_version'),
            'call_sid' : payload.get('call_sid'),
            'conference_sid' : payload.get('conference_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'start_time' : payload.get('start_time'),
            'duration' : payload.get('duration'),
            'sid' : payload.get('sid'),
            'price' : payload.get('price'),
            'price_unit' : payload.get('price_unit'),
            'status' : payload.get('status'),
            'channels' : payload.get('channels'),
            'source' : payload.get('source'),
            'error_code' : payload.get('error_code'),
            'encryption_details' : payload.get('encryption_details'),
            'uri' : payload.get('uri'),
        }

        self._context = None
        self._solution = {
            'account_sid': account_sid or self._properties['account_sid'],'conference_sid': conference_sid or self._properties['conference_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = RecordingContext(
                self._version,
                account_sid=self._solution['account_sid'],conference_sid=self._solution['conference_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.RecordingInstance {}>'.format(context)



class RecordingListInstance(ListResource):
    def __init__(self, version: Version, account_sid: str, conference_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'conference_sid': conference_sid,  }
        self._uri = '/Accounts/${account_sid}/Conferences/${conference_sid}/Recordings.json'
        
    
    """
    def page(self, date_created, date_created, date_created, page_size):
        
        data = values.of({
            'date_created': date_created,'date_created': date_created,'date_created': date_created,'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return RecordingPage(self._version, payload, account_sid=self._solution['account_sid'], conference_sid=self._solution['conference_sid'], )
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.RecordingListInstance>'

