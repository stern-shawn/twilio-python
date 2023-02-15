"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
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

# from twilio.rest.interaction_channel.interaction_channel_invite import InteractionChannelInviteListInstancefrom twilio.rest.interaction_channel.interaction_channel_participant import InteractionChannelParticipantListInstance


class InteractionChannelContext(InstanceContext):
    def __init__(self, version: Version, interaction_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'interaction_sid': interaction_sid, 'sid': sid,  }
        self._uri = '/Interactions/${interaction_sid}/Channels/${sid}'
        
        self._invites = None
        self._participants = None
    
    def fetch(self):
        
        """
        Fetch the InteractionChannelInstance

        :returns: The fetched InteractionChannelInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return InteractionChannelInstance(self._version, payload, interaction_sid=self._solution['interaction_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return InteractionChannelInstance(self._version, payload, interaction_sid=self._solution['interaction_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.InteractionChannelContext>'



class InteractionChannelInstance(InstanceResource):
    def __init__(self, version, payload, interaction_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'interaction_sid' : payload.get('interaction_sid'),
            'type' : payload.get('type'),
            'status' : payload.get('status'),
            'error_code' : payload.get('error_code'),
            'error_message' : payload.get('error_message'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'interaction_sid': interaction_sid or self._properties['interaction_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = InteractionChannelContext(
                self._version,
                interaction_sid=self._solution['interaction_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def invites(self):
        return self._proxy.invites
    @property
    def participants(self):
        return self._proxy.participants
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.InteractionChannelInstance {}>'.format(context)



class InteractionChannelList(ListResource):
    def __init__(self, version: Version, interaction_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'interaction_sid': interaction_sid,  }
        self._uri = '/Interactions/${interaction_sid}/Channels'
        

    """
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return InteractionChannelPage(self._version, payload, interaction_sid=self._solution['interaction_sid'], )
    """


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.InteractionChannelList>'

