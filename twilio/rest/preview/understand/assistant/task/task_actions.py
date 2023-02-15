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


class TaskActionsContext(InstanceContext):
    def __init__(self, version: Version, assistant_sid: str, task_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid, 'task_sid': task_sid,  }
        self._uri = '/Assistants/${assistant_sid}/Tasks/${task_sid}/Actions'
        
    
    def fetch(self):
        
        """
        Fetch the TaskActionsInstance

        :returns: The fetched TaskActionsInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return TaskActionsInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], task_sid=self._solution['task_sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return TaskActionsInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], task_sid=self._solution['task_sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.Understand.TaskActionsContext>'



class TaskActionsInstance(InstanceResource):
    def __init__(self, version, payload, assistant_sid: str, task_sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'assistant_sid' : payload.get('assistant_sid'),
            'task_sid' : payload.get('task_sid'),
            'url' : payload.get('url'),
            'data' : payload.get('data'),
        }

        self._context = None
        self._solution = {
            'assistant_sid': assistant_sid or self._properties['assistant_sid'],'task_sid': task_sid or self._properties['task_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = TaskActionsContext(
                self._version,
                assistant_sid=self._solution['assistant_sid'],task_sid=self._solution['task_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.Understand.TaskActionsInstance {}>'.format(context)



class TaskActionsList(ListResource):
    def __init__(self, version: Version, assistant_sid: str, task_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid, 'task_sid': task_sid,  }
        self._uri = ''
        


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.Understand.TaskActionsList>'

