r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Serverless
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
from twilio.rest.serverless.v1.service.function.function_version.function_version_content import FunctionVersionContentList


class FunctionVersionList(ListResource):

    def __init__(self, version: Version, service_sid: str, function_sid: str):
        """
        Initialize the FunctionVersionList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to read the Function Version resources from.
        :param function_sid: The SID of the function that is the parent of the Function Version resources to read.
        
        :returns: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionList
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'function_sid': function_sid,  }
        self._uri = '/Services/{service_sid}/Functions/{function_sid}/Versions'.format(**self._solution)
        
        
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams FunctionVersionInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.serverless.v1.service.function.function_version.FunctionVersionInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronous coroutine that streams FunctionVersionInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.serverless.v1.service.function.function_version.FunctionVersionInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists FunctionVersionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.serverless.v1.service.function.function_version.FunctionVersionInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronous coroutine that lists FunctionVersionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.serverless.v1.service.function.function_version.FunctionVersionInstance]
        """
        return list(await self.stream_async(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of FunctionVersionInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FunctionVersionInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return FunctionVersionPage(self._version, response, self._solution)

    async def page_async(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronous coroutine that retrieve a single page of FunctionVersionInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FunctionVersionInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return FunctionVersionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FunctionVersionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FunctionVersionInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return FunctionVersionPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronous coroutine that retrieve a specific page of FunctionVersionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FunctionVersionInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return FunctionVersionPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a FunctionVersionContext
        
        :param sid: The SID of the Function Version resource to fetch.
        
        :returns: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionContext
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionContext
        """
        return FunctionVersionContext(self._version, service_sid=self._solution['service_sid'], function_sid=self._solution['function_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a FunctionVersionContext
        
        :param sid: The SID of the Function Version resource to fetch.
        
        :returns: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionContext
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionContext
        """
        return FunctionVersionContext(self._version, service_sid=self._solution['service_sid'], function_sid=self._solution['function_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.FunctionVersionList>'




class FunctionVersionPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the FunctionVersionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionPage
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FunctionVersionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionInstance
        """
        return FunctionVersionInstance(self._version, payload, service_sid=self._solution['service_sid'], function_sid=self._solution['function_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.FunctionVersionPage>'




class FunctionVersionContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, function_sid: str, sid: str):
        """
        Initialize the FunctionVersionContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the Function Version resource from.:param function_sid: The SID of the function that is the parent of the Function Version resource to fetch.:param sid: The SID of the Function Version resource to fetch.

        :returns: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionContext
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'function_sid': function_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Functions/{function_sid}/Versions/{sid}'.format(**self._solution)
        
        self._function_version_content = None
    
    
    def fetch(self):
        """
        Fetch the FunctionVersionInstance
        

        :returns: The fetched FunctionVersionInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return FunctionVersionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            function_sid=self._solution['function_sid'],
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the FunctionVersionInstance
        

        :returns: The fetched FunctionVersionInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return FunctionVersionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            function_sid=self._solution['function_sid'],
            sid=self._solution['sid'],
            
        )
    
    
    @property
    def function_version_content(self):
        """
        Access the function_version_content

        :returns: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionContentList
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionContentList
        """
        if self._function_version_content is None:
            self._function_version_content = FunctionVersionContentList(self._version, self._solution['service_sid'], self._solution['function_sid'], self._solution['sid'],
            )
        return self._function_version_content
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.FunctionVersionContext {}>'.format(context)

class FunctionVersionInstance(InstanceResource):

    class Visibility(object):
        PUBLIC = "public"
        PRIVATE = "private"
        PROTECTED = "protected"

    def __init__(self, version, payload, service_sid: str, function_sid: str, sid: str=None):
        """
        Initialize the FunctionVersionInstance
        :returns: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'function_sid': payload.get('function_sid'),
            'path': payload.get('path'),
            'visibility': payload.get('visibility'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'function_sid': function_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FunctionVersionContext for this FunctionVersionInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionContext
        """
        if self._context is None:
            self._context = FunctionVersionContext(self._version, service_sid=self._solution['service_sid'], function_sid=self._solution['function_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Function Version resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Function Version resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: The SID of the Service that the Function Version resource is associated with.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def function_sid(self):
        """
        :returns: The SID of the Function resource that is the parent of the Function Version resource.
        :rtype: str
        """
        return self._properties['function_sid']
    
    @property
    def path(self):
        """
        :returns: The URL-friendly string by which the Function Version resource can be referenced. It can be a maximum of 255 characters. All paths begin with a forward slash ('/'). If a Function Version creation request is submitted with a path not containing a leading slash, the path will automatically be prepended with one.
        :rtype: str
        """
        return self._properties['path']
    
    @property
    def visibility(self):
        """
        :returns: 
        :rtype: FunctionVersionInstance.Visibility
        """
        return self._properties['visibility']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the Function Version resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Function Version resource.
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
        Fetch the FunctionVersionInstance
        

        :returns: The fetched FunctionVersionInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the FunctionVersionInstance
        

        :returns: The fetched FunctionVersionInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionInstance
        """
        return await self._proxy.fetch_async()
    
    @property
    def function_version_content(self):
        """
        Access the function_version_content

        :returns: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionContentList
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionContentList
        """
        return self._proxy.function_version_content
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.FunctionVersionInstance {}>'.format(context)


