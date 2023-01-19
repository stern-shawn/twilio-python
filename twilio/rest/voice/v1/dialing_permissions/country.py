"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Voice
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

# from twilio.rest.country.highrisk_special_prefix import HighriskSpecialPrefixListInstance


class CountryContext(InstanceContext):
    def __init__(self, version: Version, iso_code: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'iso_code': iso_code,  }
        self._uri = '/DialingPermissions/Countries/${iso_code}'
        
        self._highrisk_special_prefixes = None
    
    def fetch(self):
        
        """
        Fetch the CountryInstance

        :returns: The fetched CountryInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return CountryInstance(self._version, payload, iso_code=self._solution['iso_code'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.CountryContext>'



class CountryInstance(InstanceResource):
    def __init__(self, version, payload, iso_code: str):
        super().__init__(version)
        self._properties = { 
            'iso_code' : payload.get('iso_code'),
            'name' : payload.get('name'),
            'continent' : payload.get('continent'),
            'country_codes' : payload.get('country_codes'),
            'low_risk_numbers_enabled' : payload.get('low_risk_numbers_enabled'),
            'high_risk_special_numbers_enabled' : payload.get('high_risk_special_numbers_enabled'),
            'high_risk_tollfraud_numbers_enabled' : payload.get('high_risk_tollfraud_numbers_enabled'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'iso_code': iso_code or self._properties['iso_code'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = CountryContext(
                self._version,
                iso_code=self._solution['iso_code'],
            )
        return self._context

    @property
    def highrisk_special_prefixes(self):
        return self._proxy.highrisk_special_prefixes
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.CountryInstance {}>'.format(context)



class CountryListInstance(ListResource):
    def __init__(self, version: Version):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/DialingPermissions/Countries'
        
    
    """
    def page(self, iso_code, continent, country_code, low_risk_numbers_enabled, high_risk_special_numbers_enabled, high_risk_tollfraud_numbers_enabled, page_size):
        
        data = values.of({
            'iso_code': iso_code,'continent': continent,'country_code': country_code,'low_risk_numbers_enabled': low_risk_numbers_enabled,'high_risk_special_numbers_enabled': high_risk_special_numbers_enabled,'high_risk_tollfraud_numbers_enabled': high_risk_tollfraud_numbers_enabled,'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return CountryPage(self._version, payload, )
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.CountryListInstance>'

