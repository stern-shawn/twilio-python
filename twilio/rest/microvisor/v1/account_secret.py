r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Microvisor
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


class AccountSecretList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the AccountSecretList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.microvisor.v1.account_secret.AccountSecretList
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Secrets'.format(**self._solution)
        
        
    
    
    
    
    def create(self, key, value):
        """
        Create the AccountSecretInstance

        :param str key: The secret key; up to 100 characters.
        :param str value: The secret value; up to 4096 characters.
        
        :returns: The created AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        """
        data = values.of({ 
            'Key': key,
            'Value': value,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return AccountSecretInstance(self._version, payload)

    async def create_async(self, key, value):
        """
        Asynchronous coroutine to create the AccountSecretInstance

        :param str key: The secret key; up to 100 characters.
        :param str value: The secret value; up to 4096 characters.
        
        :returns: The created AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        """
        data = values.of({ 
            'Key': key,
            'Value': value,
        })
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data,)

        return AccountSecretInstance(self._version, payload)
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams AccountSecretInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.microvisor.v1.account_secret.AccountSecretInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronous coroutine that streams AccountSecretInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.microvisor.v1.account_secret.AccountSecretInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists AccountSecretInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.microvisor.v1.account_secret.AccountSecretInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronous coroutine that lists AccountSecretInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.microvisor.v1.account_secret.AccountSecretInstance]
        """
        return list(await self.stream_async(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of AccountSecretInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return AccountSecretPage(self._version, response, self._solution)

    async def page_async(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronous coroutine that retrieve a single page of AccountSecretInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return AccountSecretPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AccountSecretInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return AccountSecretPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronous coroutine that retrieve a specific page of AccountSecretInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return AccountSecretPage(self._version, response, self._solution)


    def get(self, key):
        """
        Constructs a AccountSecretContext
        
        :param key: The secret key; up to 100 characters.
        
        :returns: twilio.rest.microvisor.v1.account_secret.AccountSecretContext
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretContext
        """
        return AccountSecretContext(self._version, key=key)

    def __call__(self, key):
        """
        Constructs a AccountSecretContext
        
        :param key: The secret key; up to 100 characters.
        
        :returns: twilio.rest.microvisor.v1.account_secret.AccountSecretContext
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretContext
        """
        return AccountSecretContext(self._version, key=key)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Microvisor.V1.AccountSecretList>'










class AccountSecretPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the AccountSecretPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.microvisor.v1.account_secret.AccountSecretPage
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AccountSecretInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        """
        return AccountSecretInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Microvisor.V1.AccountSecretPage>'




class AccountSecretContext(InstanceContext):

    def __init__(self, version: Version, key: str):
        """
        Initialize the AccountSecretContext

        :param Version version: Version that contains the resource
        :param key: The secret key; up to 100 characters.

        :returns: twilio.rest.microvisor.v1.account_secret.AccountSecretContext
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'key': key,
        }
        self._uri = '/Secrets/{key}'.format(**self._solution)
        
    
    
    def delete(self):
        """
        Deletes the AccountSecretInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the AccountSecretInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(method='DELETE', uri=self._uri,)
    
    
    def fetch(self):
        """
        Fetch the AccountSecretInstance
        

        :returns: The fetched AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AccountSecretInstance(
            self._version,
            payload,
            key=self._solution['key'],
            
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the AccountSecretInstance
        

        :returns: The fetched AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return AccountSecretInstance(
            self._version,
            payload,
            key=self._solution['key'],
            
        )
    
    
    def update(self, value):
        """
        Update the AccountSecretInstance
        
        :params str value: The secret value; up to 4096 characters.

        :returns: The updated AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        """
        data = values.of({ 
            'Value': value,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return AccountSecretInstance(
            self._version,
            payload,
            key=self._solution['key']
        )

    async def update_async(self, value):
        """
        Asynchronous coroutine to update the AccountSecretInstance
        
        :params str value: The secret value; up to 4096 characters.

        :returns: The updated AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        """
        data = values.of({ 
            'Value': value,
        })
        

        payload = await self._version.update_async(method='POST', uri=self._uri, data=data,)

        return AccountSecretInstance(
            self._version,
            payload,
            key=self._solution['key']
        )
    
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Microvisor.V1.AccountSecretContext {}>'.format(context)

class AccountSecretInstance(InstanceResource):

    def __init__(self, version, payload, key: str=None):
        """
        Initialize the AccountSecretInstance
        :returns: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        """
        super().__init__(version)

        self._properties = { 
            'key': payload.get('key'),
            'date_rotated': deserialize.iso8601_datetime(payload.get('date_rotated')),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'key': key or self._properties['key'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AccountSecretContext for this AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretContext
        """
        if self._context is None:
            self._context = AccountSecretContext(self._version, key=self._solution['key'],)
        return self._context
    
    @property
    def key(self):
        """
        :returns: The secret key; up to 100 characters.
        :rtype: str
        """
        return self._properties['key']
    
    @property
    def date_rotated(self):
        """
        :returns: 
        :rtype: datetime
        """
        return self._properties['date_rotated']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Secret.
        :rtype: str
        """
        return self._properties['url']
    
    
    def delete(self):
        """
        Deletes the AccountSecretInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the AccountSecretInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()
    
    
    def fetch(self):
        """
        Fetch the AccountSecretInstance
        

        :returns: The fetched AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the AccountSecretInstance
        

        :returns: The fetched AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, value):
        """
        Update the AccountSecretInstance
        
        :params str value: The secret value; up to 4096 characters.

        :returns: The updated AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        """
        return self._proxy.update(value=value, )

    async def update_async(self, value):
        """
        Asynchronous coroutine to update the AccountSecretInstance
        
        :params str value: The secret value; up to 4096 characters.

        :returns: The updated AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        """
        return await self._proxy.update_async(value=value, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Microvisor.V1.AccountSecretInstance {}>'.format(context)


