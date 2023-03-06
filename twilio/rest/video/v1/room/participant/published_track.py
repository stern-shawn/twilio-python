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


class PublishedTrackList(ListResource):

    def __init__(self, version: Version, room_sid: str, participant_sid: str):
        """
        Initialize the PublishedTrackList

        :param Version version: Version that contains the resource
        :param room_sid: The SID of the Room resource where the Track resources to read are published.
        :param participant_sid: The SID of the Participant resource with the published tracks to read.
        
        :returns: twilio.rest.video.v1.room.participant.published_track.PublishedTrackList
        :rtype: twilio.rest.video.v1.room.participant.published_track.PublishedTrackList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'room_sid': room_sid, 'participant_sid': participant_sid,  }
        self._uri = '/Rooms/{room_sid}/Participants/{participant_sid}/PublishedTracks'.format(**self._solution)
        
        
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams PublishedTrackInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.room.participant.published_track.PublishedTrackInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists PublishedTrackInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.room.participant.published_track.PublishedTrackInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of PublishedTrackInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of PublishedTrackInstance
        :rtype: twilio.rest.video.v1.room.participant.published_track.PublishedTrackPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return PublishedTrackPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of PublishedTrackInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of PublishedTrackInstance
        :rtype: twilio.rest.video.v1.room.participant.published_track.PublishedTrackPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return PublishedTrackPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a PublishedTrackContext
        
        :param sid: The SID of the RoomParticipantPublishedTrack resource to fetch.
        
        :returns: twilio.rest.video.v1.room.participant.published_track.PublishedTrackContext
        :rtype: twilio.rest.video.v1.room.participant.published_track.PublishedTrackContext
        """
        return PublishedTrackContext(self._version, room_sid=self._solution['room_sid'], participant_sid=self._solution['participant_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a PublishedTrackContext
        
        :param sid: The SID of the RoomParticipantPublishedTrack resource to fetch.
        
        :returns: twilio.rest.video.v1.room.participant.published_track.PublishedTrackContext
        :rtype: twilio.rest.video.v1.room.participant.published_track.PublishedTrackContext
        """
        return PublishedTrackContext(self._version, room_sid=self._solution['room_sid'], participant_sid=self._solution['participant_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.PublishedTrackList>'




class PublishedTrackPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the PublishedTrackPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.video.v1.room.participant.published_track.PublishedTrackPage
        :rtype: twilio.rest.video.v1.room.participant.published_track.PublishedTrackPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of PublishedTrackInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.video.v1.room.participant.published_track.PublishedTrackInstance
        :rtype: twilio.rest.video.v1.room.participant.published_track.PublishedTrackInstance
        """
        return PublishedTrackInstance(self._version, payload, room_sid=self._solution['room_sid'], participant_sid=self._solution['participant_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.PublishedTrackPage>'




class PublishedTrackContext(InstanceContext):

    def __init__(self, version: Version, room_sid: str, participant_sid: str, sid: str):
        """
        Initialize the PublishedTrackContext

        :param Version version: Version that contains the resource
        :param room_sid: The SID of the Room resource where the Track resource to fetch is published.:param participant_sid: The SID of the Participant resource with the published track to fetch.:param sid: The SID of the RoomParticipantPublishedTrack resource to fetch.

        :returns: twilio.rest.video.v1.room.participant.published_track.PublishedTrackContext
        :rtype: twilio.rest.video.v1.room.participant.published_track.PublishedTrackContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'room_sid': room_sid,
            'participant_sid': participant_sid,
            'sid': sid,
        }
        self._uri = '/Rooms/{room_sid}/Participants/{participant_sid}/PublishedTracks/{sid}'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the PublishedTrackInstance
        

        :returns: The fetched PublishedTrackInstance
        :rtype: twilio.rest.video.v1.room.participant.published_track.PublishedTrackInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return PublishedTrackInstance(
            self._version,
            payload,
            room_sid=self._solution['room_sid'],
            participant_sid=self._solution['participant_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.PublishedTrackContext {}>'.format(context)

class PublishedTrackInstance(InstanceResource):

    class Kind(object):
        AUDIO = "audio"
        VIDEO = "video"
        DATA = "data"

    def __init__(self, version, payload, room_sid: str, participant_sid: str, sid: str=None):
        """
        Initialize the PublishedTrackInstance
        :returns: twilio.rest.video.v1.room.participant.published_track.PublishedTrackInstance
        :rtype: twilio.rest.video.v1.room.participant.published_track.PublishedTrackInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'participant_sid': payload.get('participant_sid'),
            'room_sid': payload.get('room_sid'),
            'name': payload.get('name'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'enabled': payload.get('enabled'),
            'kind': payload.get('kind'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'room_sid': room_sid, 'participant_sid': participant_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: PublishedTrackContext for this PublishedTrackInstance
        :rtype: twilio.rest.video.v1.room.participant.published_track.PublishedTrackContext
        """
        if self._context is None:
            self._context = PublishedTrackContext(self._version, room_sid=self._solution['room_sid'], participant_sid=self._solution['participant_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the RoomParticipantPublishedTrack resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def participant_sid(self):
        """
        :returns: The SID of the Participant resource with the published track.
        :rtype: str
        """
        return self._properties['participant_sid']
    
    @property
    def room_sid(self):
        """
        :returns: The SID of the Room resource where the track is published.
        :rtype: str
        """
        return self._properties['room_sid']
    
    @property
    def name(self):
        """
        :returns: The track name. Must be no more than 128 characters, and be unique among the participant's published tracks.
        :rtype: str
        """
        return self._properties['name']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def enabled(self):
        """
        :returns: Whether the track is enabled.
        :rtype: bool
        """
        return self._properties['enabled']
    
    @property
    def kind(self):
        """
        :returns: 
        :rtype: Kind
        """
        return self._properties['kind']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self):
        """
        Fetch the PublishedTrackInstance
        

        :returns: The fetched PublishedTrackInstance
        :rtype: twilio.rest.video.v1.room.participant.published_track.PublishedTrackInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.PublishedTrackInstance {}>'.format(context)


