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

from twilio.base.page import Page

# from twilio.rest.channel.invite import InviteListInstancefrom twilio.rest.channel.member import MemberListInstancefrom twilio.rest.channel.message import MessageListInstancefrom twilio.rest.channel.webhook import WebhookListInstance


class ChannelContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'sid': sid,  }
        self._uri = '/Services/${service_sid}/Channels/${sid}'
        
        self._invites = None
        self._members = None
        self._messages = None
        self._webhooks = None
    
    def delete(self, x_twilio_webhook_enabled):
        
        

        """
        Deletes the ChannelInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the ChannelInstance

        :returns: The fetched ChannelInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ChannelInstance(self._version, payload, service_sid=self._solution['service_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, x_twilio_webhook_enabled, body):
        data = values.of({
            'x_twilio_webhook_enabled': x_twilio_webhook_enabled,'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return ChannelInstance(self._version, payload, service_sid=self._solution['service_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.ChannelContext>'



class ChannelInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'service_sid' : payload.get('service_sid'),
            'friendly_name' : payload.get('friendly_name'),
            'unique_name' : payload.get('unique_name'),
            'attributes' : payload.get('attributes'),
            'type' : payload.get('type'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'created_by' : payload.get('created_by'),
            'members_count' : payload.get('members_count'),
            'messages_count' : payload.get('messages_count'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ChannelContext(
                self._version,
                service_sid=self._solution['service_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def invites(self):
        return self._proxy.invites
    @property
    def members(self):
        return self._proxy.members
    @property
    def messages(self):
        return self._proxy.messages
    @property
    def webhooks(self):
        return self._proxy.webhooks
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2.ChannelInstance {}>'.format(context)



class ChannelList(ListResource):
    def __init__(self, version: Version, service_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/${service_sid}/Channels'
        

    """
    def create(self, x_twilio_webhook_enabled, body):
        data = values.of({
            'x_twilio_webhook_enabled': x_twilio_webhook_enabled,'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return ChannelInstance(self._version, payload, service_sid=self._solution['service_sid'])
        
    """

    """
    def page(self, type, page_size):
        
        data = values.of({
            'type': type,'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return ChannelPage(self._version, payload, service_sid=self._solution['service_sid'], )
    """


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.ChannelList>'

