"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Autopilot
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


class FieldContext(InstanceContext):
    def __init__(self, version: Version, assistant_sid: str, task_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid, 'task_sid': task_sid, 'sid': sid,  }
        self._uri = '/Assistants/${assistant_sid}/Tasks/${task_sid}/Fields/${sid}'
        
    
    def delete(self):
        
        

        """
        Deletes the FieldInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the FieldInstance

        :returns: The fetched FieldInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return FieldInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], task_sid=self._solution['task_sid'], sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.FieldContext>'



class FieldInstance(InstanceResource):
    def __init__(self, version, payload, assistant_sid: str, task_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'field_type' : payload.get('field_type'),
            'task_sid' : payload.get('task_sid'),
            'assistant_sid' : payload.get('assistant_sid'),
            'sid' : payload.get('sid'),
            'unique_name' : payload.get('unique_name'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'assistant_sid': assistant_sid or self._properties['assistant_sid'],'task_sid': task_sid or self._properties['task_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = FieldContext(
                self._version,
                assistant_sid=self._solution['assistant_sid'],task_sid=self._solution['task_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.FieldInstance {}>'.format(context)



class FieldListInstance(ListResource):
    def __init__(self, version: Version, assistant_sid: str, task_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid, 'task_sid': task_sid,  }
        self._uri = '/Assistants/${assistant_sid}/Tasks/${task_sid}/Fields'
        
    
    """
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return FieldInstance(self._version, payload, assistant_sid=self._solution['assistant_sid']task_sid=self._solution['task_sid'])
        
    """
    
    """
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return FieldPage(self._version, payload, assistant_sid=self._solution['assistant_sid'], task_sid=self._solution['task_sid'], )
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.FieldListInstance>'

