r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Events
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


class EventTypeList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the EventTypeList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.events.v1.event_type.EventTypeList
        :rtype: twilio.rest.events.v1.event_type.EventTypeList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Types'.format(**self._solution)
        
        
    
    
    def stream(self, schema_id=values.unset, limit=None, page_size=None):
        """
        Streams EventTypeInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str schema_id: A string parameter filtering the results to return only the Event Types using a given schema.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.events.v1.event_type.EventTypeInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            schema_id=schema_id,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, schema_id=values.unset, limit=None, page_size=None):
        """
        Asynchronous coroutine that streams EventTypeInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str schema_id: A string parameter filtering the results to return only the Event Types using a given schema.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.events.v1.event_type.EventTypeInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            schema_id=schema_id,
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, schema_id=values.unset, limit=None, page_size=None):
        """
        Lists EventTypeInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str schema_id: A string parameter filtering the results to return only the Event Types using a given schema.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.events.v1.event_type.EventTypeInstance]
        """
        return list(self.stream(
            schema_id=schema_id,
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, schema_id=values.unset, limit=None, page_size=None):
        """
        Asynchronous coroutine that lists EventTypeInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str schema_id: A string parameter filtering the results to return only the Event Types using a given schema.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.events.v1.event_type.EventTypeInstance]
        """
        return list(await self.stream_async(
            schema_id=schema_id,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, schema_id=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of EventTypeInstance records from the API.
        Request is executed immediately
        
        :param str schema_id: A string parameter filtering the results to return only the Event Types using a given schema.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of EventTypeInstance
        :rtype: twilio.rest.events.v1.event_type.EventTypePage
        """
        data = values.of({ 
            'SchemaId': schema_id,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return EventTypePage(self._version, response, self._solution)

    async def page_async(self, schema_id=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronous coroutine that retrieve a single page of EventTypeInstance records from the API.
        Request is executed immediately
        
        :param str schema_id: A string parameter filtering the results to return only the Event Types using a given schema.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of EventTypeInstance
        :rtype: twilio.rest.events.v1.event_type.EventTypePage
        """
        data = values.of({ 
            'SchemaId': schema_id,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return EventTypePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of EventTypeInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of EventTypeInstance
        :rtype: twilio.rest.events.v1.event_type.EventTypePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return EventTypePage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronous coroutine that retrieve a specific page of EventTypeInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of EventTypeInstance
        :rtype: twilio.rest.events.v1.event_type.EventTypePage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return EventTypePage(self._version, response, self._solution)


    def get(self, type):
        """
        Constructs a EventTypeContext
        
        :param type: A string that uniquely identifies this Event Type.
        
        :returns: twilio.rest.events.v1.event_type.EventTypeContext
        :rtype: twilio.rest.events.v1.event_type.EventTypeContext
        """
        return EventTypeContext(self._version, type=type)

    def __call__(self, type):
        """
        Constructs a EventTypeContext
        
        :param type: A string that uniquely identifies this Event Type.
        
        :returns: twilio.rest.events.v1.event_type.EventTypeContext
        :rtype: twilio.rest.events.v1.event_type.EventTypeContext
        """
        return EventTypeContext(self._version, type=type)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Events.V1.EventTypeList>'




class EventTypePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the EventTypePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.events.v1.event_type.EventTypePage
        :rtype: twilio.rest.events.v1.event_type.EventTypePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of EventTypeInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.events.v1.event_type.EventTypeInstance
        :rtype: twilio.rest.events.v1.event_type.EventTypeInstance
        """
        return EventTypeInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Events.V1.EventTypePage>'




class EventTypeContext(InstanceContext):

    def __init__(self, version: Version, type: str):
        """
        Initialize the EventTypeContext

        :param Version version: Version that contains the resource
        :param type: A string that uniquely identifies this Event Type.

        :returns: twilio.rest.events.v1.event_type.EventTypeContext
        :rtype: twilio.rest.events.v1.event_type.EventTypeContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'type': type,
        }
        self._uri = '/Types/{type}'.format(**self._solution)
        
    
    
    def fetch(self):
        """
        Fetch the EventTypeInstance
        

        :returns: The fetched EventTypeInstance
        :rtype: twilio.rest.events.v1.event_type.EventTypeInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return EventTypeInstance(
            self._version,
            payload,
            type=self._solution['type'],
            
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the EventTypeInstance
        

        :returns: The fetched EventTypeInstance
        :rtype: twilio.rest.events.v1.event_type.EventTypeInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return EventTypeInstance(
            self._version,
            payload,
            type=self._solution['type'],
            
        )
    
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Events.V1.EventTypeContext {}>'.format(context)

class EventTypeInstance(InstanceResource):

    def __init__(self, version, payload, type: str=None):
        """
        Initialize the EventTypeInstance
        :returns: twilio.rest.events.v1.event_type.EventTypeInstance
        :rtype: twilio.rest.events.v1.event_type.EventTypeInstance
        """
        super().__init__(version)

        self._properties = { 
            'type': payload.get('type'),
            'schema_id': payload.get('schema_id'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'description': payload.get('description'),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'type': type or self._properties['type'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: EventTypeContext for this EventTypeInstance
        :rtype: twilio.rest.events.v1.event_type.EventTypeContext
        """
        if self._context is None:
            self._context = EventTypeContext(self._version, type=self._solution['type'],)
        return self._context
    
    @property
    def type(self):
        """
        :returns: A string that uniquely identifies this Event Type.
        :rtype: str
        """
        return self._properties['type']
    
    @property
    def schema_id(self):
        """
        :returns: A string that uniquely identifies the Schema this Event Type adheres to.
        :rtype: str
        """
        return self._properties['schema_id']
    
    @property
    def date_created(self):
        """
        :returns: The date that this Event Type was created, given in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date that this Event Type was updated, given in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def description(self):
        """
        :returns: A human readable description for this Event Type.
        :rtype: str
        """
        return self._properties['description']
    
    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['links']
    
    
    def fetch(self):
        """
        Fetch the EventTypeInstance
        

        :returns: The fetched EventTypeInstance
        :rtype: twilio.rest.events.v1.event_type.EventTypeInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the EventTypeInstance
        

        :returns: The fetched EventTypeInstance
        :rtype: twilio.rest.events.v1.event_type.EventTypeInstance
        """
        return await self._proxy.fetch_async()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Events.V1.EventTypeInstance {}>'.format(context)


