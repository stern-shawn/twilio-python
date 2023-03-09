r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trusthub
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


class TrustProductsChannelEndpointAssignmentList(ListResource):

    def __init__(self, version: Version, trust_product_sid: str):
        """
        Initialize the TrustProductsChannelEndpointAssignmentList

        :param Version version: Version that contains the resource
        :param trust_product_sid: The unique string that we created to identify the CustomerProfile resource.
        
        :returns: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentList
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'trust_product_sid': trust_product_sid,  }
        self._uri = '/TrustProducts/{trust_product_sid}/ChannelEndpointAssignments'.format(**self._solution)
        
        
    
    
    
    def create(self, channel_endpoint_type, channel_endpoint_sid):
        """
        Create the TrustProductsChannelEndpointAssignmentInstance

        :param str channel_endpoint_type: The type of channel endpoint. eg: phone-number
        :param str channel_endpoint_sid: The SID of an channel endpoint
        
        :returns: The created TrustProductsChannelEndpointAssignmentInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentInstance
        """
        data = values.of({ 
            'ChannelEndpointType': channel_endpoint_type,
            'ChannelEndpointSid': channel_endpoint_sid,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return TrustProductsChannelEndpointAssignmentInstance(self._version, payload, trust_product_sid=self._solution['trust_product_sid'])

    async def create_async(self, channel_endpoint_type, channel_endpoint_sid):
        """
        Asynchronous coroutine to create the TrustProductsChannelEndpointAssignmentInstance

        :param str channel_endpoint_type: The type of channel endpoint. eg: phone-number
        :param str channel_endpoint_sid: The SID of an channel endpoint
        
        :returns: The created TrustProductsChannelEndpointAssignmentInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentInstance
        """
        data = values.of({ 
            'ChannelEndpointType': channel_endpoint_type,
            'ChannelEndpointSid': channel_endpoint_sid,
        })
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data,)

        return TrustProductsChannelEndpointAssignmentInstance(self._version, payload, trust_product_sid=self._solution['trust_product_sid'])
    
    
    def stream(self, channel_endpoint_sid=values.unset, channel_endpoint_sids=values.unset, limit=None, page_size=None):
        """
        Streams TrustProductsChannelEndpointAssignmentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str channel_endpoint_sid: The SID of an channel endpoint
        :param str channel_endpoint_sids: comma separated list of channel endpoint sids
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            channel_endpoint_sid=channel_endpoint_sid,
            channel_endpoint_sids=channel_endpoint_sids,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, channel_endpoint_sid=values.unset, channel_endpoint_sids=values.unset, limit=None, page_size=None):
        """
        Asynchronous coroutine that streams TrustProductsChannelEndpointAssignmentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str channel_endpoint_sid: The SID of an channel endpoint
        :param str channel_endpoint_sids: comma separated list of channel endpoint sids
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            channel_endpoint_sid=channel_endpoint_sid,
            channel_endpoint_sids=channel_endpoint_sids,
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, channel_endpoint_sid=values.unset, channel_endpoint_sids=values.unset, limit=None, page_size=None):
        """
        Lists TrustProductsChannelEndpointAssignmentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str channel_endpoint_sid: The SID of an channel endpoint
        :param str channel_endpoint_sids: comma separated list of channel endpoint sids
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentInstance]
        """
        return list(self.stream(
            channel_endpoint_sid=channel_endpoint_sid,
            channel_endpoint_sids=channel_endpoint_sids,
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, channel_endpoint_sid=values.unset, channel_endpoint_sids=values.unset, limit=None, page_size=None):
        """
        Asynchronous coroutine that lists TrustProductsChannelEndpointAssignmentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str channel_endpoint_sid: The SID of an channel endpoint
        :param str channel_endpoint_sids: comma separated list of channel endpoint sids
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentInstance]
        """
        return list(await self.stream_async(
            channel_endpoint_sid=channel_endpoint_sid,
            channel_endpoint_sids=channel_endpoint_sids,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, channel_endpoint_sid=values.unset, channel_endpoint_sids=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of TrustProductsChannelEndpointAssignmentInstance records from the API.
        Request is executed immediately
        
        :param str channel_endpoint_sid: The SID of an channel endpoint
        :param str channel_endpoint_sids: comma separated list of channel endpoint sids
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TrustProductsChannelEndpointAssignmentInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentPage
        """
        data = values.of({ 
            'ChannelEndpointSid': channel_endpoint_sid,
            'ChannelEndpointSids': channel_endpoint_sids,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return TrustProductsChannelEndpointAssignmentPage(self._version, response, self._solution)

    async def page_async(self, channel_endpoint_sid=values.unset, channel_endpoint_sids=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronous coroutine that retrieve a single page of TrustProductsChannelEndpointAssignmentInstance records from the API.
        Request is executed immediately
        
        :param str channel_endpoint_sid: The SID of an channel endpoint
        :param str channel_endpoint_sids: comma separated list of channel endpoint sids
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TrustProductsChannelEndpointAssignmentInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentPage
        """
        data = values.of({ 
            'ChannelEndpointSid': channel_endpoint_sid,
            'ChannelEndpointSids': channel_endpoint_sids,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return TrustProductsChannelEndpointAssignmentPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of TrustProductsChannelEndpointAssignmentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TrustProductsChannelEndpointAssignmentInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return TrustProductsChannelEndpointAssignmentPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronous coroutine that retrieve a specific page of TrustProductsChannelEndpointAssignmentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TrustProductsChannelEndpointAssignmentInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return TrustProductsChannelEndpointAssignmentPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a TrustProductsChannelEndpointAssignmentContext
        
        :param sid: The unique string that we created to identify the resource.
        
        :returns: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentContext
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentContext
        """
        return TrustProductsChannelEndpointAssignmentContext(self._version, trust_product_sid=self._solution['trust_product_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a TrustProductsChannelEndpointAssignmentContext
        
        :param sid: The unique string that we created to identify the resource.
        
        :returns: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentContext
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentContext
        """
        return TrustProductsChannelEndpointAssignmentContext(self._version, trust_product_sid=self._solution['trust_product_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trusthub.V1.TrustProductsChannelEndpointAssignmentList>'








class TrustProductsChannelEndpointAssignmentPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the TrustProductsChannelEndpointAssignmentPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentPage
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of TrustProductsChannelEndpointAssignmentInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentInstance
        """
        return TrustProductsChannelEndpointAssignmentInstance(self._version, payload, trust_product_sid=self._solution['trust_product_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trusthub.V1.TrustProductsChannelEndpointAssignmentPage>'




class TrustProductsChannelEndpointAssignmentContext(InstanceContext):

    def __init__(self, version: Version, trust_product_sid: str, sid: str):
        """
        Initialize the TrustProductsChannelEndpointAssignmentContext

        :param Version version: Version that contains the resource
        :param trust_product_sid: The unique string that we created to identify the CustomerProfile resource.:param sid: The unique string that we created to identify the resource.

        :returns: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentContext
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'trust_product_sid': trust_product_sid,
            'sid': sid,
        }
        self._uri = '/TrustProducts/{trust_product_sid}/ChannelEndpointAssignments/{sid}'.format(**self._solution)
        
    
    
    def delete(self):
        """
        Deletes the TrustProductsChannelEndpointAssignmentInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the TrustProductsChannelEndpointAssignmentInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(method='DELETE', uri=self._uri,)
    
    
    def fetch(self):
        """
        Fetch the TrustProductsChannelEndpointAssignmentInstance
        

        :returns: The fetched TrustProductsChannelEndpointAssignmentInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return TrustProductsChannelEndpointAssignmentInstance(
            self._version,
            payload,
            trust_product_sid=self._solution['trust_product_sid'],
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the TrustProductsChannelEndpointAssignmentInstance
        

        :returns: The fetched TrustProductsChannelEndpointAssignmentInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return TrustProductsChannelEndpointAssignmentInstance(
            self._version,
            payload,
            trust_product_sid=self._solution['trust_product_sid'],
            sid=self._solution['sid'],
            
        )
    
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trusthub.V1.TrustProductsChannelEndpointAssignmentContext {}>'.format(context)

class TrustProductsChannelEndpointAssignmentInstance(InstanceResource):

    def __init__(self, version, payload, trust_product_sid: str, sid: str=None):
        """
        Initialize the TrustProductsChannelEndpointAssignmentInstance
        :returns: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'trust_product_sid': payload.get('trust_product_sid'),
            'account_sid': payload.get('account_sid'),
            'channel_endpoint_type': payload.get('channel_endpoint_type'),
            'channel_endpoint_sid': payload.get('channel_endpoint_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'trust_product_sid': trust_product_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: TrustProductsChannelEndpointAssignmentContext for this TrustProductsChannelEndpointAssignmentInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentContext
        """
        if self._context is None:
            self._context = TrustProductsChannelEndpointAssignmentContext(self._version, trust_product_sid=self._solution['trust_product_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Item Assignment resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def trust_product_sid(self):
        """
        :returns: The unique string that we created to identify the CustomerProfile resource.
        :rtype: str
        """
        return self._properties['trust_product_sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Item Assignment resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def channel_endpoint_type(self):
        """
        :returns: The type of channel endpoint. eg: phone-number
        :rtype: str
        """
        return self._properties['channel_endpoint_type']
    
    @property
    def channel_endpoint_sid(self):
        """
        :returns: The SID of an channel endpoint
        :rtype: str
        """
        return self._properties['channel_endpoint_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Identity resource.
        :rtype: str
        """
        return self._properties['url']
    
    
    def delete(self):
        """
        Deletes the TrustProductsChannelEndpointAssignmentInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the TrustProductsChannelEndpointAssignmentInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()
    
    
    def fetch(self):
        """
        Fetch the TrustProductsChannelEndpointAssignmentInstance
        

        :returns: The fetched TrustProductsChannelEndpointAssignmentInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the TrustProductsChannelEndpointAssignmentInstance
        

        :returns: The fetched TrustProductsChannelEndpointAssignmentInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment.TrustProductsChannelEndpointAssignmentInstance
        """
        return await self._proxy.fetch_async()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trusthub.V1.TrustProductsChannelEndpointAssignmentInstance {}>'.format(context)


