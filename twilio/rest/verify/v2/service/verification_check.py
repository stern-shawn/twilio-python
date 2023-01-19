"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
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



class VerificationCheckInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'service_sid' : payload.get('service_sid'),
            'account_sid' : payload.get('account_sid'),
            'to' : payload.get('to'),
            'channel' : payload.get('channel'),
            'status' : payload.get('status'),
            'valid' : payload.get('valid'),
            'amount' : payload.get('amount'),
            'payee' : payload.get('payee'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'sna_attempts_error_codes' : payload.get('sna_attempts_error_codes'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = VerificationCheckContext(
                self._version,
                service_sid=self._solution['service_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2.VerificationCheckInstance {}>'.format(context)



class VerificationCheckListInstance(ListResource):
    def __init__(self, version: Version, service_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/${service_sid}/VerificationCheck'
        
    
    """
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return VerificationCheckInstance(self._version, payload, service_sid=self._solution['service_sid'])
        
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.VerificationCheckListInstance>'

