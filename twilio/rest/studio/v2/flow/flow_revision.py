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

# 


class FlowRevisionContext(InstanceContext):
    def __init__(self, version: Version, sid: str, revision: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid, 'revision': revision,  }
        self._uri = '/Flows/${sid}/Revisions/${revision}'
        
    
    def fetch(self):
        
        """
        Fetch the FlowRevisionInstance

        :returns: The fetched FlowRevisionInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return FlowRevisionInstance(self._version, payload, sid=self._solution['sid'], revision=self._solution['revision'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.FlowRevisionContext>'



class FlowRevisionInstance(InstanceResource):
    def __init__(self, version, payload, sid: str, revision: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'friendly_name' : payload.get('friendly_name'),
            'definition' : payload.get('definition'),
            'status' : payload.get('status'),
            'revision' : payload.get('revision'),
            'commit_message' : payload.get('commit_message'),
            'valid' : payload.get('valid'),
            'errors' : payload.get('errors'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid'],'revision': revision or self._properties['revision'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = FlowRevisionContext(
                self._version,
                sid=self._solution['sid'],revision=self._solution['revision'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2.FlowRevisionInstance {}>'.format(context)



class FlowRevisionList(ListResource):
    def __init__(self, version: Version, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid,  }
        self._uri = '/Flows/${sid}/Revisions'
        

    """
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return FlowRevisionPage(self._version, payload, sid=self._solution['sid'], )
    """


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.FlowRevisionList>'

