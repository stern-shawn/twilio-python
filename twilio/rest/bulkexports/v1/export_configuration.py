"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Bulkexports
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


class ExportConfigurationContext(InstanceContext):
    def __init__(self, version: Version, resource_type: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'resource_type': resource_type,  }
        self._uri = '/Exports/${resource_type}/Configuration'
        
    
    def fetch(self):
        
        """
        Fetch the ExportConfigurationInstance

        :returns: The fetched ExportConfigurationInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ExportConfigurationInstance(self._version, payload, resource_type=self._solution['resource_type'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return ExportConfigurationInstance(self._version, payload, resource_type=self._solution['resource_type'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ExportConfigurationContext>'



class ExportConfigurationInstance(InstanceResource):
    def __init__(self, version, payload, resource_type: str):
        super().__init__(version)
        self._properties = { 
            'enabled' : payload.get('enabled'),
            'webhook_url' : payload.get('webhook_url'),
            'webhook_method' : payload.get('webhook_method'),
            'resource_type' : payload.get('resource_type'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'resource_type': resource_type or self._properties['resource_type'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ExportConfigurationContext(
                self._version,
                resource_type=self._solution['resource_type'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.ExportConfigurationInstance {}>'.format(context)



class ExportConfigurationListInstance(ListResource):
    def __init__(self, version: Version):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = ''
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ExportConfigurationListInstance>'

