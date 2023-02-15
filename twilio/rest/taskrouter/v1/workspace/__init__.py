"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Taskrouter
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

# from twilio.rest.workspace.activity import ActivityListInstancefrom twilio.rest.workspace.event import EventListInstancefrom twilio.rest.workspace.task import TaskListInstancefrom twilio.rest.workspace.task_channel import TaskChannelListInstancefrom twilio.rest.workspace.task_queue import TaskQueueListInstancefrom twilio.rest.workspace.worker import WorkerListInstancefrom twilio.rest.workspace.workflow import WorkflowListInstancefrom twilio.rest.workspace.workspace_cumulative_statistics import WorkspaceCumulativeStatisticsListInstancefrom twilio.rest.workspace.workspace_real_time_statistics import WorkspaceRealTimeStatisticsListInstancefrom twilio.rest.workspace.workspace_statistics import WorkspaceStatisticsListInstance


class WorkspaceContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid,  }
        self._uri = '/Workspaces/${sid}'
        
        self._activities = None
        self._events = None
        self._tasks = None
        self._task_channels = None
        self._task_queues = None
        self._workers = None
        self._workflows = None
        self._cumulative_statistics = None
        self._real_time_statistics = None
        self._statistics = None
    
    def delete(self):
        
        

        """
        Deletes the WorkspaceInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the WorkspaceInstance

        :returns: The fetched WorkspaceInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return WorkspaceInstance(self._version, payload, sid=self._solution['sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return WorkspaceInstance(self._version, payload, sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.WorkspaceContext>'



class WorkspaceInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'default_activity_name' : payload.get('default_activity_name'),
            'default_activity_sid' : payload.get('default_activity_sid'),
            'event_callback_url' : payload.get('event_callback_url'),
            'events_filter' : payload.get('events_filter'),
            'friendly_name' : payload.get('friendly_name'),
            'multi_task_enabled' : payload.get('multi_task_enabled'),
            'sid' : payload.get('sid'),
            'timeout_activity_name' : payload.get('timeout_activity_name'),
            'timeout_activity_sid' : payload.get('timeout_activity_sid'),
            'prioritize_queue_order' : payload.get('prioritize_queue_order'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = WorkspaceContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def activities(self):
        return self._proxy.activities
    @property
    def events(self):
        return self._proxy.events
    @property
    def tasks(self):
        return self._proxy.tasks
    @property
    def task_channels(self):
        return self._proxy.task_channels
    @property
    def task_queues(self):
        return self._proxy.task_queues
    @property
    def workers(self):
        return self._proxy.workers
    @property
    def workflows(self):
        return self._proxy.workflows
    @property
    def cumulative_statistics(self):
        return self._proxy.cumulative_statistics
    @property
    def real_time_statistics(self):
        return self._proxy.real_time_statistics
    @property
    def statistics(self):
        return self._proxy.statistics
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.WorkspaceInstance {}>'.format(context)



class WorkspaceList(ListResource):
    def __init__(self, version: Version):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Workspaces'
        

    """
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return WorkspaceInstance(self._version, payload, )
        
    """

    """
    def page(self, friendly_name, page_size):
        
        data = values.of({
            'friendly_name': friendly_name,'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return WorkspacePage(self._version, payload, )
    """


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.WorkspaceList>'

