"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Media
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

# from twilio.rest.player_streamer.playback_grant import PlaybackGrantListInstance


class PlayerStreamerContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid,  }
        self._uri = '/PlayerStreamers/${sid}'
        
        self._playback_grant = None
    
    def fetch(self):
        
        """
        Fetch the PlayerStreamerInstance

        :returns: The fetched PlayerStreamerInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return PlayerStreamerInstance(self._version, payload, sid=self._solution['sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return PlayerStreamerInstance(self._version, payload, sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.PlayerStreamerContext>'



class PlayerStreamerInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'video' : payload.get('video'),
            'links' : payload.get('links'),
            'sid' : payload.get('sid'),
            'status' : payload.get('status'),
            'url' : payload.get('url'),
            'status_callback' : payload.get('status_callback'),
            'status_callback_method' : payload.get('status_callback_method'),
            'ended_reason' : payload.get('ended_reason'),
            'max_duration' : payload.get('max_duration'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = PlayerStreamerContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def playback_grant(self):
        return self._proxy.playback_grant
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.PlayerStreamerInstance {}>'.format(context)



class PlayerStreamerList(ListResource):
    def __init__(self, version: Version):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/PlayerStreamers'
        

    """
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return PlayerStreamerInstance(self._version, payload, )
        
    """

    """
    def page(self, order, status, page_size):
        
        data = values.of({
            'order': order,'status': status,'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return PlayerStreamerPage(self._version, payload, )
    """


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.PlayerStreamerList>'

