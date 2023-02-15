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

# from twilio.rest.brand_registration.brand_vetting import BrandVettingListInstance


class BrandRegistrationContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid,  }
        self._uri = '/a2p/BrandRegistrations/${sid}'
        
        self._brand_vettings = None
    
    def fetch(self):
        
        """
        Fetch the BrandRegistrationInstance

        :returns: The fetched BrandRegistrationInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return BrandRegistrationInstance(self._version, payload, sid=self._solution['sid'], )
        

        
    
    def update(self):
        data = values.of({
            
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return BrandRegistrationInstance(self._version, payload, sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.BrandRegistrationContext>'



class BrandRegistrationInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'customer_profile_bundle_sid' : payload.get('customer_profile_bundle_sid'),
            'a2p_profile_bundle_sid' : payload.get('a2p_profile_bundle_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'brand_type' : payload.get('brand_type'),
            'status' : payload.get('status'),
            'tcr_id' : payload.get('tcr_id'),
            'failure_reason' : payload.get('failure_reason'),
            'url' : payload.get('url'),
            'brand_score' : payload.get('brand_score'),
            'brand_feedback' : payload.get('brand_feedback'),
            'identity_status' : payload.get('identity_status'),
            'russell_3000' : payload.get('russell_3000'),
            'government_entity' : payload.get('government_entity'),
            'tax_exempt_status' : payload.get('tax_exempt_status'),
            'skip_automatic_sec_vet' : payload.get('skip_automatic_sec_vet'),
            'mock' : payload.get('mock'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = BrandRegistrationContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def brand_vettings(self):
        return self._proxy.brand_vettings
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.BrandRegistrationInstance {}>'.format(context)



class BrandRegistrationList(ListResource):
    def __init__(self, version: Version):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/a2p/BrandRegistrations'
        

    """
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return BrandRegistrationInstance(self._version, payload, )
        
    """

    """
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return BrandRegistrationPage(self._version, payload, )
    """


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.BrandRegistrationList>'

