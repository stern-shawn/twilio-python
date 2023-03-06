"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Ip_messaging
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
from twilio.rest.ip_messaging.v1.service.user.user_channel import UserChannelList


class UserList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the UserList

        :param Version version: Version that contains the resource
        :param service_sid: 
        
        :returns: twilio.rest.ip_messaging.v1.service.user.UserList
        :rtype: twilio.rest.ip_messaging.v1.service.user.UserList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/{service_sid}/Users'.format(**self._solution)
        
        
    
    
    
    
    def create(self, identity, role_sid=values.unset, attributes=values.unset, friendly_name=values.unset):
        """
        Create the UserInstance

        :param str identity: 
        :param str role_sid: 
        :param str attributes: 
        :param str friendly_name: 
        
        :returns: The created UserInstance
        :rtype: twilio.rest.ip_messaging.v1.service.user.UserInstance
        """
        data = values.of({ 
            'Identity': identity,
            'RoleSid': role_sid,
            'Attributes': attributes,
            'FriendlyName': friendly_name,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return UserInstance(self._version, payload, service_sid=self._solution['service_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams UserInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.ip_messaging.v1.service.user.UserInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists UserInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.ip_messaging.v1.service.user.UserInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of UserInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UserInstance
        :rtype: twilio.rest.ip_messaging.v1.service.user.UserPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return UserPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of UserInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UserInstance
        :rtype: twilio.rest.ip_messaging.v1.service.user.UserPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return UserPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a UserContext
        
        :param sid: 
        
        :returns: twilio.rest.ip_messaging.v1.service.user.UserContext
        :rtype: twilio.rest.ip_messaging.v1.service.user.UserContext
        """
        return UserContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a UserContext
        
        :param sid: 
        
        :returns: twilio.rest.ip_messaging.v1.service.user.UserContext
        :rtype: twilio.rest.ip_messaging.v1.service.user.UserContext
        """
        return UserContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V1.UserList>'










class UserPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the UserPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.ip_messaging.v1.service.user.UserPage
        :rtype: twilio.rest.ip_messaging.v1.service.user.UserPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UserInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.ip_messaging.v1.service.user.UserInstance
        :rtype: twilio.rest.ip_messaging.v1.service.user.UserInstance
        """
        return UserInstance(self._version, payload, service_sid=self._solution['service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V1.UserPage>'




class UserContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the UserContext

        :param Version version: Version that contains the resource
        :param service_sid: :param sid: 

        :returns: twilio.rest.ip_messaging.v1.service.user.UserContext
        :rtype: twilio.rest.ip_messaging.v1.service.user.UserContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Users/{sid}'.format(**self._solution)
        
        self._user_channels = None
    
    def delete(self):
        """
        Deletes the UserInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the UserInstance
        

        :returns: The fetched UserInstance
        :rtype: twilio.rest.ip_messaging.v1.service.user.UserInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return UserInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, role_sid=values.unset, attributes=values.unset, friendly_name=values.unset):
        """
        Update the UserInstance
        
        :params str role_sid: 
        :params str attributes: 
        :params str friendly_name: 

        :returns: The updated UserInstance
        :rtype: twilio.rest.ip_messaging.v1.service.user.UserInstance
        """
        data = values.of({ 
            'RoleSid': role_sid,
            'Attributes': attributes,
            'FriendlyName': friendly_name,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return UserInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid']
        )
        
    
    @property
    def user_channels(self):
        """
        Access the user_channels

        :returns: twilio.rest.ip_messaging.v1.service.user.UserChannelList
        :rtype: twilio.rest.ip_messaging.v1.service.user.UserChannelList
        """
        if self._user_channels is None:
            self._user_channels = UserChannelList(self._version, self._solution['service_sid'], self._solution['sid'],
            )
        return self._user_channels
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V1.UserContext {}>'.format(context)

class UserInstance(InstanceResource):

    def __init__(self, version, payload, service_sid: str, sid: str=None):
        """
        Initialize the UserInstance
        :returns: twilio.rest.ip_messaging.v1.service.user.UserInstance
        :rtype: twilio.rest.ip_messaging.v1.service.user.UserInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'attributes': payload.get('attributes'),
            'friendly_name': payload.get('friendly_name'),
            'role_sid': payload.get('role_sid'),
            'identity': payload.get('identity'),
            'is_online': payload.get('is_online'),
            'is_notifiable': payload.get('is_notifiable'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'joined_channels_count': deserialize.integer(payload.get('joined_channels_count')),
            'links': payload.get('links'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: UserContext for this UserInstance
        :rtype: twilio.rest.ip_messaging.v1.service.user.UserContext
        """
        if self._context is None:
            self._context = UserContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'],)
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
    def service_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def attributes(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['attributes']
    
    @property
    def friendly_name(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def role_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['role_sid']
    
    @property
    def identity(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['identity']
    
    @property
    def is_online(self):
        """
        :returns: 
        :rtype: bool
        """
        return self._properties['is_online']
    
    @property
    def is_notifiable(self):
        """
        :returns: 
        :rtype: bool
        """
        return self._properties['is_notifiable']
    
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
    def joined_channels_count(self):
        """
        :returns: 
        :rtype: int
        """
        return self._properties['joined_channels_count']
    
    @property
    def links(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['links']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    def delete(self):
        """
        Deletes the UserInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the UserInstance
        

        :returns: The fetched UserInstance
        :rtype: twilio.rest.ip_messaging.v1.service.user.UserInstance
        """
        return self._proxy.fetch()
    
    def update(self, role_sid=values.unset, attributes=values.unset, friendly_name=values.unset):
        """
        Update the UserInstance
        
        :params str role_sid: 
        :params str attributes: 
        :params str friendly_name: 

        :returns: The updated UserInstance
        :rtype: twilio.rest.ip_messaging.v1.service.user.UserInstance
        """
        return self._proxy.update(role_sid=role_sid, attributes=attributes, friendly_name=friendly_name, )
    
    @property
    def user_channels(self):
        """
        Access the user_channels

        :returns: twilio.rest.ip_messaging.v1.service.user.UserChannelList
        :rtype: twilio.rest.ip_messaging.v1.service.user.UserChannelList
        """
        return self._proxy.user_channels
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V1.UserInstance {}>'.format(context)


