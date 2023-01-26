"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trusthub
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

# from twilio.rest.trust_products.trust_products_channel_endpoint_assignment import TrustProductsChannelEndpointAssignmentListInstancefrom twilio.rest.trust_products.trust_products_entity_assignments import TrustProductsEntityAssignmentsListInstancefrom twilio.rest.trust_products.trust_products_evaluations import TrustProductsEvaluationsListInstance


class TrustProductsContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid,  }
        self._uri = '/TrustProducts/${sid}'
        
        self._trust_products_channel_endpoint_assignment = None
        self._trust_products_entity_assignments = None
        self._trust_products_evaluations = None
    
    def delete(self):
        
        

        """
        Deletes the TrustProductsInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the TrustProductsInstance

        :returns: The fetched TrustProductsInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return TrustProductsInstance(self._version, payload, sid=self._solution['sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return TrustProductsInstance(self._version, payload, sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.TrustProductsContext>'



class TrustProductsInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'policy_sid' : payload.get('policy_sid'),
            'friendly_name' : payload.get('friendly_name'),
            'status' : payload.get('status'),
            'valid_until' : payload.get('valid_until'),
            'email' : payload.get('email'),
            'status_callback' : payload.get('status_callback'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
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
            self._context = TrustProductsContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def trust_products_channel_endpoint_assignment(self):
        return self._proxy.trust_products_channel_endpoint_assignment
    @property
    def trust_products_entity_assignments(self):
        return self._proxy.trust_products_entity_assignments
    @property
    def trust_products_evaluations(self):
        return self._proxy.trust_products_evaluations
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.TrustProductsInstance {}>'.format(context)



class TrustProductsListInstance(ListResource):
    def __init__(self, version: Version):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/TrustProducts'
        
    
    """
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return TrustProductsInstance(self._version, payload, )
        
    """
    
    """
    def page(self, status, friendly_name, policy_sid, page_size):
        
        data = values.of({
            'status': status,'friendly_name': friendly_name,'policy_sid': policy_sid,'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return TrustProductsPage(self._version, payload, )
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.TrustProductsListInstance>'
