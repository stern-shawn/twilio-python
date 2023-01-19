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

# from twilio.rest.participant.anonymize import AnonymizeListInstancefrom twilio.rest.participant.published_track import PublishedTrackListInstancefrom twilio.rest.participant.subscribe_rules import SubscribeRulesListInstancefrom twilio.rest.participant.subscribed_track import SubscribedTrackListInstance


class ParticipantContext(InstanceContext):
    def __init__(self, version: Version, room_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'room_sid': room_sid, 'sid': sid,  }
        self._uri = '/Rooms/${room_sid}/Participants/${sid}'
        
        self._anonymize = None
        self._published_tracks = None
        self._subscribe_rules = None
        self._subscribed_tracks = None
    
    def fetch(self):
        
        """
        Fetch the ParticipantInstance

        :returns: The fetched ParticipantInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ParticipantInstance(self._version, payload, room_sid=self._solution['room_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return ParticipantInstance(self._version, payload, room_sid=self._solution['room_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ParticipantContext>'



class ParticipantInstance(InstanceResource):
    def __init__(self, version, payload, room_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'room_sid' : payload.get('room_sid'),
            'account_sid' : payload.get('account_sid'),
            'status' : payload.get('status'),
            'identity' : payload.get('identity'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'start_time' : payload.get('start_time'),
            'end_time' : payload.get('end_time'),
            'duration' : payload.get('duration'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'room_sid': room_sid or self._properties['room_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ParticipantContext(
                self._version,
                room_sid=self._solution['room_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def anonymize(self):
        return self._proxy.anonymize
    @property
    def published_tracks(self):
        return self._proxy.published_tracks
    @property
    def subscribe_rules(self):
        return self._proxy.subscribe_rules
    @property
    def subscribed_tracks(self):
        return self._proxy.subscribed_tracks
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.ParticipantInstance {}>'.format(context)



class ParticipantListInstance(ListResource):
    def __init__(self, version: Version, room_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'room_sid': room_sid,  }
        self._uri = '/Rooms/${room_sid}/Participants'
        
    
    """
    def page(self, status, identity, date_created_after, date_created_before, page_size):
        
        data = values.of({
            'status': status,'identity': identity,'date_created_after': date_created_after,'date_created_before': date_created_before,'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return ParticipantPage(self._version, payload, room_sid=self._solution['room_sid'], )
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ParticipantListInstance>'

