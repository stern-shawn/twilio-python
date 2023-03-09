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
from twilio.rest.serverless.v1.service.asset.asset_version import AssetVersionList


class AssetList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the AssetList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to read the Asset resources from.
        
        :returns: twilio.rest.serverless.v1.service.asset.AssetList
        :rtype: twilio.rest.serverless.v1.service.asset.AssetList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/{service_sid}/Assets'.format(**self._solution)
        
        
    
    
    
    
    def create(self, friendly_name):
        """
        Create the AssetInstance

        :param str friendly_name: A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters.
        
        :returns: The created AssetInstance
        :rtype: twilio.rest.serverless.v1.service.asset.AssetInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return AssetInstance(self._version, payload, service_sid=self._solution['service_sid'])

    async def create_async(self, friendly_name):
        """
        Asynchronous coroutine to create the AssetInstance

        :param str friendly_name: A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters.
        
        :returns: The created AssetInstance
        :rtype: twilio.rest.serverless.v1.service.asset.AssetInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
        })
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data,)

        return AssetInstance(self._version, payload, service_sid=self._solution['service_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams AssetInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.serverless.v1.service.asset.AssetInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronous coroutine that streams AssetInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.serverless.v1.service.asset.AssetInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists AssetInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.serverless.v1.service.asset.AssetInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronous coroutine that lists AssetInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.serverless.v1.service.asset.AssetInstance]
        """
        return list(await self.stream_async(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of AssetInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AssetInstance
        :rtype: twilio.rest.serverless.v1.service.asset.AssetPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return AssetPage(self._version, response, self._solution)

    async def page_async(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronous coroutine that retrieve a single page of AssetInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AssetInstance
        :rtype: twilio.rest.serverless.v1.service.asset.AssetPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return AssetPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AssetInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AssetInstance
        :rtype: twilio.rest.serverless.v1.service.asset.AssetPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return AssetPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronous coroutine that retrieve a specific page of AssetInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AssetInstance
        :rtype: twilio.rest.serverless.v1.service.asset.AssetPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return AssetPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a AssetContext
        
        :param sid: The SID that identifies the Asset resource to update.
        
        :returns: twilio.rest.serverless.v1.service.asset.AssetContext
        :rtype: twilio.rest.serverless.v1.service.asset.AssetContext
        """
        return AssetContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a AssetContext
        
        :param sid: The SID that identifies the Asset resource to update.
        
        :returns: twilio.rest.serverless.v1.service.asset.AssetContext
        :rtype: twilio.rest.serverless.v1.service.asset.AssetContext
        """
        return AssetContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.AssetList>'










class AssetPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the AssetPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.serverless.v1.service.asset.AssetPage
        :rtype: twilio.rest.serverless.v1.service.asset.AssetPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AssetInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.serverless.v1.service.asset.AssetInstance
        :rtype: twilio.rest.serverless.v1.service.asset.AssetInstance
        """
        return AssetInstance(self._version, payload, service_sid=self._solution['service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.AssetPage>'




class AssetContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the AssetContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to update the Asset resource from.:param sid: The SID that identifies the Asset resource to update.

        :returns: twilio.rest.serverless.v1.service.asset.AssetContext
        :rtype: twilio.rest.serverless.v1.service.asset.AssetContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Assets/{sid}'.format(**self._solution)
        
        self._asset_versions = None
    
    
    def delete(self):
        """
        Deletes the AssetInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the AssetInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(method='DELETE', uri=self._uri,)
    
    
    def fetch(self):
        """
        Fetch the AssetInstance
        

        :returns: The fetched AssetInstance
        :rtype: twilio.rest.serverless.v1.service.asset.AssetInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AssetInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the AssetInstance
        

        :returns: The fetched AssetInstance
        :rtype: twilio.rest.serverless.v1.service.asset.AssetInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return AssetInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
            
        )
    
    
    def update(self, friendly_name):
        """
        Update the AssetInstance
        
        :params str friendly_name: A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters.

        :returns: The updated AssetInstance
        :rtype: twilio.rest.serverless.v1.service.asset.AssetInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return AssetInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid']
        )

    async def update_async(self, friendly_name):
        """
        Asynchronous coroutine to update the AssetInstance
        
        :params str friendly_name: A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters.

        :returns: The updated AssetInstance
        :rtype: twilio.rest.serverless.v1.service.asset.AssetInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
        })
        

        payload = await self._version.update_async(method='POST', uri=self._uri, data=data,)

        return AssetInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid']
        )
    
    
    @property
    def asset_versions(self):
        """
        Access the asset_versions

        :returns: twilio.rest.serverless.v1.service.asset.AssetVersionList
        :rtype: twilio.rest.serverless.v1.service.asset.AssetVersionList
        """
        if self._asset_versions is None:
            self._asset_versions = AssetVersionList(self._version, self._solution['service_sid'], self._solution['sid'],
            )
        return self._asset_versions
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.AssetContext {}>'.format(context)

class AssetInstance(InstanceResource):

    def __init__(self, version, payload, service_sid: str, sid: str=None):
        """
        Initialize the AssetInstance
        :returns: twilio.rest.serverless.v1.service.asset.AssetInstance
        :rtype: twilio.rest.serverless.v1.service.asset.AssetInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'friendly_name': payload.get('friendly_name'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AssetContext for this AssetInstance
        :rtype: twilio.rest.serverless.v1.service.asset.AssetContext
        """
        if self._context is None:
            self._context = AssetContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Asset resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Asset resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: The SID of the Service that the Asset resource is associated with.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the Asset resource. It can be a maximum of 255 characters.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the Asset resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the Asset resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Asset resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: The URLs of the Asset resource's nested resources.
        :rtype: dict
        """
        return self._properties['links']
    
    
    def delete(self):
        """
        Deletes the AssetInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the AssetInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()
    
    
    def fetch(self):
        """
        Fetch the AssetInstance
        

        :returns: The fetched AssetInstance
        :rtype: twilio.rest.serverless.v1.service.asset.AssetInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the AssetInstance
        

        :returns: The fetched AssetInstance
        :rtype: twilio.rest.serverless.v1.service.asset.AssetInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, friendly_name):
        """
        Update the AssetInstance
        
        :params str friendly_name: A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters.

        :returns: The updated AssetInstance
        :rtype: twilio.rest.serverless.v1.service.asset.AssetInstance
        """
        return self._proxy.update(friendly_name=friendly_name, )

    async def update_async(self, friendly_name):
        """
        Asynchronous coroutine to update the AssetInstance
        
        :params str friendly_name: A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters.

        :returns: The updated AssetInstance
        :rtype: twilio.rest.serverless.v1.service.asset.AssetInstance
        """
        return await self._proxy.update_async(friendly_name=friendly_name, )
    
    @property
    def asset_versions(self):
        """
        Access the asset_versions

        :returns: twilio.rest.serverless.v1.service.asset.AssetVersionList
        :rtype: twilio.rest.serverless.v1.service.asset.AssetVersionList
        """
        return self._proxy.asset_versions
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.AssetInstance {}>'.format(context)


