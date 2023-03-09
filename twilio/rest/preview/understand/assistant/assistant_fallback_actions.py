r"""
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



class AssistantFallbackActionsList(ListResource):

    def __init__(self, version: Version, assistant_sid: str):
        """
        Initialize the AssistantFallbackActionsList

        :param Version version: Version that contains the resource
        :param assistant_sid: 
        
        :returns: twilio.rest.preview.understand.assistant.assistant_fallback_actions.AssistantFallbackActionsList
        :rtype: twilio.rest.preview.understand.assistant.assistant_fallback_actions.AssistantFallbackActionsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid,  }
        
        
        
    
    

    def get(self):
        """
        Constructs a AssistantFallbackActionsContext
        
        :returns: twilio.rest.preview.understand.assistant.assistant_fallback_actions.AssistantFallbackActionsContext
        :rtype: twilio.rest.preview.understand.assistant.assistant_fallback_actions.AssistantFallbackActionsContext
        """
        return AssistantFallbackActionsContext(self._version, assistant_sid=self._solution['assistant_sid'])

    def __call__(self):
        """
        Constructs a AssistantFallbackActionsContext
        
        :returns: twilio.rest.preview.understand.assistant.assistant_fallback_actions.AssistantFallbackActionsContext
        :rtype: twilio.rest.preview.understand.assistant.assistant_fallback_actions.AssistantFallbackActionsContext
        """
        return AssistantFallbackActionsContext(self._version, assistant_sid=self._solution['assistant_sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Understand.AssistantFallbackActionsList>'

class AssistantFallbackActionsContext(InstanceContext):

    def __init__(self, version: Version, assistant_sid: str):
        """
        Initialize the AssistantFallbackActionsContext

        :param Version version: Version that contains the resource
        :param assistant_sid: 

        :returns: twilio.rest.preview.understand.assistant.assistant_fallback_actions.AssistantFallbackActionsContext
        :rtype: twilio.rest.preview.understand.assistant.assistant_fallback_actions.AssistantFallbackActionsContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'assistant_sid': assistant_sid,
        }
        self._uri = '/Assistants/{assistant_sid}/FallbackActions'.format(**self._solution)
        
    
    
    def fetch(self):
        """
        Fetch the AssistantFallbackActionsInstance
        

        :returns: The fetched AssistantFallbackActionsInstance
        :rtype: twilio.rest.preview.understand.assistant.assistant_fallback_actions.AssistantFallbackActionsInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AssistantFallbackActionsInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the AssistantFallbackActionsInstance
        

        :returns: The fetched AssistantFallbackActionsInstance
        :rtype: twilio.rest.preview.understand.assistant.assistant_fallback_actions.AssistantFallbackActionsInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return AssistantFallbackActionsInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            
        )
    
    
    def update(self, fallback_actions=values.unset):
        """
        Update the AssistantFallbackActionsInstance
        
        :params object fallback_actions: 

        :returns: The updated AssistantFallbackActionsInstance
        :rtype: twilio.rest.preview.understand.assistant.assistant_fallback_actions.AssistantFallbackActionsInstance
        """
        data = values.of({ 
            'FallbackActions': serialize.object(fallback_actions),
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return AssistantFallbackActionsInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid']
        )

    async def update_async(self, fallback_actions=values.unset):
        """
        Asynchronous coroutine to update the AssistantFallbackActionsInstance
        
        :params object fallback_actions: 

        :returns: The updated AssistantFallbackActionsInstance
        :rtype: twilio.rest.preview.understand.assistant.assistant_fallback_actions.AssistantFallbackActionsInstance
        """
        data = values.of({ 
            'FallbackActions': serialize.object(fallback_actions),
        })
        

        payload = await self._version.update_async(method='POST', uri=self._uri, data=data,)

        return AssistantFallbackActionsInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid']
        )
    
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Understand.AssistantFallbackActionsContext {}>'.format(context)

class AssistantFallbackActionsInstance(InstanceResource):

    def __init__(self, version, payload, assistant_sid: str):
        """
        Initialize the AssistantFallbackActionsInstance
        :returns: twilio.rest.preview.understand.assistant.assistant_fallback_actions.AssistantFallbackActionsInstance
        :rtype: twilio.rest.preview.understand.assistant.assistant_fallback_actions.AssistantFallbackActionsInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'assistant_sid': payload.get('assistant_sid'),
            'url': payload.get('url'),
            'data': payload.get('data'),
        }

        self._context = None
        self._solution = { 'assistant_sid': assistant_sid,  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AssistantFallbackActionsContext for this AssistantFallbackActionsInstance
        :rtype: twilio.rest.preview.understand.assistant.assistant_fallback_actions.AssistantFallbackActionsContext
        """
        if self._context is None:
            self._context = AssistantFallbackActionsContext(self._version, assistant_sid=self._solution['assistant_sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def assistant_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['assistant_sid']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def data(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['data']
    
    
    def fetch(self):
        """
        Fetch the AssistantFallbackActionsInstance
        

        :returns: The fetched AssistantFallbackActionsInstance
        :rtype: twilio.rest.preview.understand.assistant.assistant_fallback_actions.AssistantFallbackActionsInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the AssistantFallbackActionsInstance
        

        :returns: The fetched AssistantFallbackActionsInstance
        :rtype: twilio.rest.preview.understand.assistant.assistant_fallback_actions.AssistantFallbackActionsInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, fallback_actions=values.unset):
        """
        Update the AssistantFallbackActionsInstance
        
        :params object fallback_actions: 

        :returns: The updated AssistantFallbackActionsInstance
        :rtype: twilio.rest.preview.understand.assistant.assistant_fallback_actions.AssistantFallbackActionsInstance
        """
        return self._proxy.update(fallback_actions=fallback_actions, )

    async def update_async(self, fallback_actions=values.unset):
        """
        Asynchronous coroutine to update the AssistantFallbackActionsInstance
        
        :params object fallback_actions: 

        :returns: The updated AssistantFallbackActionsInstance
        :rtype: twilio.rest.preview.understand.assistant.assistant_fallback_actions.AssistantFallbackActionsInstance
        """
        return await self._proxy.update_async(fallback_actions=fallback_actions, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Understand.AssistantFallbackActionsInstance {}>'.format(context)


