r"""
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



class VerificationList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the VerificationList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the verification [Service](https://www.twilio.com/docs/verify/api/service) to create the resource under.
        
        :returns: twilio.rest.verify.v2.service.verification.VerificationList
        :rtype: twilio.rest.verify.v2.service.verification.VerificationList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/{service_sid}/Verifications'.format(**self._solution)
        
        
    
    
    
    def create(self, to, channel, custom_friendly_name=values.unset, custom_message=values.unset, send_digits=values.unset, locale=values.unset, custom_code=values.unset, amount=values.unset, payee=values.unset, rate_limits=values.unset, channel_configuration=values.unset, app_hash=values.unset, template_sid=values.unset, template_custom_substitutions=values.unset, device_ip=values.unset):
        """
        Create the VerificationInstance

        :param str to: The phone number or [email](https://www.twilio.com/docs/verify/email) to verify. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
        :param str channel: The verification method to use. One of: [`email`](https://www.twilio.com/docs/verify/email), `sms`, `whatsapp`, `call`, `sna` or `auto`.
        :param str custom_friendly_name: A custom user defined friendly name that overwrites the existing one in the verification message
        :param str custom_message: The text of a custom message to use for the verification.
        :param str send_digits: The digits to send after a phone call is answered, for example, to dial an extension. For more information, see the Programmable Voice documentation of [sendDigits](https://www.twilio.com/docs/voice/twiml/number#attributes-sendDigits).
        :param str locale: Locale will automatically resolve based on phone number country code for SMS, WhatsApp, and call channel verifications. It will fallback to English or the template’s default translation if the selected translation is not available. This parameter will override the automatic locale resolution. [See supported languages and more information here](https://www.twilio.com/docs/verify/supported-languages).
        :param str custom_code: A pre-generated code to use for verification. The code can be between 4 and 10 characters, inclusive.
        :param str amount: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
        :param str payee: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
        :param object rate_limits: The custom key-value pairs of Programmable Rate Limits. Keys correspond to `unique_name` fields defined when [creating your Rate Limit](https://www.twilio.com/docs/verify/api/service-rate-limits). Associated value pairs represent values in the request that you are rate limiting on. You may include multiple Rate Limit values in each request.
        :param object channel_configuration: [`email`](https://www.twilio.com/docs/verify/email) channel configuration in json format. The fields 'from' and 'from_name' are optional but if included the 'from' field must have a valid email address.
        :param str app_hash: Your [App Hash](https://developers.google.com/identity/sms-retriever/verify#computing_your_apps_hash_string) to be appended at the end of your verification SMS body. Applies only to SMS. Example SMS body: `<#> Your AppName verification code is: 1234 He42w354ol9`.
        :param str template_sid: The message [template](https://www.twilio.com/docs/verify/api/templates). If provided, will override the default template for the Service. SMS and Voice channels only.
        :param str template_custom_substitutions: A stringified JSON object in which the keys are the template's special variables and the values are the variables substitutions.
        :param str device_ip: The IP address of the client's device. If provided, it has to be a valid IPv4 or IPv6 address.
        
        :returns: The created VerificationInstance
        :rtype: twilio.rest.verify.v2.service.verification.VerificationInstance
        """
        data = values.of({ 
            'To': to,
            'Channel': channel,
            'CustomFriendlyName': custom_friendly_name,
            'CustomMessage': custom_message,
            'SendDigits': send_digits,
            'Locale': locale,
            'CustomCode': custom_code,
            'Amount': amount,
            'Payee': payee,
            'RateLimits': serialize.object(rate_limits),
            'ChannelConfiguration': serialize.object(channel_configuration),
            'AppHash': app_hash,
            'TemplateSid': template_sid,
            'TemplateCustomSubstitutions': template_custom_substitutions,
            'DeviceIp': device_ip,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return VerificationInstance(self._version, payload, service_sid=self._solution['service_sid'])

    async def create_async(self, to, channel, custom_friendly_name=values.unset, custom_message=values.unset, send_digits=values.unset, locale=values.unset, custom_code=values.unset, amount=values.unset, payee=values.unset, rate_limits=values.unset, channel_configuration=values.unset, app_hash=values.unset, template_sid=values.unset, template_custom_substitutions=values.unset, device_ip=values.unset):
        """
        Asynchronous coroutine to create the VerificationInstance

        :param str to: The phone number or [email](https://www.twilio.com/docs/verify/email) to verify. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
        :param str channel: The verification method to use. One of: [`email`](https://www.twilio.com/docs/verify/email), `sms`, `whatsapp`, `call`, `sna` or `auto`.
        :param str custom_friendly_name: A custom user defined friendly name that overwrites the existing one in the verification message
        :param str custom_message: The text of a custom message to use for the verification.
        :param str send_digits: The digits to send after a phone call is answered, for example, to dial an extension. For more information, see the Programmable Voice documentation of [sendDigits](https://www.twilio.com/docs/voice/twiml/number#attributes-sendDigits).
        :param str locale: Locale will automatically resolve based on phone number country code for SMS, WhatsApp, and call channel verifications. It will fallback to English or the template’s default translation if the selected translation is not available. This parameter will override the automatic locale resolution. [See supported languages and more information here](https://www.twilio.com/docs/verify/supported-languages).
        :param str custom_code: A pre-generated code to use for verification. The code can be between 4 and 10 characters, inclusive.
        :param str amount: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
        :param str payee: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
        :param object rate_limits: The custom key-value pairs of Programmable Rate Limits. Keys correspond to `unique_name` fields defined when [creating your Rate Limit](https://www.twilio.com/docs/verify/api/service-rate-limits). Associated value pairs represent values in the request that you are rate limiting on. You may include multiple Rate Limit values in each request.
        :param object channel_configuration: [`email`](https://www.twilio.com/docs/verify/email) channel configuration in json format. The fields 'from' and 'from_name' are optional but if included the 'from' field must have a valid email address.
        :param str app_hash: Your [App Hash](https://developers.google.com/identity/sms-retriever/verify#computing_your_apps_hash_string) to be appended at the end of your verification SMS body. Applies only to SMS. Example SMS body: `<#> Your AppName verification code is: 1234 He42w354ol9`.
        :param str template_sid: The message [template](https://www.twilio.com/docs/verify/api/templates). If provided, will override the default template for the Service. SMS and Voice channels only.
        :param str template_custom_substitutions: A stringified JSON object in which the keys are the template's special variables and the values are the variables substitutions.
        :param str device_ip: The IP address of the client's device. If provided, it has to be a valid IPv4 or IPv6 address.
        
        :returns: The created VerificationInstance
        :rtype: twilio.rest.verify.v2.service.verification.VerificationInstance
        """
        data = values.of({ 
            'To': to,
            'Channel': channel,
            'CustomFriendlyName': custom_friendly_name,
            'CustomMessage': custom_message,
            'SendDigits': send_digits,
            'Locale': locale,
            'CustomCode': custom_code,
            'Amount': amount,
            'Payee': payee,
            'RateLimits': serialize.object(rate_limits),
            'ChannelConfiguration': serialize.object(channel_configuration),
            'AppHash': app_hash,
            'TemplateSid': template_sid,
            'TemplateCustomSubstitutions': template_custom_substitutions,
            'DeviceIp': device_ip,
        })
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data,)

        return VerificationInstance(self._version, payload, service_sid=self._solution['service_sid'])
    

    def get(self, sid):
        """
        Constructs a VerificationContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Verification resource to update.
        
        :returns: twilio.rest.verify.v2.service.verification.VerificationContext
        :rtype: twilio.rest.verify.v2.service.verification.VerificationContext
        """
        return VerificationContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a VerificationContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Verification resource to update.
        
        :returns: twilio.rest.verify.v2.service.verification.VerificationContext
        :rtype: twilio.rest.verify.v2.service.verification.VerificationContext
        """
        return VerificationContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.VerificationList>'

class VerificationContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the VerificationContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the verification [Service](https://www.twilio.com/docs/verify/api/service) to update the resource from.:param sid: The Twilio-provided string that uniquely identifies the Verification resource to update.

        :returns: twilio.rest.verify.v2.service.verification.VerificationContext
        :rtype: twilio.rest.verify.v2.service.verification.VerificationContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Verifications/{sid}'.format(**self._solution)
        
    
    
    def fetch(self):
        """
        Fetch the VerificationInstance
        

        :returns: The fetched VerificationInstance
        :rtype: twilio.rest.verify.v2.service.verification.VerificationInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return VerificationInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the VerificationInstance
        

        :returns: The fetched VerificationInstance
        :rtype: twilio.rest.verify.v2.service.verification.VerificationInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return VerificationInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
            
        )
    
    
    def update(self, status):
        """
        Update the VerificationInstance
        
        :params VerificationInstance.Status status: 

        :returns: The updated VerificationInstance
        :rtype: twilio.rest.verify.v2.service.verification.VerificationInstance
        """
        data = values.of({ 
            'Status': status,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return VerificationInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid']
        )

    async def update_async(self, status):
        """
        Asynchronous coroutine to update the VerificationInstance
        
        :params VerificationInstance.Status status: 

        :returns: The updated VerificationInstance
        :rtype: twilio.rest.verify.v2.service.verification.VerificationInstance
        """
        data = values.of({ 
            'Status': status,
        })
        

        payload = await self._version.update_async(method='POST', uri=self._uri, data=data,)

        return VerificationInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid']
        )
    
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.VerificationContext {}>'.format(context)

class VerificationInstance(InstanceResource):

    class Channel(object):
        SMS = "sms"
        CALL = "call"
        EMAIL = "email"
        WHATSAPP = "whatsapp"
        SNA = "sna"

    def __init__(self, version, payload, service_sid: str, sid: str=None):
        """
        Initialize the VerificationInstance
        :returns: twilio.rest.verify.v2.service.verification.VerificationInstance
        :rtype: twilio.rest.verify.v2.service.verification.VerificationInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'service_sid': payload.get('service_sid'),
            'account_sid': payload.get('account_sid'),
            'to': payload.get('to'),
            'channel': payload.get('channel'),
            'status': payload.get('status'),
            'valid': payload.get('valid'),
            'lookup': payload.get('lookup'),
            'amount': payload.get('amount'),
            'payee': payload.get('payee'),
            'send_code_attempts': payload.get('send_code_attempts'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'sna': payload.get('sna'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: VerificationContext for this VerificationInstance
        :rtype: twilio.rest.verify.v2.service.verification.VerificationContext
        """
        if self._context is None:
            self._context = VerificationContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Verification resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def service_sid(self):
        """
        :returns: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Verification resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def to(self):
        """
        :returns: The phone number or [email](https://www.twilio.com/docs/verify/email) being verified. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
        :rtype: str
        """
        return self._properties['to']
    
    @property
    def channel(self):
        """
        :returns: 
        :rtype: VerificationInstance.Channel
        """
        return self._properties['channel']
    
    @property
    def status(self):
        """
        :returns: The status of the verification. One of: `pending`, `approved`, or `canceled`
        :rtype: str
        """
        return self._properties['status']
    
    @property
    def valid(self):
        """
        :returns: Use \"status\" instead. Legacy property indicating whether the verification was successful.
        :rtype: bool
        """
        return self._properties['valid']
    
    @property
    def lookup(self):
        """
        :returns: Information about the phone number being verified.
        :rtype: dict
        """
        return self._properties['lookup']
    
    @property
    def amount(self):
        """
        :returns: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
        :rtype: str
        """
        return self._properties['amount']
    
    @property
    def payee(self):
        """
        :returns: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
        :rtype: str
        """
        return self._properties['payee']
    
    @property
    def send_code_attempts(self):
        """
        :returns: An array of verification attempt objects containing the channel attempted and the channel-specific transaction SID.
        :rtype: list[object]
        """
        return self._properties['send_code_attempts']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def sna(self):
        """
        :returns: The set of fields used for a silent network auth (`sna`) verification. Contains a single field with the URL to be invoked to verify the phone number.
        :rtype: dict
        """
        return self._properties['sna']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Verification resource.
        :rtype: str
        """
        return self._properties['url']
    
    
    def fetch(self):
        """
        Fetch the VerificationInstance
        

        :returns: The fetched VerificationInstance
        :rtype: twilio.rest.verify.v2.service.verification.VerificationInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the VerificationInstance
        

        :returns: The fetched VerificationInstance
        :rtype: twilio.rest.verify.v2.service.verification.VerificationInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, status):
        """
        Update the VerificationInstance
        
        :params VerificationInstance.Status status: 

        :returns: The updated VerificationInstance
        :rtype: twilio.rest.verify.v2.service.verification.VerificationInstance
        """
        return self._proxy.update(status=status, )

    async def update_async(self, status):
        """
        Asynchronous coroutine to update the VerificationInstance
        
        :params VerificationInstance.Status status: 

        :returns: The updated VerificationInstance
        :rtype: twilio.rest.verify.v2.service.verification.VerificationInstance
        """
        return await self._proxy.update_async(status=status, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.VerificationInstance {}>'.format(context)


