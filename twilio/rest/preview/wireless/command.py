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


class CommandList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the CommandList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.preview.wireless.command.CommandList
        :rtype: twilio.rest.preview.wireless.command.CommandList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Commands'.format(**self._solution)
        
        
    
    
    def create(self, command, device=values.unset, sim=values.unset, callback_method=values.unset, callback_url=values.unset, command_mode=values.unset, include_sid=values.unset):
        """
        Create the CommandInstance

        :param str command: 
        :param str device: 
        :param str sim: 
        :param str callback_method: 
        :param str callback_url: 
        :param str command_mode: 
        :param str include_sid: 
        
        :returns: The created CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandInstance
        """
        data = values.of({ 
            'Command': command,
            'Device': device,
            'Sim': sim,
            'CallbackMethod': callback_method,
            'CallbackUrl': callback_url,
            'CommandMode': command_mode,
            'IncludeSid': include_sid,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return CommandInstance(self._version, payload)

    async def create_async(self, command, device=values.unset, sim=values.unset, callback_method=values.unset, callback_url=values.unset, command_mode=values.unset, include_sid=values.unset):
        """
        Asynchronous coroutine to create the CommandInstance

        :param str command: 
        :param str device: 
        :param str sim: 
        :param str callback_method: 
        :param str callback_url: 
        :param str command_mode: 
        :param str include_sid: 
        
        :returns: The created CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandInstance
        """
        data = values.of({ 
            'Command': command,
            'Device': device,
            'Sim': sim,
            'CallbackMethod': callback_method,
            'CallbackUrl': callback_url,
            'CommandMode': command_mode,
            'IncludeSid': include_sid,
        })
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data,)

        return CommandInstance(self._version, payload)
    
    
    def stream(self, device=values.unset, sim=values.unset, status=values.unset, direction=values.unset, limit=None, page_size=None):
        """
        Streams CommandInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str device: 
        :param str sim: 
        :param str status: 
        :param str direction: 
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.wireless.command.CommandInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            device=device,
            sim=sim,
            status=status,
            direction=direction,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, device=values.unset, sim=values.unset, status=values.unset, direction=values.unset, limit=None, page_size=None):
        """
        Asynchronous coroutine that streams CommandInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str device: 
        :param str sim: 
        :param str status: 
        :param str direction: 
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.wireless.command.CommandInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            device=device,
            sim=sim,
            status=status,
            direction=direction,
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, device=values.unset, sim=values.unset, status=values.unset, direction=values.unset, limit=None, page_size=None):
        """
        Lists CommandInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str device: 
        :param str sim: 
        :param str status: 
        :param str direction: 
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.wireless.command.CommandInstance]
        """
        return list(self.stream(
            device=device,
            sim=sim,
            status=status,
            direction=direction,
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, device=values.unset, sim=values.unset, status=values.unset, direction=values.unset, limit=None, page_size=None):
        """
        Asynchronous coroutine that lists CommandInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str device: 
        :param str sim: 
        :param str status: 
        :param str direction: 
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.wireless.command.CommandInstance]
        """
        return list(await self.stream_async(
            device=device,
            sim=sim,
            status=status,
            direction=direction,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, device=values.unset, sim=values.unset, status=values.unset, direction=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of CommandInstance records from the API.
        Request is executed immediately
        
        :param str device: 
        :param str sim: 
        :param str status: 
        :param str direction: 
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandPage
        """
        data = values.of({ 
            'Device': device,
            'Sim': sim,
            'Status': status,
            'Direction': direction,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return CommandPage(self._version, response, self._solution)

    async def page_async(self, device=values.unset, sim=values.unset, status=values.unset, direction=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronous coroutine that retrieve a single page of CommandInstance records from the API.
        Request is executed immediately
        
        :param str device: 
        :param str sim: 
        :param str status: 
        :param str direction: 
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandPage
        """
        data = values.of({ 
            'Device': device,
            'Sim': sim,
            'Status': status,
            'Direction': direction,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return CommandPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CommandInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return CommandPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronous coroutine that retrieve a specific page of CommandInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return CommandPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a CommandContext
        
        :param sid: 
        
        :returns: twilio.rest.preview.wireless.command.CommandContext
        :rtype: twilio.rest.preview.wireless.command.CommandContext
        """
        return CommandContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a CommandContext
        
        :param sid: 
        
        :returns: twilio.rest.preview.wireless.command.CommandContext
        :rtype: twilio.rest.preview.wireless.command.CommandContext
        """
        return CommandContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Wireless.CommandList>'






class CommandPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the CommandPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.wireless.command.CommandPage
        :rtype: twilio.rest.preview.wireless.command.CommandPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CommandInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.wireless.command.CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandInstance
        """
        return CommandInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Wireless.CommandPage>'




class CommandContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the CommandContext

        :param Version version: Version that contains the resource
        :param sid: 

        :returns: twilio.rest.preview.wireless.command.CommandContext
        :rtype: twilio.rest.preview.wireless.command.CommandContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Commands/{sid}'.format(**self._solution)
        
    
    
    def fetch(self):
        """
        Fetch the CommandInstance
        

        :returns: The fetched CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return CommandInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the CommandInstance
        

        :returns: The fetched CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return CommandInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
    
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Wireless.CommandContext {}>'.format(context)

class CommandInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the CommandInstance
        :returns: twilio.rest.preview.wireless.command.CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'device_sid': payload.get('device_sid'),
            'sim_sid': payload.get('sim_sid'),
            'command': payload.get('command'),
            'command_mode': payload.get('command_mode'),
            'status': payload.get('status'),
            'direction': payload.get('direction'),
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

        :returns: CommandContext for this CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandContext
        """
        if self._context is None:
            self._context = CommandContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def device_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['device_sid']
    
    @property
    def sim_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['sim_sid']
    
    @property
    def command(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['command']
    
    @property
    def command_mode(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['command_mode']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['status']
    
    @property
    def direction(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['direction']
    
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
    
    
    def fetch(self):
        """
        Fetch the CommandInstance
        

        :returns: The fetched CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the CommandInstance
        

        :returns: The fetched CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandInstance
        """
        return await self._proxy.fetch_async()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Wireless.CommandInstance {}>'.format(context)


