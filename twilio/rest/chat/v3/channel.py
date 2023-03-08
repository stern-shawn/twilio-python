"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Chat
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



class ChannelList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the ChannelList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.chat.v3.channel.ChannelList
        :rtype: twilio.rest.chat.v3.channel.ChannelList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    

    def get(self, service_sid, sid):
        """
        Constructs a ChannelContext
        
        :param service_sid: The unique SID identifier of the Service.
        
        :param sid: A 34 character string that uniquely identifies this Channel.
        
        :returns: twilio.rest.chat.v3.channel.ChannelContext
        :rtype: twilio.rest.chat.v3.channel.ChannelContext
        """
        return ChannelContext(self._version, service_sid=service_sid, sid=sid)

    def __call__(self, service_sid, sid):
        """
        Constructs a ChannelContext
        
        :param service_sid: The unique SID identifier of the Service.
        
        :param sid: A 34 character string that uniquely identifies this Channel.
        
        :returns: twilio.rest.chat.v3.channel.ChannelContext
        :rtype: twilio.rest.chat.v3.channel.ChannelContext
        """
        return ChannelContext(self._version, service_sid=service_sid, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat.V3.ChannelList>'

class ChannelContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the ChannelContext

        :param Version version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.:param sid: A 34 character string that uniquely identifies this Channel.

        :returns: twilio.rest.chat.v3.channel.ChannelContext
        :rtype: twilio.rest.chat.v3.channel.ChannelContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Channels/{sid}'.format(**self._solution)
        
    
    def update(self, x_twilio_webhook_enabled=values.unset, type=values.unset, messaging_service_sid=values.unset):
        """
        Update the ChannelInstance
        
        :params ChannelInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :params ChannelInstance.ChannelType type: 
        :params str messaging_service_sid: The unique ID of the [Messaging Service](https://www.twilio.com/docs/sms/services/api) this channel belongs to.

        :returns: The updated ChannelInstance
        :rtype: twilio.rest.chat.v3.channel.ChannelInstance
        """
        data = values.of({ 
            'Type': type,
            'MessagingServiceSid': messaging_service_sid,
        })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers)

        return ChannelInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Chat.V3.ChannelContext {}>'.format(context)

class ChannelInstance(InstanceResource):

    class ChannelType(object):
        PUBLIC = "public"
        PRIVATE = "private"

    class WebhookEnabledType(object):
        TRUE = "true"
        FALSE = "false"

    def __init__(self, version, payload, service_sid: str=None, sid: str=None):
        """
        Initialize the ChannelInstance
        :returns: twilio.rest.chat.v3.channel.ChannelInstance
        :rtype: twilio.rest.chat.v3.channel.ChannelInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'friendly_name': payload.get('friendly_name'),
            'unique_name': payload.get('unique_name'),
            'attributes': payload.get('attributes'),
            'type': payload.get('type'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'created_by': payload.get('created_by'),
            'members_count': deserialize.integer(payload.get('members_count')),
            'messages_count': deserialize.integer(payload.get('messages_count')),
            'messaging_service_sid': payload.get('messaging_service_sid'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid or self._properties['service_sid'], 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ChannelContext for this ChannelInstance
        :rtype: twilio.rest.chat.v3.channel.ChannelContext
        """
        if self._context is None:
            self._context = ChannelContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Channel resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Channel resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) the Channel resource is associated with.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.
        :rtype: str
        """
        return self._properties['unique_name']
    
    @property
    def attributes(self):
        """
        :returns: The JSON string that stores application-specific data. If attributes have not been set, `{}` is returned.
        :rtype: str
        """
        return self._properties['attributes']
    
    @property
    def type(self):
        """
        :returns: 
        :rtype: ChannelInstance.ChannelType
        """
        return self._properties['type']
    
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
    def created_by(self):
        """
        :returns: The `identity` of the User that created the channel. If the Channel was created by using the API, the value is `system`.
        :rtype: str
        """
        return self._properties['created_by']
    
    @property
    def members_count(self):
        """
        :returns: The number of Members in the Channel.
        :rtype: int
        """
        return self._properties['members_count']
    
    @property
    def messages_count(self):
        """
        :returns: The number of Messages that have been passed in the Channel.
        :rtype: int
        """
        return self._properties['messages_count']
    
    @property
    def messaging_service_sid(self):
        """
        :returns: The unique ID of the [Messaging Service](https://www.twilio.com/docs/sms/services/api) this channel belongs to.
        :rtype: str
        """
        return self._properties['messaging_service_sid']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Channel resource.
        :rtype: str
        """
        return self._properties['url']
    
    def update(self, x_twilio_webhook_enabled=values.unset, type=values.unset, messaging_service_sid=values.unset):
        """
        Update the ChannelInstance
        
        :params ChannelInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :params ChannelInstance.ChannelType type: 
        :params str messaging_service_sid: The unique ID of the [Messaging Service](https://www.twilio.com/docs/sms/services/api) this channel belongs to.

        :returns: The updated ChannelInstance
        :rtype: twilio.rest.chat.v3.channel.ChannelInstance
        """
        return self._proxy.update(x_twilio_webhook_enabled=x_twilio_webhook_enabled, type=type, messaging_service_sid=messaging_service_sid, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Chat.V3.ChannelInstance {}>'.format(context)


