"""
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
from twilio.base.page import Page
from twilio.rest.studio.v2.flow.execution.execution_step.execution_step_context import ExecutionStepContextList


class ExecutionStepList(ListResource):

    def __init__(self, version: Version, flow_sid: str, execution_sid: str):
        """
        Initialize the ExecutionStepList

        :param Version version: Version that contains the resource
        :param flow_sid: The SID of the Flow with the Steps to read.
        :param execution_sid: The SID of the Execution with the Steps to read.
        
        :returns: twilio.rest.studio.v2.flow.execution.execution_step.ExecutionStepList
        :rtype: twilio.rest.studio.v2.flow.execution.execution_step.ExecutionStepList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'flow_sid': flow_sid, 'execution_sid': execution_sid,  }
        self._uri = '/Flows/${flow_sid}/Executions/${execution_sid}/Steps'.format(**self._solution)
        
        
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams ExecutionStepInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.studio.v2.flow.execution.execution_step.ExecutionStepInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ExecutionStepInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.studio.v2.flow.execution.execution_step.ExecutionStepInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ExecutionStepInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ExecutionStepInstance
        :rtype: twilio.rest.studio.v2.flow.execution.execution_step.ExecutionStepPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ExecutionStepPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ExecutionStepInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ExecutionStepInstance
        :rtype: twilio.rest.studio.v2.flow.execution.execution_step.ExecutionStepPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ExecutionStepPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a ExecutionStepContext
        
        :param sid: The SID of the ExecutionStep resource to fetch.
        
        :returns: twilio.rest.studio.v2.flow.execution.execution_step.ExecutionStepContext
        :rtype: twilio.rest.studio.v2.flow.execution.execution_step.ExecutionStepContext
        """
        return ExecutionStepContext(self._version, flow_sid=self._solution['flow_sid'], execution_sid=self._solution['execution_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a ExecutionStepContext
        
        :param sid: The SID of the ExecutionStep resource to fetch.
        
        :returns: twilio.rest.studio.v2.flow.execution.execution_step.ExecutionStepContext
        :rtype: twilio.rest.studio.v2.flow.execution.execution_step.ExecutionStepContext
        """
        return ExecutionStepContext(self._version, flow_sid=self._solution['flow_sid'], execution_sid=self._solution['execution_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V2.ExecutionStepList>'




class ExecutionStepPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ExecutionStepPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.studio.v2.flow.execution.execution_step.ExecutionStepPage
        :rtype: twilio.rest.studio.v2.flow.execution.execution_step.ExecutionStepPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ExecutionStepInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.studio.v2.flow.execution.execution_step.ExecutionStepInstance
        :rtype: twilio.rest.studio.v2.flow.execution.execution_step.ExecutionStepInstance
        """
        return ExecutionStepInstance(self._version, payload, flow_sid=self._solution['flow_sid'], execution_sid=self._solution['execution_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V2.ExecutionStepPage>'





class ExecutionStepContext(InstanceContext):
    def __init__(self, version: Version, flow_sid: str, execution_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'flow_sid': flow_sid, 'execution_sid': execution_sid, 'sid': sid,  }
        self._uri = '/Flows/${flow_sid}/Executions/${execution_sid}/Steps/${sid}'
        
        self._step_context = None
    
    def fetch(self):
        
        """
        Fetch the ExecutionStepInstance

        :returns: The fetched ExecutionStepInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ExecutionStepInstance(self._version, payload, flow_sid=self._solution['flow_sid'], execution_sid=self._solution['execution_sid'], sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V2.ExecutionStepContext>'



class ExecutionStepInstance(InstanceResource):
    def __init__(self, version, payload, flow_sid: str, execution_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'flow_sid' : payload.get('flow_sid'),
            'execution_sid' : payload.get('execution_sid'),
            'name' : payload.get('name'),
            'context' : payload.get('context'),
            'transitioned_from' : payload.get('transitioned_from'),
            'transitioned_to' : payload.get('transitioned_to'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'flow_sid': flow_sid or self._properties['flow_sid'],'execution_sid': execution_sid or self._properties['execution_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ExecutionStepContext(
                self._version,
                flow_sid=self._solution['flow_sid'],execution_sid=self._solution['execution_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def step_context(self):
        return self._proxy.step_context
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V2.ExecutionStepInstance {}>'.format(context)



