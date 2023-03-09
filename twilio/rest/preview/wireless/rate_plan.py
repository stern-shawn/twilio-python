r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
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


class RatePlanList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the RatePlanList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.preview.wireless.rate_plan.RatePlanList
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/RatePlans'.format(**self._solution)
        
        
    
    
    
    
    def create(self, unique_name=values.unset, friendly_name=values.unset, data_enabled=values.unset, data_limit=values.unset, data_metering=values.unset, messaging_enabled=values.unset, voice_enabled=values.unset, commands_enabled=values.unset, national_roaming_enabled=values.unset, international_roaming=values.unset):
        """
        Create the RatePlanInstance

        :param str unique_name: 
        :param str friendly_name: 
        :param bool data_enabled: 
        :param int data_limit: 
        :param str data_metering: 
        :param bool messaging_enabled: 
        :param bool voice_enabled: 
        :param bool commands_enabled: 
        :param bool national_roaming_enabled: 
        :param list[str] international_roaming: 
        
        :returns: The created RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        """
        data = values.of({ 
            'UniqueName': unique_name,
            'FriendlyName': friendly_name,
            'DataEnabled': data_enabled,
            'DataLimit': data_limit,
            'DataMetering': data_metering,
            'MessagingEnabled': messaging_enabled,
            'VoiceEnabled': voice_enabled,
            'CommandsEnabled': commands_enabled,
            'NationalRoamingEnabled': national_roaming_enabled,
            'InternationalRoaming': serialize.map(international_roaming, lambda e: e),
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return RatePlanInstance(self._version, payload)

    async def create_async(self, unique_name=values.unset, friendly_name=values.unset, data_enabled=values.unset, data_limit=values.unset, data_metering=values.unset, messaging_enabled=values.unset, voice_enabled=values.unset, commands_enabled=values.unset, national_roaming_enabled=values.unset, international_roaming=values.unset):
        """
        Asynchronous coroutine to create the RatePlanInstance

        :param str unique_name: 
        :param str friendly_name: 
        :param bool data_enabled: 
        :param int data_limit: 
        :param str data_metering: 
        :param bool messaging_enabled: 
        :param bool voice_enabled: 
        :param bool commands_enabled: 
        :param bool national_roaming_enabled: 
        :param list[str] international_roaming: 
        
        :returns: The created RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        """
        data = values.of({ 
            'UniqueName': unique_name,
            'FriendlyName': friendly_name,
            'DataEnabled': data_enabled,
            'DataLimit': data_limit,
            'DataMetering': data_metering,
            'MessagingEnabled': messaging_enabled,
            'VoiceEnabled': voice_enabled,
            'CommandsEnabled': commands_enabled,
            'NationalRoamingEnabled': national_roaming_enabled,
            'InternationalRoaming': serialize.map(international_roaming, lambda e: e),
        })
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data,)

        return RatePlanInstance(self._version, payload)
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams RatePlanInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.preview.wireless.rate_plan.RatePlanInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronous coroutine that streams RatePlanInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.preview.wireless.rate_plan.RatePlanInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists RatePlanInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.wireless.rate_plan.RatePlanInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronous coroutine that lists RatePlanInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.wireless.rate_plan.RatePlanInstance]
        """
        return list(await self.stream_async(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of RatePlanInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return RatePlanPage(self._version, response, self._solution)

    async def page_async(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronous coroutine that retrieve a single page of RatePlanInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return RatePlanPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of RatePlanInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return RatePlanPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronous coroutine that retrieve a specific page of RatePlanInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return RatePlanPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a RatePlanContext
        
        :param sid: 
        
        :returns: twilio.rest.preview.wireless.rate_plan.RatePlanContext
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanContext
        """
        return RatePlanContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a RatePlanContext
        
        :param sid: 
        
        :returns: twilio.rest.preview.wireless.rate_plan.RatePlanContext
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanContext
        """
        return RatePlanContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Wireless.RatePlanList>'










class RatePlanPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the RatePlanPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.wireless.rate_plan.RatePlanPage
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of RatePlanInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        """
        return RatePlanInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Wireless.RatePlanPage>'




class RatePlanContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the RatePlanContext

        :param Version version: Version that contains the resource
        :param sid: 

        :returns: twilio.rest.preview.wireless.rate_plan.RatePlanContext
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/RatePlans/{sid}'.format(**self._solution)
        
    
    
    def delete(self):
        """
        Deletes the RatePlanInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the RatePlanInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(method='DELETE', uri=self._uri,)
    
    
    def fetch(self):
        """
        Fetch the RatePlanInstance
        

        :returns: The fetched RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return RatePlanInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the RatePlanInstance
        

        :returns: The fetched RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return RatePlanInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
    
    
    def update(self, unique_name=values.unset, friendly_name=values.unset):
        """
        Update the RatePlanInstance
        
        :params str unique_name: 
        :params str friendly_name: 

        :returns: The updated RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        """
        data = values.of({ 
            'UniqueName': unique_name,
            'FriendlyName': friendly_name,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return RatePlanInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )

    async def update_async(self, unique_name=values.unset, friendly_name=values.unset):
        """
        Asynchronous coroutine to update the RatePlanInstance
        
        :params str unique_name: 
        :params str friendly_name: 

        :returns: The updated RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        """
        data = values.of({ 
            'UniqueName': unique_name,
            'FriendlyName': friendly_name,
        })
        

        payload = await self._version.update_async(method='POST', uri=self._uri, data=data,)

        return RatePlanInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
    
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Wireless.RatePlanContext {}>'.format(context)

class RatePlanInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the RatePlanInstance
        :returns: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'unique_name': payload.get('unique_name'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'data_enabled': payload.get('data_enabled'),
            'data_metering': payload.get('data_metering'),
            'data_limit': deserialize.integer(payload.get('data_limit')),
            'messaging_enabled': payload.get('messaging_enabled'),
            'voice_enabled': payload.get('voice_enabled'),
            'national_roaming_enabled': payload.get('national_roaming_enabled'),
            'international_roaming': payload.get('international_roaming'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RatePlanContext for this RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanContext
        """
        if self._context is None:
            self._context = RatePlanContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def unique_name(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['unique_name']
    
    @property
    def account_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def data_enabled(self):
        """
        :returns: 
        :rtype: bool
        """
        return self._properties['data_enabled']
    
    @property
    def data_metering(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['data_metering']
    
    @property
    def data_limit(self):
        """
        :returns: 
        :rtype: int
        """
        return self._properties['data_limit']
    
    @property
    def messaging_enabled(self):
        """
        :returns: 
        :rtype: bool
        """
        return self._properties['messaging_enabled']
    
    @property
    def voice_enabled(self):
        """
        :returns: 
        :rtype: bool
        """
        return self._properties['voice_enabled']
    
    @property
    def national_roaming_enabled(self):
        """
        :returns: 
        :rtype: bool
        """
        return self._properties['national_roaming_enabled']
    
    @property
    def international_roaming(self):
        """
        :returns: 
        :rtype: list[str]
        """
        return self._properties['international_roaming']
    
    @property
    def date_created(self):
        """
        :returns: 
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: 
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    
    def delete(self):
        """
        Deletes the RatePlanInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the RatePlanInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()
    
    
    def fetch(self):
        """
        Fetch the RatePlanInstance
        

        :returns: The fetched RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the RatePlanInstance
        

        :returns: The fetched RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, unique_name=values.unset, friendly_name=values.unset):
        """
        Update the RatePlanInstance
        
        :params str unique_name: 
        :params str friendly_name: 

        :returns: The updated RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        """
        return self._proxy.update(unique_name=unique_name, friendly_name=friendly_name, )

    async def update_async(self, unique_name=values.unset, friendly_name=values.unset):
        """
        Asynchronous coroutine to update the RatePlanInstance
        
        :params str unique_name: 
        :params str friendly_name: 

        :returns: The updated RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        """
        return await self._proxy.update_async(unique_name=unique_name, friendly_name=friendly_name, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Wireless.RatePlanInstance {}>'.format(context)


