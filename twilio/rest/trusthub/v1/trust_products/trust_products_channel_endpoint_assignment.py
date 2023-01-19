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

# 


class TrustProductsChannelEndpointAssignmentContext(InstanceContext):
    def __init__(self, version: Version, trust_product_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'trust_product_sid': trust_product_sid, 'sid': sid,  }
        self._uri = '/TrustProducts/${trust_product_sid}/ChannelEndpointAssignments/${sid}'
        
    
    def delete(self):
        
        

        """
        Deletes the TrustProductsChannelEndpointAssignmentInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the TrustProductsChannelEndpointAssignmentInstance

        :returns: The fetched TrustProductsChannelEndpointAssignmentInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return TrustProductsChannelEndpointAssignmentInstance(self._version, payload, trust_product_sid=self._solution['trust_product_sid'], sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.TrustProductsChannelEndpointAssignmentContext>'



class TrustProductsChannelEndpointAssignmentInstance(InstanceResource):
    def __init__(self, version, payload, trust_product_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'trust_product_sid' : payload.get('trust_product_sid'),
            'account_sid' : payload.get('account_sid'),
            'channel_endpoint_type' : payload.get('channel_endpoint_type'),
            'channel_endpoint_sid' : payload.get('channel_endpoint_sid'),
            'date_created' : payload.get('date_created'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'trust_product_sid': trust_product_sid or self._properties['trust_product_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = TrustProductsChannelEndpointAssignmentContext(
                self._version,
                trust_product_sid=self._solution['trust_product_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.TrustProductsChannelEndpointAssignmentInstance {}>'.format(context)



class TrustProductsChannelEndpointAssignmentListInstance(ListResource):
    def __init__(self, version: Version, trust_product_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'trust_product_sid': trust_product_sid,  }
        self._uri = '/TrustProducts/${trust_product_sid}/ChannelEndpointAssignments'
        
    
    """
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return TrustProductsChannelEndpointAssignmentInstance(self._version, payload, trust_product_sid=self._solution['trust_product_sid'])
        
    """
    
    """
    def page(self, channel_endpoint_sid, channel_endpoint_sids, page_size):
        
        data = values.of({
            'channel_endpoint_sid': channel_endpoint_sid,'channel_endpoint_sids': channel_endpoint_sids,'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return TrustProductsChannelEndpointAssignmentPage(self._version, payload, trust_product_sid=self._solution['trust_product_sid'], )
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.TrustProductsChannelEndpointAssignmentListInstance>'

