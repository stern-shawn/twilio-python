r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Insights
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
from twilio.rest.insights.v1.room.participant import ParticipantList


class RoomList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the RoomList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.insights.v1.room.RoomList
        :rtype: twilio.rest.insights.v1.room.RoomList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Video/Rooms'.format(**self._solution)
        
        
    
    
    def stream(self, room_type=values.unset, codec=values.unset, room_name=values.unset, created_after=values.unset, created_before=values.unset, limit=None, page_size=None):
        """
        Streams RoomInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param list[RoomInstance.RoomType] room_type: Type of room. Can be `go`, `peer_to_peer`, `group`, or `group_small`.
        :param list[RoomInstance.Codec] codec: Codecs used by participants in the room. Can be `VP8`, `H264`, or `VP9`.
        :param str room_name: Room friendly name.
        :param datetime created_after: Only read rooms that started on or after this ISO 8601 timestamp.
        :param datetime created_before: Only read rooms that started before this ISO 8601 timestamp.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.room.RoomInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            room_type=room_type,
            codec=codec,
            room_name=room_name,
            created_after=created_after,
            created_before=created_before,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, room_type=values.unset, codec=values.unset, room_name=values.unset, created_after=values.unset, created_before=values.unset, limit=None, page_size=None):
        """
        Asynchronous coroutine that streams RoomInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param list[RoomInstance.RoomType] room_type: Type of room. Can be `go`, `peer_to_peer`, `group`, or `group_small`.
        :param list[RoomInstance.Codec] codec: Codecs used by participants in the room. Can be `VP8`, `H264`, or `VP9`.
        :param str room_name: Room friendly name.
        :param datetime created_after: Only read rooms that started on or after this ISO 8601 timestamp.
        :param datetime created_before: Only read rooms that started before this ISO 8601 timestamp.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.room.RoomInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            room_type=room_type,
            codec=codec,
            room_name=room_name,
            created_after=created_after,
            created_before=created_before,
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, room_type=values.unset, codec=values.unset, room_name=values.unset, created_after=values.unset, created_before=values.unset, limit=None, page_size=None):
        """
        Lists RoomInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param list[RoomInstance.RoomType] room_type: Type of room. Can be `go`, `peer_to_peer`, `group`, or `group_small`.
        :param list[RoomInstance.Codec] codec: Codecs used by participants in the room. Can be `VP8`, `H264`, or `VP9`.
        :param str room_name: Room friendly name.
        :param datetime created_after: Only read rooms that started on or after this ISO 8601 timestamp.
        :param datetime created_before: Only read rooms that started before this ISO 8601 timestamp.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.room.RoomInstance]
        """
        return list(self.stream(
            room_type=room_type,
            codec=codec,
            room_name=room_name,
            created_after=created_after,
            created_before=created_before,
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, room_type=values.unset, codec=values.unset, room_name=values.unset, created_after=values.unset, created_before=values.unset, limit=None, page_size=None):
        """
        Asynchronous coroutine that lists RoomInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param list[RoomInstance.RoomType] room_type: Type of room. Can be `go`, `peer_to_peer`, `group`, or `group_small`.
        :param list[RoomInstance.Codec] codec: Codecs used by participants in the room. Can be `VP8`, `H264`, or `VP9`.
        :param str room_name: Room friendly name.
        :param datetime created_after: Only read rooms that started on or after this ISO 8601 timestamp.
        :param datetime created_before: Only read rooms that started before this ISO 8601 timestamp.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.room.RoomInstance]
        """
        return list(await self.stream_async(
            room_type=room_type,
            codec=codec,
            room_name=room_name,
            created_after=created_after,
            created_before=created_before,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, room_type=values.unset, codec=values.unset, room_name=values.unset, created_after=values.unset, created_before=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of RoomInstance records from the API.
        Request is executed immediately
        
        :param list[RoomInstance.RoomType] room_type: Type of room. Can be `go`, `peer_to_peer`, `group`, or `group_small`.
        :param list[RoomInstance.Codec] codec: Codecs used by participants in the room. Can be `VP8`, `H264`, or `VP9`.
        :param str room_name: Room friendly name.
        :param datetime created_after: Only read rooms that started on or after this ISO 8601 timestamp.
        :param datetime created_before: Only read rooms that started before this ISO 8601 timestamp.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RoomInstance
        :rtype: twilio.rest.insights.v1.room.RoomPage
        """
        data = values.of({ 
            'RoomType': serialize.map(room_type),
            'Codec': serialize.map(codec),
            'RoomName': room_name,
            'CreatedAfter': serialize.iso8601_datetime(created_after),
            'CreatedBefore': serialize.iso8601_datetime(created_before),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return RoomPage(self._version, response, self._solution)

    async def page_async(self, room_type=values.unset, codec=values.unset, room_name=values.unset, created_after=values.unset, created_before=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronous coroutine that retrieve a single page of RoomInstance records from the API.
        Request is executed immediately
        
        :param list[RoomInstance.RoomType] room_type: Type of room. Can be `go`, `peer_to_peer`, `group`, or `group_small`.
        :param list[RoomInstance.Codec] codec: Codecs used by participants in the room. Can be `VP8`, `H264`, or `VP9`.
        :param str room_name: Room friendly name.
        :param datetime created_after: Only read rooms that started on or after this ISO 8601 timestamp.
        :param datetime created_before: Only read rooms that started before this ISO 8601 timestamp.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RoomInstance
        :rtype: twilio.rest.insights.v1.room.RoomPage
        """
        data = values.of({ 
            'RoomType': serialize.map(room_type),
            'Codec': serialize.map(codec),
            'RoomName': room_name,
            'CreatedAfter': serialize.iso8601_datetime(created_after),
            'CreatedBefore': serialize.iso8601_datetime(created_before),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return RoomPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of RoomInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RoomInstance
        :rtype: twilio.rest.insights.v1.room.RoomPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return RoomPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronous coroutine that retrieve a specific page of RoomInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RoomInstance
        :rtype: twilio.rest.insights.v1.room.RoomPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return RoomPage(self._version, response, self._solution)


    def get(self, room_sid):
        """
        Constructs a RoomContext
        
        :param room_sid: The SID of the Room resource.
        
        :returns: twilio.rest.insights.v1.room.RoomContext
        :rtype: twilio.rest.insights.v1.room.RoomContext
        """
        return RoomContext(self._version, room_sid=room_sid)

    def __call__(self, room_sid):
        """
        Constructs a RoomContext
        
        :param room_sid: The SID of the Room resource.
        
        :returns: twilio.rest.insights.v1.room.RoomContext
        :rtype: twilio.rest.insights.v1.room.RoomContext
        """
        return RoomContext(self._version, room_sid=room_sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.RoomList>'




class RoomPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the RoomPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.insights.v1.room.RoomPage
        :rtype: twilio.rest.insights.v1.room.RoomPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of RoomInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.insights.v1.room.RoomInstance
        :rtype: twilio.rest.insights.v1.room.RoomInstance
        """
        return RoomInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.RoomPage>'




class RoomContext(InstanceContext):

    def __init__(self, version: Version, room_sid: str):
        """
        Initialize the RoomContext

        :param Version version: Version that contains the resource
        :param room_sid: The SID of the Room resource.

        :returns: twilio.rest.insights.v1.room.RoomContext
        :rtype: twilio.rest.insights.v1.room.RoomContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'room_sid': room_sid,
        }
        self._uri = '/Video/Rooms/{room_sid}'.format(**self._solution)
        
        self._participants = None
    
    
    def fetch(self):
        """
        Fetch the RoomInstance
        

        :returns: The fetched RoomInstance
        :rtype: twilio.rest.insights.v1.room.RoomInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return RoomInstance(
            self._version,
            payload,
            room_sid=self._solution['room_sid'],
            
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the RoomInstance
        

        :returns: The fetched RoomInstance
        :rtype: twilio.rest.insights.v1.room.RoomInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return RoomInstance(
            self._version,
            payload,
            room_sid=self._solution['room_sid'],
            
        )
    
    
    @property
    def participants(self):
        """
        Access the participants

        :returns: twilio.rest.insights.v1.room.ParticipantList
        :rtype: twilio.rest.insights.v1.room.ParticipantList
        """
        if self._participants is None:
            self._participants = ParticipantList(self._version, self._solution['room_sid'],
            )
        return self._participants
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.RoomContext {}>'.format(context)

class RoomInstance(InstanceResource):

    class Codec(object):
        VP8 = "VP8"
        H264 = "H264"
        VP9 = "VP9"

    class CreatedMethod(object):
        SDK = "sdk"
        AD_HOC = "ad_hoc"
        API = "api"

    class EdgeLocation(object):
        ASHBURN = "ashburn"
        DUBLIN = "dublin"
        FRANKFURT = "frankfurt"
        SINGAPORE = "singapore"
        SYDNEY = "sydney"
        SAO_PAULO = "sao_paulo"
        ROAMING = "roaming"
        UMATILLA = "umatilla"
        TOKYO = "tokyo"

    class EndReason(object):
        ROOM_ENDED_VIA_API = "room_ended_via_api"
        TIMEOUT = "timeout"

    class ProcessingState(object):
        COMPLETE = "complete"
        IN_PROGRESS = "in_progress"

    class RoomStatus(object):
        IN_PROGRESS = "in_progress"
        COMPLETED = "completed"

    class RoomType(object):
        GO = "go"
        PEER_TO_PEER = "peer_to_peer"
        GROUP = "group"
        GROUP_SMALL = "group_small"

    class TwilioRealm(object):
        US1 = "us1"
        US2 = "us2"
        AU1 = "au1"
        BR1 = "br1"
        IE1 = "ie1"
        JP1 = "jp1"
        SG1 = "sg1"
        IN1 = "in1"
        DE1 = "de1"
        GLL = "gll"

    def __init__(self, version, payload, room_sid: str=None):
        """
        Initialize the RoomInstance
        :returns: twilio.rest.insights.v1.room.RoomInstance
        :rtype: twilio.rest.insights.v1.room.RoomInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'room_sid': payload.get('room_sid'),
            'room_name': payload.get('room_name'),
            'create_time': deserialize.iso8601_datetime(payload.get('create_time')),
            'end_time': deserialize.iso8601_datetime(payload.get('end_time')),
            'room_type': payload.get('room_type'),
            'room_status': payload.get('room_status'),
            'status_callback': payload.get('status_callback'),
            'status_callback_method': payload.get('status_callback_method'),
            'created_method': payload.get('created_method'),
            'end_reason': payload.get('end_reason'),
            'max_participants': deserialize.integer(payload.get('max_participants')),
            'unique_participants': deserialize.integer(payload.get('unique_participants')),
            'unique_participant_identities': deserialize.integer(payload.get('unique_participant_identities')),
            'concurrent_participants': deserialize.integer(payload.get('concurrent_participants')),
            'max_concurrent_participants': deserialize.integer(payload.get('max_concurrent_participants')),
            'codecs': payload.get('codecs'),
            'media_region': payload.get('media_region'),
            'duration_sec': payload.get('duration_sec'),
            'total_participant_duration_sec': payload.get('total_participant_duration_sec'),
            'total_recording_duration_sec': payload.get('total_recording_duration_sec'),
            'processing_state': payload.get('processing_state'),
            'recording_enabled': payload.get('recording_enabled'),
            'edge_location': payload.get('edge_location'),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'room_sid': room_sid or self._properties['room_sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RoomContext for this RoomInstance
        :rtype: twilio.rest.insights.v1.room.RoomContext
        """
        if self._context is None:
            self._context = RoomContext(self._version, room_sid=self._solution['room_sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: Account SID associated with this room.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def room_sid(self):
        """
        :returns: Unique identifier for the room.
        :rtype: str
        """
        return self._properties['room_sid']
    
    @property
    def room_name(self):
        """
        :returns: Room friendly name.
        :rtype: str
        """
        return self._properties['room_name']
    
    @property
    def create_time(self):
        """
        :returns: Creation time of the room.
        :rtype: datetime
        """
        return self._properties['create_time']
    
    @property
    def end_time(self):
        """
        :returns: End time for the room.
        :rtype: datetime
        """
        return self._properties['end_time']
    
    @property
    def room_type(self):
        """
        :returns: 
        :rtype: RoomInstance.RoomType
        """
        return self._properties['room_type']
    
    @property
    def room_status(self):
        """
        :returns: 
        :rtype: RoomInstance.RoomStatus
        """
        return self._properties['room_status']
    
    @property
    def status_callback(self):
        """
        :returns: Webhook provided for status callbacks.
        :rtype: str
        """
        return self._properties['status_callback']
    
    @property
    def status_callback_method(self):
        """
        :returns: HTTP method provided for status callback URL.
        :rtype: str
        """
        return self._properties['status_callback_method']
    
    @property
    def created_method(self):
        """
        :returns: 
        :rtype: RoomInstance.CreatedMethod
        """
        return self._properties['created_method']
    
    @property
    def end_reason(self):
        """
        :returns: 
        :rtype: RoomInstance.EndReason
        """
        return self._properties['end_reason']
    
    @property
    def max_participants(self):
        """
        :returns: Max number of total participants allowed by the application settings.
        :rtype: int
        """
        return self._properties['max_participants']
    
    @property
    def unique_participants(self):
        """
        :returns: Number of participants. May include duplicate identities for participants who left and rejoined.
        :rtype: int
        """
        return self._properties['unique_participants']
    
    @property
    def unique_participant_identities(self):
        """
        :returns: Unique number of participant identities.
        :rtype: int
        """
        return self._properties['unique_participant_identities']
    
    @property
    def concurrent_participants(self):
        """
        :returns: Actual number of concurrent participants.
        :rtype: int
        """
        return self._properties['concurrent_participants']
    
    @property
    def max_concurrent_participants(self):
        """
        :returns: Maximum number of participants allowed in the room at the same time allowed by the application settings.
        :rtype: int
        """
        return self._properties['max_concurrent_participants']
    
    @property
    def codecs(self):
        """
        :returns: Codecs used by participants in the room. Can be `VP8`, `H264`, or `VP9`.
        :rtype: list[RoomInstance.Codec]
        """
        return self._properties['codecs']
    
    @property
    def media_region(self):
        """
        :returns: 
        :rtype: RoomInstance.TwilioRealm
        """
        return self._properties['media_region']
    
    @property
    def duration_sec(self):
        """
        :returns: Total room duration from create time to end time.
        :rtype: int
        """
        return self._properties['duration_sec']
    
    @property
    def total_participant_duration_sec(self):
        """
        :returns: Combined amount of participant time in the room.
        :rtype: int
        """
        return self._properties['total_participant_duration_sec']
    
    @property
    def total_recording_duration_sec(self):
        """
        :returns: Combined amount of recorded seconds for participants in the room.
        :rtype: int
        """
        return self._properties['total_recording_duration_sec']
    
    @property
    def processing_state(self):
        """
        :returns: 
        :rtype: RoomInstance.ProcessingState
        """
        return self._properties['processing_state']
    
    @property
    def recording_enabled(self):
        """
        :returns: Boolean indicating if recording is enabled for the room.
        :rtype: bool
        """
        return self._properties['recording_enabled']
    
    @property
    def edge_location(self):
        """
        :returns: 
        :rtype: RoomInstance.EdgeLocation
        """
        return self._properties['edge_location']
    
    @property
    def url(self):
        """
        :returns: URL for the room resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: Room subresources.
        :rtype: dict
        """
        return self._properties['links']
    
    
    def fetch(self):
        """
        Fetch the RoomInstance
        

        :returns: The fetched RoomInstance
        :rtype: twilio.rest.insights.v1.room.RoomInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the RoomInstance
        

        :returns: The fetched RoomInstance
        :rtype: twilio.rest.insights.v1.room.RoomInstance
        """
        return await self._proxy.fetch_async()
    
    @property
    def participants(self):
        """
        Access the participants

        :returns: twilio.rest.insights.v1.room.ParticipantList
        :rtype: twilio.rest.insights.v1.room.ParticipantList
        """
        return self._proxy.participants
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.RoomInstance {}>'.format(context)


