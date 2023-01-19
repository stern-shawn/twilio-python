"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Proxy
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

# 


class MessageInteractionContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, session_sid: str, participant_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'session_sid': session_sid, 'participant_sid': participant_sid, 'sid': sid,  }
        self._uri = '/Services/${service_sid}/Sessions/${session_sid}/Participants/${participant_sid}/MessageInteractions/${sid}'
        
    
    def fetch(self):
        
        """
        Fetch the MessageInteractionInstance

        :returns: The fetched MessageInteractionInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return MessageInteractionInstance(self._version, payload, service_sid=self._solution['service_sid'], session_sid=self._solution['session_sid'], participant_sid=self._solution['participant_sid'], sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.MessageInteractionContext>'



class MessageInteractionInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, session_sid: str, participant_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'session_sid' : payload.get('session_sid'),
            'service_sid' : payload.get('service_sid'),
            'account_sid' : payload.get('account_sid'),
            'data' : payload.get('data'),
            'type' : payload.get('type'),
            'participant_sid' : payload.get('participant_sid'),
            'inbound_participant_sid' : payload.get('inbound_participant_sid'),
            'inbound_resource_sid' : payload.get('inbound_resource_sid'),
            'inbound_resource_status' : payload.get('inbound_resource_status'),
            'inbound_resource_type' : payload.get('inbound_resource_type'),
            'inbound_resource_url' : payload.get('inbound_resource_url'),
            'outbound_participant_sid' : payload.get('outbound_participant_sid'),
            'outbound_resource_sid' : payload.get('outbound_resource_sid'),
            'outbound_resource_status' : payload.get('outbound_resource_status'),
            'outbound_resource_type' : payload.get('outbound_resource_type'),
            'outbound_resource_url' : payload.get('outbound_resource_url'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid'],'session_sid': session_sid or self._properties['session_sid'],'participant_sid': participant_sid or self._properties['participant_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = MessageInteractionContext(
                self._version,
                service_sid=self._solution['service_sid'],session_sid=self._solution['session_sid'],participant_sid=self._solution['participant_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.MessageInteractionInstance {}>'.format(context)



class MessageInteractionListInstance(ListResource):
    def __init__(self, version: Version, service_sid: str, session_sid: str, participant_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'session_sid': session_sid, 'participant_sid': participant_sid,  }
        self._uri = '/Services/${service_sid}/Sessions/${session_sid}/Participants/${participant_sid}/MessageInteractions'
        
    
    """
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return MessageInteractionInstance(self._version, payload, service_sid=self._solution['service_sid']session_sid=self._solution['session_sid']participant_sid=self._solution['participant_sid'])
        
    """
    
    """
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return MessageInteractionPage(self._version, payload, service_sid=self._solution['service_sid'], session_sid=self._solution['session_sid'], participant_sid=self._solution['participant_sid'], )
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.MessageInteractionListInstance>'

