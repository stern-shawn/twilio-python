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

from twilio.base.page import Page

# 


class BrandVettingContext(InstanceContext):
    def __init__(self, version: Version, brand_sid: str, brand_vetting_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'brand_sid': brand_sid, 'brand_vetting_sid': brand_vetting_sid,  }
        self._uri = '/a2p/BrandRegistrations/${brand_sid}/Vettings/${brand_vetting_sid}'
        
    
    def fetch(self):
        
        """
        Fetch the BrandVettingInstance

        :returns: The fetched BrandVettingInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return BrandVettingInstance(self._version, payload, brand_sid=self._solution['brand_sid'], brand_vetting_sid=self._solution['brand_vetting_sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.BrandVettingContext>'



class BrandVettingInstance(InstanceResource):
    def __init__(self, version, payload, brand_sid: str, brand_vetting_sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'brand_sid' : payload.get('brand_sid'),
            'brand_vetting_sid' : payload.get('brand_vetting_sid'),
            'date_updated' : payload.get('date_updated'),
            'date_created' : payload.get('date_created'),
            'vetting_id' : payload.get('vetting_id'),
            'vetting_class' : payload.get('vetting_class'),
            'vetting_status' : payload.get('vetting_status'),
            'vetting_provider' : payload.get('vetting_provider'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'brand_sid': brand_sid or self._properties['brand_sid'],'brand_vetting_sid': brand_vetting_sid or self._properties['brand_vetting_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = BrandVettingContext(
                self._version,
                brand_sid=self._solution['brand_sid'],brand_vetting_sid=self._solution['brand_vetting_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.BrandVettingInstance {}>'.format(context)



class BrandVettingListInstance(ListResource):
    def __init__(self, version: Version, brand_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'brand_sid': brand_sid,  }
        self._uri = '/a2p/BrandRegistrations/${brand_sid}/Vettings'
        
    
    """
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return BrandVettingInstance(self._version, payload, brand_sid=self._solution['brand_sid'])
        
    """
    
    """
    def page(self, vetting_provider, page_size):
        
        data = values.of({
            'vetting_provider': vetting_provider,'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return BrandVettingPage(self._version, payload, brand_sid=self._solution['brand_sid'], )
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.BrandVettingListInstance>'

