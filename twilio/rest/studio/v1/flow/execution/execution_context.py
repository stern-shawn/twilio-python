r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Studio
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



class ExecutionContextList(ListResource):

    def __init__(self, version: Version, flow_sid: str, execution_sid: str):
        """
        Initialize the ExecutionContextList

        :param Version version: Version that contains the resource
        :param flow_sid: The SID of the Flow with the Execution context to fetch.
        :param execution_sid: The SID of the Execution context to fetch.
        
        :returns: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextList
        :rtype: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'flow_sid': flow_sid, 'execution_sid': execution_sid,  }
        
        
        
    

    def get(self):
        """
        Constructs a ExecutionContextContext
        
        :returns: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextContext
        :rtype: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextContext
        """
        return ExecutionContextContext(self._version, flow_sid=self._solution['flow_sid'], execution_sid=self._solution['execution_sid'])

    def __call__(self):
        """
        Constructs a ExecutionContextContext
        
        :returns: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextContext
        :rtype: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextContext
        """
        return ExecutionContextContext(self._version, flow_sid=self._solution['flow_sid'], execution_sid=self._solution['execution_sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V1.ExecutionContextList>'

class ExecutionContextContext(InstanceContext):

    def __init__(self, version: Version, flow_sid: str, execution_sid: str):
        """
        Initialize the ExecutionContextContext

        :param Version version: Version that contains the resource
        :param flow_sid: The SID of the Flow with the Execution context to fetch.:param execution_sid: The SID of the Execution context to fetch.

        :returns: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextContext
        :rtype: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'flow_sid': flow_sid,
            'execution_sid': execution_sid,
        }
        self._uri = '/Flows/{flow_sid}/Executions/{execution_sid}/Context'.format(**self._solution)
        
    
    
    def fetch(self):
        """
        Fetch the ExecutionContextInstance
        

        :returns: The fetched ExecutionContextInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ExecutionContextInstance(
            self._version,
            payload,
            flow_sid=self._solution['flow_sid'],
            execution_sid=self._solution['execution_sid'],
            
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the ExecutionContextInstance
        

        :returns: The fetched ExecutionContextInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return ExecutionContextInstance(
            self._version,
            payload,
            flow_sid=self._solution['flow_sid'],
            execution_sid=self._solution['execution_sid'],
            
        )
    
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V1.ExecutionContextContext {}>'.format(context)

class ExecutionContextInstance(InstanceResource):

    def __init__(self, version, payload, flow_sid: str, execution_sid: str):
        """
        Initialize the ExecutionContextInstance
        :returns: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'context': payload.get('context'),
            'flow_sid': payload.get('flow_sid'),
            'execution_sid': payload.get('execution_sid'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'flow_sid': flow_sid, 'execution_sid': execution_sid,  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ExecutionContextContext for this ExecutionContextInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextContext
        """
        if self._context is None:
            self._context = ExecutionContextContext(self._version, flow_sid=self._solution['flow_sid'], execution_sid=self._solution['execution_sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ExecutionContext resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def context(self):
        """
        :returns: The current state of the Flow's Execution. As a flow executes, we save its state in this context. We save data that your widgets can access as variables in configuration fields or in text areas as variable substitution.
        :rtype: dict
        """
        return self._properties['context']
    
    @property
    def flow_sid(self):
        """
        :returns: The SID of the Flow.
        :rtype: str
        """
        return self._properties['flow_sid']
    
    @property
    def execution_sid(self):
        """
        :returns: The SID of the context's Execution resource.
        :rtype: str
        """
        return self._properties['execution_sid']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties['url']
    
    
    def fetch(self):
        """
        Fetch the ExecutionContextInstance
        

        :returns: The fetched ExecutionContextInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the ExecutionContextInstance
        

        :returns: The fetched ExecutionContextInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextInstance
        """
        return await self._proxy.fetch_async()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V1.ExecutionContextInstance {}>'.format(context)


