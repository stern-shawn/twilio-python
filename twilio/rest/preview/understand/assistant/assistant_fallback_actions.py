"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
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

# 


class AssistantFallbackActionsContext(InstanceContext):
    def __init__(self, version: Version, assistant_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid,  }
        self._uri = '/Assistants/${assistant_sid}/FallbackActions'
        
    
    def fetch(self):
        
        """
        Fetch the AssistantFallbackActionsInstance

        :returns: The fetched AssistantFallbackActionsInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AssistantFallbackActionsInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return AssistantFallbackActionsInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.Understand.AssistantFallbackActionsContext>'



class AssistantFallbackActionsInstance(InstanceResource):
    def __init__(self, version, payload, assistant_sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'assistant_sid' : payload.get('assistant_sid'),
            'url' : payload.get('url'),
            'data' : payload.get('data'),
        }

        self._context = None
        self._solution = {
            'assistant_sid': assistant_sid or self._properties['assistant_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = AssistantFallbackActionsContext(
                self._version,
                assistant_sid=self._solution['assistant_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.Understand.AssistantFallbackActionsInstance {}>'.format(context)



class AssistantFallbackActionsListInstance(ListResource):
    def __init__(self, version: Version, assistant_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid,  }
        self._uri = ''
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.Understand.AssistantFallbackActionsListInstance>'

