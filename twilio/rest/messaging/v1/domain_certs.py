"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Messaging
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


class DomainCertsContext(InstanceContext):
    def __init__(self, version: Version, domain_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'domain_sid': domain_sid,  }
        self._uri = '/LinkShortening/Domains/${domain_sid}/Certificate'
        
    
    def delete(self):
        
        

        """
        Deletes the DomainCertsInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the DomainCertsInstance

        :returns: The fetched DomainCertsInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return DomainCertsInstance(self._version, payload, domain_sid=self._solution['domain_sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return DomainCertsInstance(self._version, payload, domain_sid=self._solution['domain_sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.DomainCertsContext>'



class DomainCertsInstance(InstanceResource):
    def __init__(self, version, payload, domain_sid: str):
        super().__init__(version)
        self._properties = { 
            'domain_sid' : payload.get('domain_sid'),
            'date_updated' : payload.get('date_updated'),
            'date_expires' : payload.get('date_expires'),
            'date_created' : payload.get('date_created'),
            'domain_name' : payload.get('domain_name'),
            'certificate_sid' : payload.get('certificate_sid'),
            'url' : payload.get('url'),
            'validated' : payload.get('validated'),
        }

        self._context = None
        self._solution = {
            'domain_sid': domain_sid or self._properties['domain_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = DomainCertsContext(
                self._version,
                domain_sid=self._solution['domain_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.DomainCertsInstance {}>'.format(context)



class DomainCertsListInstance(ListResource):
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
        return '<Twilio.Api.V1.DomainCertsListInstance>'

