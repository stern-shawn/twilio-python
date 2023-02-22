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
from twilio.rest.video.v1.room.participant.anonymize import AnonymizeList
from twilio.rest.video.v1.room.participant.published_track import PublishedTrackList
from twilio.rest.video.v1.room.participant.subscribe_rules import SubscribeRulesList
from twilio.rest.video.v1.room.participant.subscribed_track import SubscribedTrackList


class ParticipantList(ListResource):

    def __init__(self, version: Version, room_sid: str):
        """
        Initialize the ParticipantList

        :param Version version: Version that contains the resource
        :param room_sid: The SID of the room with the Participant resources to read.
        
        :returns: twilio.rest.video.v1.room.participant.ParticipantList
        :rtype: twilio.rest.video.v1.room.participant.ParticipantList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'room_sid': room_sid,  }
        self._uri = '/Rooms/${room_sid}/Participants'.format(**self._solution)
        
        
    
    
    
    def stream(self, status=values.unset, identity=values.unset, date_created_after=values.unset, date_created_before=values.unset, limit=None, page_size=None):
        """
        Streams ParticipantInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param RoomParticipantStatus status: Read only the participants with this status. Can be: `connected` or `disconnected`. For `in-progress` Rooms the default Status is `connected`, for `completed` Rooms only `disconnected` Participants are returned.
        :param str identity: Read only the Participants with this [User](https://www.twilio.com/docs/chat/rest/user-resource) `identity` value.
        :param datetime date_created_after: Read only Participants that started after this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :param datetime date_created_before: Read only Participants that started before this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.room.participant.ParticipantInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            status=status,
            identity=identity,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, status=values.unset, identity=values.unset, date_created_after=values.unset, date_created_before=values.unset, limit=None, page_size=None):
        """
        Lists ParticipantInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param RoomParticipantStatus status: Read only the participants with this status. Can be: `connected` or `disconnected`. For `in-progress` Rooms the default Status is `connected`, for `completed` Rooms only `disconnected` Participants are returned.
        :param str identity: Read only the Participants with this [User](https://www.twilio.com/docs/chat/rest/user-resource) `identity` value.
        :param datetime date_created_after: Read only Participants that started after this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :param datetime date_created_before: Read only Participants that started before this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.room.participant.ParticipantInstance]
        """
        return list(self.stream(
            status=status,
            identity=identity,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, status=values.unset, identity=values.unset, date_created_after=values.unset, date_created_before=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ParticipantInstance records from the API.
        Request is executed immediately
        
        :param RoomParticipantStatus status: Read only the participants with this status. Can be: `connected` or `disconnected`. For `in-progress` Rooms the default Status is `connected`, for `completed` Rooms only `disconnected` Participants are returned.
        :param str identity: Read only the Participants with this [User](https://www.twilio.com/docs/chat/rest/user-resource) `identity` value.
        :param datetime date_created_after: Read only Participants that started after this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :param datetime date_created_before: Read only Participants that started before this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ParticipantInstance
        :rtype: twilio.rest.video.v1.room.participant.ParticipantPage
        """
        data = values.of({ 
            'Status': status,
            'Identity': identity,
            'DateCreatedAfter': serialize.iso8601_datetime(date_created_after),
            'DateCreatedBefore': serialize.iso8601_datetime(date_created_before),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ParticipantPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ParticipantInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ParticipantInstance
        :rtype: twilio.rest.video.v1.room.participant.ParticipantPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ParticipantPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a ParticipantContext
        
        :param sid: The SID of the RoomParticipant resource to update.
        
        :returns: twilio.rest.video.v1.room.participant.ParticipantContext
        :rtype: twilio.rest.video.v1.room.participant.ParticipantContext
        """
        return ParticipantContext(self._version, room_sid=self._solution['room_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a ParticipantContext
        
        :param sid: The SID of the RoomParticipant resource to update.
        
        :returns: twilio.rest.video.v1.room.participant.ParticipantContext
        :rtype: twilio.rest.video.v1.room.participant.ParticipantContext
        """
        return ParticipantContext(self._version, room_sid=self._solution['room_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.ParticipantList>'






class ParticipantPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ParticipantPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.video.v1.room.participant.ParticipantPage
        :rtype: twilio.rest.video.v1.room.participant.ParticipantPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ParticipantInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.video.v1.room.participant.ParticipantInstance
        :rtype: twilio.rest.video.v1.room.participant.ParticipantInstance
        """
        return ParticipantInstance(self._version, payload, room_sid=self._solution['room_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.ParticipantPage>'





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
        

        
    
    def update(self, status):
        data = values.of({
            'status': status,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return ParticipantInstance(self._version, payload, room_sid=self._solution['room_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.ParticipantContext>'



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
        return '<Twilio.Video.V1.ParticipantInstance {}>'.format(context)



