r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Voice
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


class ConnectionPolicyTargetList(ListResource):

    def __init__(self, version: Version, connection_policy_sid: str):
        """
        Initialize the ConnectionPolicyTargetList

        :param Version version: Version that contains the resource
        :param connection_policy_sid: The SID of the Connection Policy from which to read the Targets.
        
        :returns: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetList
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'connection_policy_sid': connection_policy_sid,  }
        self._uri = '/ConnectionPolicies/{connection_policy_sid}/Targets'.format(**self._solution)
        
        
    
    
    
    
    def create(self, target, friendly_name=values.unset, priority=values.unset, weight=values.unset, enabled=values.unset):
        """
        Create the ConnectionPolicyTargetInstance

        :param str target: The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
        :param str friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :param int priority: The relative importance of the target. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important target.
        :param int weight: The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. Targets with higher values receive more load than those with lower ones with the same priority.
        :param bool enabled: Whether the Target is enabled. The default is `true`.
        
        :returns: The created ConnectionPolicyTargetInstance
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetInstance
        """
        data = values.of({ 
            'Target': target,
            'FriendlyName': friendly_name,
            'Priority': priority,
            'Weight': weight,
            'Enabled': enabled,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return ConnectionPolicyTargetInstance(self._version, payload, connection_policy_sid=self._solution['connection_policy_sid'])

    async def create_async(self, target, friendly_name=values.unset, priority=values.unset, weight=values.unset, enabled=values.unset):
        """
        Asynchronous coroutine to create the ConnectionPolicyTargetInstance

        :param str target: The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
        :param str friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :param int priority: The relative importance of the target. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important target.
        :param int weight: The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. Targets with higher values receive more load than those with lower ones with the same priority.
        :param bool enabled: Whether the Target is enabled. The default is `true`.
        
        :returns: The created ConnectionPolicyTargetInstance
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetInstance
        """
        data = values.of({ 
            'Target': target,
            'FriendlyName': friendly_name,
            'Priority': priority,
            'Weight': weight,
            'Enabled': enabled,
        })
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data,)

        return ConnectionPolicyTargetInstance(self._version, payload, connection_policy_sid=self._solution['connection_policy_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams ConnectionPolicyTargetInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronous coroutine that streams ConnectionPolicyTargetInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ConnectionPolicyTargetInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronous coroutine that lists ConnectionPolicyTargetInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetInstance]
        """
        return list(await self.stream_async(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ConnectionPolicyTargetInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ConnectionPolicyTargetInstance
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ConnectionPolicyTargetPage(self._version, response, self._solution)

    async def page_async(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronous coroutine that retrieve a single page of ConnectionPolicyTargetInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ConnectionPolicyTargetInstance
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return ConnectionPolicyTargetPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ConnectionPolicyTargetInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ConnectionPolicyTargetInstance
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ConnectionPolicyTargetPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronous coroutine that retrieve a specific page of ConnectionPolicyTargetInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ConnectionPolicyTargetInstance
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return ConnectionPolicyTargetPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a ConnectionPolicyTargetContext
        
        :param sid: The unique string that we created to identify the Target resource to update.
        
        :returns: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetContext
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetContext
        """
        return ConnectionPolicyTargetContext(self._version, connection_policy_sid=self._solution['connection_policy_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a ConnectionPolicyTargetContext
        
        :param sid: The unique string that we created to identify the Target resource to update.
        
        :returns: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetContext
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetContext
        """
        return ConnectionPolicyTargetContext(self._version, connection_policy_sid=self._solution['connection_policy_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Voice.V1.ConnectionPolicyTargetList>'










class ConnectionPolicyTargetPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ConnectionPolicyTargetPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetPage
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ConnectionPolicyTargetInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetInstance
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetInstance
        """
        return ConnectionPolicyTargetInstance(self._version, payload, connection_policy_sid=self._solution['connection_policy_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Voice.V1.ConnectionPolicyTargetPage>'




class ConnectionPolicyTargetContext(InstanceContext):

    def __init__(self, version: Version, connection_policy_sid: str, sid: str):
        """
        Initialize the ConnectionPolicyTargetContext

        :param Version version: Version that contains the resource
        :param connection_policy_sid: The SID of the Connection Policy that owns the Target.:param sid: The unique string that we created to identify the Target resource to update.

        :returns: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetContext
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'connection_policy_sid': connection_policy_sid,
            'sid': sid,
        }
        self._uri = '/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}'.format(**self._solution)
        
    
    
    def delete(self):
        """
        Deletes the ConnectionPolicyTargetInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the ConnectionPolicyTargetInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(method='DELETE', uri=self._uri,)
    
    
    def fetch(self):
        """
        Fetch the ConnectionPolicyTargetInstance
        

        :returns: The fetched ConnectionPolicyTargetInstance
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ConnectionPolicyTargetInstance(
            self._version,
            payload,
            connection_policy_sid=self._solution['connection_policy_sid'],
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the ConnectionPolicyTargetInstance
        

        :returns: The fetched ConnectionPolicyTargetInstance
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return ConnectionPolicyTargetInstance(
            self._version,
            payload,
            connection_policy_sid=self._solution['connection_policy_sid'],
            sid=self._solution['sid'],
            
        )
    
    
    def update(self, friendly_name=values.unset, target=values.unset, priority=values.unset, weight=values.unset, enabled=values.unset):
        """
        Update the ConnectionPolicyTargetInstance
        
        :params str friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :params str target: The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
        :params int priority: The relative importance of the target. Can be an integer from 0 to 65535, inclusive. The lowest number represents the most important target.
        :params int weight: The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive. Targets with higher values receive more load than those with lower ones with the same priority.
        :params bool enabled: Whether the Target is enabled.

        :returns: The updated ConnectionPolicyTargetInstance
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'Target': target,
            'Priority': priority,
            'Weight': weight,
            'Enabled': enabled,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return ConnectionPolicyTargetInstance(
            self._version,
            payload,
            connection_policy_sid=self._solution['connection_policy_sid'],
            sid=self._solution['sid']
        )

    async def update_async(self, friendly_name=values.unset, target=values.unset, priority=values.unset, weight=values.unset, enabled=values.unset):
        """
        Asynchronous coroutine to update the ConnectionPolicyTargetInstance
        
        :params str friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :params str target: The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
        :params int priority: The relative importance of the target. Can be an integer from 0 to 65535, inclusive. The lowest number represents the most important target.
        :params int weight: The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive. Targets with higher values receive more load than those with lower ones with the same priority.
        :params bool enabled: Whether the Target is enabled.

        :returns: The updated ConnectionPolicyTargetInstance
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'Target': target,
            'Priority': priority,
            'Weight': weight,
            'Enabled': enabled,
        })
        

        payload = await self._version.update_async(method='POST', uri=self._uri, data=data,)

        return ConnectionPolicyTargetInstance(
            self._version,
            payload,
            connection_policy_sid=self._solution['connection_policy_sid'],
            sid=self._solution['sid']
        )
    
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Voice.V1.ConnectionPolicyTargetContext {}>'.format(context)

class ConnectionPolicyTargetInstance(InstanceResource):

    def __init__(self, version, payload, connection_policy_sid: str, sid: str=None):
        """
        Initialize the ConnectionPolicyTargetInstance
        :returns: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetInstance
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'connection_policy_sid': payload.get('connection_policy_sid'),
            'sid': payload.get('sid'),
            'friendly_name': payload.get('friendly_name'),
            'target': payload.get('target'),
            'priority': deserialize.integer(payload.get('priority')),
            'weight': deserialize.integer(payload.get('weight')),
            'enabled': payload.get('enabled'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'connection_policy_sid': connection_policy_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ConnectionPolicyTargetContext for this ConnectionPolicyTargetInstance
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetContext
        """
        if self._context is None:
            self._context = ConnectionPolicyTargetContext(self._version, connection_policy_sid=self._solution['connection_policy_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Target resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def connection_policy_sid(self):
        """
        :returns: The SID of the Connection Policy that owns the Target.
        :rtype: str
        """
        return self._properties['connection_policy_sid']
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Target resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def target(self):
        """
        :returns: The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
        :rtype: str
        """
        return self._properties['target']
    
    @property
    def priority(self):
        """
        :returns: The relative importance of the target. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important target.
        :rtype: int
        """
        return self._properties['priority']
    
    @property
    def weight(self):
        """
        :returns: The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. Targets with higher values receive more load than those with lower ones with the same priority.
        :rtype: int
        """
        return self._properties['weight']
    
    @property
    def enabled(self):
        """
        :returns: Whether the target is enabled. The default is `true`.
        :rtype: bool
        """
        return self._properties['enabled']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties['url']
    
    
    def delete(self):
        """
        Deletes the ConnectionPolicyTargetInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the ConnectionPolicyTargetInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()
    
    
    def fetch(self):
        """
        Fetch the ConnectionPolicyTargetInstance
        

        :returns: The fetched ConnectionPolicyTargetInstance
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the ConnectionPolicyTargetInstance
        

        :returns: The fetched ConnectionPolicyTargetInstance
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, friendly_name=values.unset, target=values.unset, priority=values.unset, weight=values.unset, enabled=values.unset):
        """
        Update the ConnectionPolicyTargetInstance
        
        :params str friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :params str target: The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
        :params int priority: The relative importance of the target. Can be an integer from 0 to 65535, inclusive. The lowest number represents the most important target.
        :params int weight: The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive. Targets with higher values receive more load than those with lower ones with the same priority.
        :params bool enabled: Whether the Target is enabled.

        :returns: The updated ConnectionPolicyTargetInstance
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetInstance
        """
        return self._proxy.update(friendly_name=friendly_name, target=target, priority=priority, weight=weight, enabled=enabled, )

    async def update_async(self, friendly_name=values.unset, target=values.unset, priority=values.unset, weight=values.unset, enabled=values.unset):
        """
        Asynchronous coroutine to update the ConnectionPolicyTargetInstance
        
        :params str friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :params str target: The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
        :params int priority: The relative importance of the target. Can be an integer from 0 to 65535, inclusive. The lowest number represents the most important target.
        :params int weight: The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive. Targets with higher values receive more load than those with lower ones with the same priority.
        :params bool enabled: Whether the Target is enabled.

        :returns: The updated ConnectionPolicyTargetInstance
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetInstance
        """
        return await self._proxy.update_async(friendly_name=friendly_name, target=target, priority=priority, weight=weight, enabled=enabled, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Voice.V1.ConnectionPolicyTargetInstance {}>'.format(context)


