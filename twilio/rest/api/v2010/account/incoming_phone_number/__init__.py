"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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
from twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on import AssignedAddOnList
from twilio.rest.api.v2010.account.incoming_phone_number.local import LocalList
from twilio.rest.api.v2010.account.incoming_phone_number.mobile import MobileList
from twilio.rest.api.v2010.account.incoming_phone_number.toll_free import TollFreeList


class IncomingPhoneNumberList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the IncomingPhoneNumberList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resources to read.
        
        :returns: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberList
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/${account_sid}/IncomingPhoneNumbers.json'.format(**self._solution)
        
        self._local = None
        self._mobile = None
        self._toll_free = None
        
    
    
    
    
    def create(self, api_version=values.unset, friendly_name=values.unset, sms_application_sid=values.unset, sms_fallback_method=values.unset, sms_fallback_url=values.unset, sms_method=values.unset, sms_url=values.unset, status_callback=values.unset, status_callback_method=values.unset, voice_application_sid=values.unset, voice_caller_id_lookup=values.unset, voice_fallback_method=values.unset, voice_fallback_url=values.unset, voice_method=values.unset, voice_url=values.unset, emergency_status=values.unset, emergency_address_sid=values.unset, trunk_sid=values.unset, identity_sid=values.unset, address_sid=values.unset, voice_receive_mode=values.unset, bundle_sid=values.unset, phone_number=values.unset, area_code=values.unset):
        """
        Create the IncomingPhoneNumberInstance
        :param str api_version: The API version to use for incoming calls made to the new phone number. The default is `2010-04-01`.
        :param str friendly_name: A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, this is a formatted version of the new phone number.
        :param str sms_application_sid: The SID of the application that should handle SMS messages sent to the new phone number. If an `sms_application_sid` is present, we ignore all of the `sms_*_url` urls and use those set on the application.
        :param str sms_fallback_method: The HTTP method that we should use to call `sms_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.
        :param str sms_fallback_url: The URL that we should call when an error occurs while requesting or executing the TwiML defined by `sms_url`.
        :param str sms_method: The HTTP method that we should use to call `sms_url`. Can be: `GET` or `POST` and defaults to `POST`.
        :param str sms_url: The URL we should call when the new phone number receives an incoming SMS message.
        :param str status_callback: The URL we should call using the `status_callback_method` to send status information to your application.
        :param str status_callback_method: The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
        :param str voice_application_sid: The SID of the application we should use to handle calls to the new phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use only those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa.
        :param bool voice_caller_id_lookup: Whether to lookup the caller's name from the CNAM database and post it to your app. Can be: `true` or `false` and defaults to `false`.
        :param str voice_fallback_method: The HTTP method that we should use to call `voice_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.
        :param str voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`.
        :param str voice_method: The HTTP method that we should use to call `voice_url`. Can be: `GET` or `POST` and defaults to `POST`.
        :param str voice_url: The URL that we should call to answer a call to the new phone number. The `voice_url` will not be called if a `voice_application_sid` or a `trunk_sid` is set.
        :param IncomingPhoneNumberEmergencyStatus emergency_status: 
        :param str emergency_address_sid: The SID of the emergency address configuration to use for emergency calling from the new phone number.
        :param str trunk_sid: The SID of the Trunk we should use to handle calls to the new phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa.
        :param str identity_sid: The SID of the Identity resource that we should associate with the new phone number. Some regions require an identity to meet local regulations.
        :param str address_sid: The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations.
        :param IncomingPhoneNumberVoiceReceiveMode voice_receive_mode: 
        :param str bundle_sid: The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations.
        :param str phone_number: The phone number to purchase specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234.
        :param str area_code: The desired area code for your new incoming phone number. Can be any three-digit, US or Canada area code. We will provision an available phone number within this area code for you. **You must provide an `area_code` or a `phone_number`.** (US and Canada only).
        
        :returns: The created IncomingPhoneNumberInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberInstance
        """
        data = values.of({ 
            'ApiVersion': api_version,
            'FriendlyName': friendly_name,
            'SmsApplicationSid': sms_application_sid,
            'SmsFallbackMethod': sms_fallback_method,
            'SmsFallbackUrl': sms_fallback_url,
            'SmsMethod': sms_method,
            'SmsUrl': sms_url,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'VoiceApplicationSid': voice_application_sid,
            'VoiceCallerIdLookup': voice_caller_id_lookup,
            'VoiceFallbackMethod': voice_fallback_method,
            'VoiceFallbackUrl': voice_fallback_url,
            'VoiceMethod': voice_method,
            'VoiceUrl': voice_url,
            'EmergencyStatus': emergency_status,
            'EmergencyAddressSid': emergency_address_sid,
            'TrunkSid': trunk_sid,
            'IdentitySid': identity_sid,
            'AddressSid': address_sid,
            'VoiceReceiveMode': voice_receive_mode,
            'BundleSid': bundle_sid,
            'PhoneNumber': phone_number,
            'AreaCode': area_code,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return IncomingPhoneNumberInstance(self._version, payload, account_sid=self._solution['account_sid'])
    
    
    def stream(self, beta=values.unset, friendly_name=values.unset, phone_number=values.unset, origin=values.unset, limit=None, page_size=None):
        """
        Streams IncomingPhoneNumberInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param bool beta: Whether to include phone numbers new to the Twilio platform. Can be: `true` or `false` and the default is `true`.
        :param str friendly_name: A string that identifies the IncomingPhoneNumber resources to read.
        :param str phone_number: The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use '*' as a wildcard for any digit.
        :param str origin: Whether to include phone numbers based on their origin. Can be: `twilio` or `hosted`. By default, phone numbers of all origin are included.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            beta=beta,
            friendly_name=friendly_name,
            phone_number=phone_number,
            origin=origin,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, beta=values.unset, friendly_name=values.unset, phone_number=values.unset, origin=values.unset, limit=None, page_size=None):
        """
        Lists IncomingPhoneNumberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param bool beta: Whether to include phone numbers new to the Twilio platform. Can be: `true` or `false` and the default is `true`.
        :param str friendly_name: A string that identifies the IncomingPhoneNumber resources to read.
        :param str phone_number: The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use '*' as a wildcard for any digit.
        :param str origin: Whether to include phone numbers based on their origin. Can be: `twilio` or `hosted`. By default, phone numbers of all origin are included.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberInstance]
        """
        return list(self.stream(
            beta=beta,
            friendly_name=friendly_name,
            phone_number=phone_number,
            origin=origin,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, beta=values.unset, friendly_name=values.unset, phone_number=values.unset, origin=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of IncomingPhoneNumberInstance records from the API.
        Request is executed immediately
        
        :param bool beta: Whether to include phone numbers new to the Twilio platform. Can be: `true` or `false` and the default is `true`.
        :param str friendly_name: A string that identifies the IncomingPhoneNumber resources to read.
        :param str phone_number: The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use '*' as a wildcard for any digit.
        :param str origin: Whether to include phone numbers based on their origin. Can be: `twilio` or `hosted`. By default, phone numbers of all origin are included.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of IncomingPhoneNumberInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberPage
        """
        data = values.of({ 
            'Beta': beta,
            'FriendlyName': friendly_name,
            'PhoneNumber': phone_number,
            'Origin': origin,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return IncomingPhoneNumberPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of IncomingPhoneNumberInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of IncomingPhoneNumberInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return IncomingPhoneNumberPage(self._version, response, self._solution)


    @property
    def local(self):
        """
        Access the local

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.LocalList
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.LocalList
        """
        if self._local is None:
            self._local = LocalList(self._version, account_sid=self._solution['account_sid'])
        return self.local

    @property
    def mobile(self):
        """
        Access the mobile

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.MobileList
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.MobileList
        """
        if self._mobile is None:
            self._mobile = MobileList(self._version, account_sid=self._solution['account_sid'])
        return self.mobile

    @property
    def toll_free(self):
        """
        Access the toll_free

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.TollFreeList
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.TollFreeList
        """
        if self._toll_free is None:
            self._toll_free = TollFreeList(self._version, account_sid=self._solution['account_sid'])
        return self.toll_free

    def get(self, sid):
        """
        Constructs a IncomingPhoneNumberContext
        
        :param sid: The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to update.
        
        :returns: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberContext
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberContext
        """
        return IncomingPhoneNumberContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a IncomingPhoneNumberContext
        
        :param sid: The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to update.
        
        :returns: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberContext
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberContext
        """
        return IncomingPhoneNumberContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.IncomingPhoneNumberList>'










class IncomingPhoneNumberPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the IncomingPhoneNumberPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberPage
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of IncomingPhoneNumberInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberInstance
        """
        return IncomingPhoneNumberInstance(self._version, payload, account_sid=self._solution['account_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.IncomingPhoneNumberPage>'





class IncomingPhoneNumberContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'sid': sid,  }
        self._uri = '/Accounts/${account_sid}/IncomingPhoneNumbers/${sid}.json'
        
        self._assigned_add_ons = None
    
    def delete(self):
        
        

        """
        Deletes the IncomingPhoneNumberInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the IncomingPhoneNumberInstance

        :returns: The fetched IncomingPhoneNumberInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return IncomingPhoneNumberInstance(self._version, payload, account_sid=self._solution['account_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, account_sid, api_version, friendly_name, sms_application_sid, sms_fallback_method, sms_fallback_url, sms_method, sms_url, status_callback, status_callback_method, voice_application_sid, voice_caller_id_lookup, voice_fallback_method, voice_fallback_url, voice_method, voice_url, emergency_status, emergency_address_sid, trunk_sid, voice_receive_mode, identity_sid, address_sid, bundle_sid):
        data = values.of({
            'account_sid': account_sid,'api_version': api_version,'friendly_name': friendly_name,'sms_application_sid': sms_application_sid,'sms_fallback_method': sms_fallback_method,'sms_fallback_url': sms_fallback_url,'sms_method': sms_method,'sms_url': sms_url,'status_callback': status_callback,'status_callback_method': status_callback_method,'voice_application_sid': voice_application_sid,'voice_caller_id_lookup': voice_caller_id_lookup,'voice_fallback_method': voice_fallback_method,'voice_fallback_url': voice_fallback_url,'voice_method': voice_method,'voice_url': voice_url,'emergency_status': emergency_status,'emergency_address_sid': emergency_address_sid,'trunk_sid': trunk_sid,'voice_receive_mode': voice_receive_mode,'identity_sid': identity_sid,'address_sid': address_sid,'bundle_sid': bundle_sid,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return IncomingPhoneNumberInstance(self._version, payload, account_sid=self._solution['account_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.IncomingPhoneNumberContext>'



class IncomingPhoneNumberInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'address_sid' : payload.get('address_sid'),
            'address_requirements' : payload.get('address_requirements'),
            'api_version' : payload.get('api_version'),
            'beta' : payload.get('beta'),
            'capabilities' : payload.get('capabilities'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'friendly_name' : payload.get('friendly_name'),
            'identity_sid' : payload.get('identity_sid'),
            'phone_number' : payload.get('phone_number'),
            'origin' : payload.get('origin'),
            'sid' : payload.get('sid'),
            'sms_application_sid' : payload.get('sms_application_sid'),
            'sms_fallback_method' : payload.get('sms_fallback_method'),
            'sms_fallback_url' : payload.get('sms_fallback_url'),
            'sms_method' : payload.get('sms_method'),
            'sms_url' : payload.get('sms_url'),
            'status_callback' : payload.get('status_callback'),
            'status_callback_method' : payload.get('status_callback_method'),
            'trunk_sid' : payload.get('trunk_sid'),
            'uri' : payload.get('uri'),
            'voice_receive_mode' : payload.get('voice_receive_mode'),
            'voice_application_sid' : payload.get('voice_application_sid'),
            'voice_caller_id_lookup' : payload.get('voice_caller_id_lookup'),
            'voice_fallback_method' : payload.get('voice_fallback_method'),
            'voice_fallback_url' : payload.get('voice_fallback_url'),
            'voice_method' : payload.get('voice_method'),
            'voice_url' : payload.get('voice_url'),
            'emergency_status' : payload.get('emergency_status'),
            'emergency_address_sid' : payload.get('emergency_address_sid'),
            'emergency_address_status' : payload.get('emergency_address_status'),
            'bundle_sid' : payload.get('bundle_sid'),
            'status' : payload.get('status'),
        }

        self._context = None
        self._solution = {
            'account_sid': account_sid or self._properties['account_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = IncomingPhoneNumberContext(
                self._version,
                account_sid=self._solution['account_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def assigned_add_ons(self):
        return self._proxy.assigned_add_ons
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.IncomingPhoneNumberInstance {}>'.format(context)



