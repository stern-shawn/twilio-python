"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Video
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
    def __init__(self, version: Version, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid,  }
        self._uri = '/Recordings/${sid}'
        
    
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

        return RecordingInstance(self._version, payload, sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.RecordingContext>'



class RecordingInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'status' : payload.get('status'),
            'date_created' : payload.get('date_created'),
            'sid' : payload.get('sid'),
            'source_sid' : payload.get('source_sid'),
            'size' : payload.get('size'),
            'url' : payload.get('url'),
            'type' : payload.get('type'),
            'duration' : payload.get('duration'),
            'container_format' : payload.get('container_format'),
            'codec' : payload.get('codec'),
            'grouping_sids' : payload.get('grouping_sids'),
            'track_name' : payload.get('track_name'),
            'offset' : payload.get('offset'),
            'media_external_location' : payload.get('media_external_location'),
            'status_callback' : payload.get('status_callback'),
            'status_callback_method' : payload.get('status_callback_method'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = RecordingContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.RecordingInstance {}>'.format(context)



class RecordingList(ListResource):
    def __init__(self, version: Version):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Recordings'
        

    """
    def page(self, status, source_sid, grouping_sid, date_created_after, date_created_before, media_type, page_size):
        
        data = values.of({
            'status': status,'source_sid': source_sid,'grouping_sid': grouping_sid,'date_created_after': date_created_after,'date_created_before': date_created_before,'media_type': media_type,'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return RecordingPage(self._version, payload, )
    """


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.RecordingList>'

