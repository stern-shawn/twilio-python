r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Lookups
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Any, Dict, List, Optional, Union
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class PhoneNumberInstance(InstanceResource):
    class ValidationError(object):
        TOO_SHORT = "TOO_SHORT"
        TOO_LONG = "TOO_LONG"
        INVALID_BUT_POSSIBLE = "INVALID_BUT_POSSIBLE"
        INVALID_COUNTRY_CODE = "INVALID_COUNTRY_CODE"
        INVALID_LENGTH = "INVALID_LENGTH"
        NOT_A_NUMBER = "NOT_A_NUMBER"

    """
    :ivar calling_country_code: International dialing prefix of the phone number defined in the E.164 standard.
    :ivar country_code: The phone number's [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    :ivar phone_number: The phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
    :ivar national_format: The phone number in [national format](https://en.wikipedia.org/wiki/National_conventions_for_writing_telephone_numbers).
    :ivar valid: Boolean which indicates if the phone number is in a valid range that can be freely assigned by a carrier to a user.
    :ivar validation_errors: Contains reasons why a phone number is invalid. Possible values: TOO_SHORT, TOO_LONG, INVALID_BUT_POSSIBLE, INVALID_COUNTRY_CODE, INVALID_LENGTH, NOT_A_NUMBER.
    :ivar caller_name: An object that contains caller name information based on [CNAM](https://support.twilio.com/hc/en-us/articles/360051670533-Getting-Started-with-CNAM-Caller-ID).
    :ivar sim_swap: An object that contains information on the last date the subscriber identity module (SIM) was changed for a mobile phone number.
    :ivar call_forwarding: An object that contains information on the unconditional call forwarding status of mobile phone number.
    :ivar live_activity: An object that contains live activity information for a mobile phone number.
    :ivar line_type_intelligence: An object that contains line type information including the carrier name, mobile country code, and mobile network code.
    :ivar identity_match: An object that contains identity match information. The result of comparing user-provided information including name, address, date of birth, national ID, against authoritative phone-based data sources
    :ivar sms_pumping_risk: An object that contains information on if a phone number has been currently or previously blocked by Verify Fraud Guard for receiving malicious SMS pumping traffic as well as other signals associated with risky carriers and low conversion rates.
    :ivar disposable_phone_number_risk: An object that contains information on if a mobile phone number could be a disposable or burner number.
    :ivar url: The absolute URL of the resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        phone_number: Optional[str] = None,
    ):
        super().__init__(version)

        self.calling_country_code: Optional[str] = payload.get("calling_country_code")
        self.country_code: Optional[str] = payload.get("country_code")
        self.phone_number: Optional[str] = payload.get("phone_number")
        self.national_format: Optional[str] = payload.get("national_format")
        self.valid: Optional[bool] = payload.get("valid")
        self.validation_errors: Optional[
            List["PhoneNumberInstance.ValidationError"]
        ] = payload.get("validation_errors")
        self.caller_name: Optional[Dict[str, object]] = payload.get("caller_name")
        self.sim_swap: Optional[Dict[str, object]] = payload.get("sim_swap")
        self.call_forwarding: Optional[Dict[str, object]] = payload.get(
            "call_forwarding"
        )
        self.live_activity: Optional[Dict[str, object]] = payload.get("live_activity")
        self.line_type_intelligence: Optional[Dict[str, object]] = payload.get(
            "line_type_intelligence"
        )
        self.identity_match: Optional[Dict[str, object]] = payload.get("identity_match")
        self.sms_pumping_risk: Optional[Dict[str, object]] = payload.get(
            "sms_pumping_risk"
        )
        self.disposable_phone_number_risk: Optional[Dict[str, object]] = payload.get(
            "disposable_phone_number_risk"
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "phone_number": phone_number or self.phone_number,
        }
        self._context: Optional[PhoneNumberContext] = None

    @property
    def _proxy(self) -> "PhoneNumberContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: PhoneNumberContext for this PhoneNumberInstance
        """
        if self._context is None:
            self._context = PhoneNumberContext(
                self._version,
                phone_number=self._solution["phone_number"],
            )
        return self._context

    def fetch(
        self,
        fields: Union[str, object] = values.unset,
        country_code: Union[str, object] = values.unset,
        first_name: Union[str, object] = values.unset,
        last_name: Union[str, object] = values.unset,
        address_line1: Union[str, object] = values.unset,
        address_line2: Union[str, object] = values.unset,
        city: Union[str, object] = values.unset,
        state: Union[str, object] = values.unset,
        postal_code: Union[str, object] = values.unset,
        address_country_code: Union[str, object] = values.unset,
        national_id: Union[str, object] = values.unset,
        date_of_birth: Union[str, object] = values.unset,
    ) -> "PhoneNumberInstance":
        """
        Fetch the PhoneNumberInstance

        :param fields: A comma-separated list of fields to return. Possible values are caller_name, sim_swap, call_forwarding, live_activity, line_type_intelligence, identity_match.
        :param country_code: The [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) used if the phone number provided is in national format.
        :param first_name: User’s first name. This query parameter is only used (optionally) for identity_match package requests.
        :param last_name: User’s last name. This query parameter is only used (optionally) for identity_match package requests.
        :param address_line1: User’s first address line. This query parameter is only used (optionally) for identity_match package requests.
        :param address_line2: User’s second address line. This query parameter is only used (optionally) for identity_match package requests.
        :param city: User’s city. This query parameter is only used (optionally) for identity_match package requests.
        :param state: User’s country subdivision, such as state, province, or locality. This query parameter is only used (optionally) for identity_match package requests.
        :param postal_code: User’s postal zip code. This query parameter is only used (optionally) for identity_match package requests.
        :param address_country_code: User’s country, up to two characters. This query parameter is only used (optionally) for identity_match package requests.
        :param national_id: User’s national ID, such as SSN or Passport ID. This query parameter is only used (optionally) for identity_match package requests.
        :param date_of_birth: User’s date of birth, in YYYYMMDD format. This query parameter is only used (optionally) for identity_match package requests.

        :returns: The fetched PhoneNumberInstance
        """
        return self._proxy.fetch(
            fields=fields,
            country_code=country_code,
            first_name=first_name,
            last_name=last_name,
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            state=state,
            postal_code=postal_code,
            address_country_code=address_country_code,
            national_id=national_id,
            date_of_birth=date_of_birth,
        )

    async def fetch_async(
        self,
        fields: Union[str, object] = values.unset,
        country_code: Union[str, object] = values.unset,
        first_name: Union[str, object] = values.unset,
        last_name: Union[str, object] = values.unset,
        address_line1: Union[str, object] = values.unset,
        address_line2: Union[str, object] = values.unset,
        city: Union[str, object] = values.unset,
        state: Union[str, object] = values.unset,
        postal_code: Union[str, object] = values.unset,
        address_country_code: Union[str, object] = values.unset,
        national_id: Union[str, object] = values.unset,
        date_of_birth: Union[str, object] = values.unset,
    ) -> "PhoneNumberInstance":
        """
        Asynchronous coroutine to fetch the PhoneNumberInstance

        :param fields: A comma-separated list of fields to return. Possible values are caller_name, sim_swap, call_forwarding, live_activity, line_type_intelligence, identity_match.
        :param country_code: The [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) used if the phone number provided is in national format.
        :param first_name: User’s first name. This query parameter is only used (optionally) for identity_match package requests.
        :param last_name: User’s last name. This query parameter is only used (optionally) for identity_match package requests.
        :param address_line1: User’s first address line. This query parameter is only used (optionally) for identity_match package requests.
        :param address_line2: User’s second address line. This query parameter is only used (optionally) for identity_match package requests.
        :param city: User’s city. This query parameter is only used (optionally) for identity_match package requests.
        :param state: User’s country subdivision, such as state, province, or locality. This query parameter is only used (optionally) for identity_match package requests.
        :param postal_code: User’s postal zip code. This query parameter is only used (optionally) for identity_match package requests.
        :param address_country_code: User’s country, up to two characters. This query parameter is only used (optionally) for identity_match package requests.
        :param national_id: User’s national ID, such as SSN or Passport ID. This query parameter is only used (optionally) for identity_match package requests.
        :param date_of_birth: User’s date of birth, in YYYYMMDD format. This query parameter is only used (optionally) for identity_match package requests.

        :returns: The fetched PhoneNumberInstance
        """
        return await self._proxy.fetch_async(
            fields=fields,
            country_code=country_code,
            first_name=first_name,
            last_name=last_name,
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            state=state,
            postal_code=postal_code,
            address_country_code=address_country_code,
            national_id=national_id,
            date_of_birth=date_of_birth,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Lookups.V2.PhoneNumberInstance {}>".format(context)


class PhoneNumberContext(InstanceContext):
    def __init__(self, version: Version, phone_number: str):
        """
        Initialize the PhoneNumberContext

        :param version: Version that contains the resource
        :param phone_number: The phone number to lookup in E.164 or national format. Default country code is +1 (North America).
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "phone_number": phone_number,
        }
        self._uri = "/PhoneNumbers/{phone_number}".format(**self._solution)

    def fetch(
        self,
        fields: Union[str, object] = values.unset,
        country_code: Union[str, object] = values.unset,
        first_name: Union[str, object] = values.unset,
        last_name: Union[str, object] = values.unset,
        address_line1: Union[str, object] = values.unset,
        address_line2: Union[str, object] = values.unset,
        city: Union[str, object] = values.unset,
        state: Union[str, object] = values.unset,
        postal_code: Union[str, object] = values.unset,
        address_country_code: Union[str, object] = values.unset,
        national_id: Union[str, object] = values.unset,
        date_of_birth: Union[str, object] = values.unset,
    ) -> PhoneNumberInstance:
        """
        Fetch the PhoneNumberInstance

        :param fields: A comma-separated list of fields to return. Possible values are caller_name, sim_swap, call_forwarding, live_activity, line_type_intelligence, identity_match.
        :param country_code: The [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) used if the phone number provided is in national format.
        :param first_name: User’s first name. This query parameter is only used (optionally) for identity_match package requests.
        :param last_name: User’s last name. This query parameter is only used (optionally) for identity_match package requests.
        :param address_line1: User’s first address line. This query parameter is only used (optionally) for identity_match package requests.
        :param address_line2: User’s second address line. This query parameter is only used (optionally) for identity_match package requests.
        :param city: User’s city. This query parameter is only used (optionally) for identity_match package requests.
        :param state: User’s country subdivision, such as state, province, or locality. This query parameter is only used (optionally) for identity_match package requests.
        :param postal_code: User’s postal zip code. This query parameter is only used (optionally) for identity_match package requests.
        :param address_country_code: User’s country, up to two characters. This query parameter is only used (optionally) for identity_match package requests.
        :param national_id: User’s national ID, such as SSN or Passport ID. This query parameter is only used (optionally) for identity_match package requests.
        :param date_of_birth: User’s date of birth, in YYYYMMDD format. This query parameter is only used (optionally) for identity_match package requests.

        :returns: The fetched PhoneNumberInstance
        """

        data = values.of(
            {
                "Fields": fields,
                "CountryCode": country_code,
                "FirstName": first_name,
                "LastName": last_name,
                "AddressLine1": address_line1,
                "AddressLine2": address_line2,
                "City": city,
                "State": state,
                "PostalCode": postal_code,
                "AddressCountryCode": address_country_code,
                "NationalId": national_id,
                "DateOfBirth": date_of_birth,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return PhoneNumberInstance(
            self._version,
            payload,
            phone_number=self._solution["phone_number"],
        )

    async def fetch_async(
        self,
        fields: Union[str, object] = values.unset,
        country_code: Union[str, object] = values.unset,
        first_name: Union[str, object] = values.unset,
        last_name: Union[str, object] = values.unset,
        address_line1: Union[str, object] = values.unset,
        address_line2: Union[str, object] = values.unset,
        city: Union[str, object] = values.unset,
        state: Union[str, object] = values.unset,
        postal_code: Union[str, object] = values.unset,
        address_country_code: Union[str, object] = values.unset,
        national_id: Union[str, object] = values.unset,
        date_of_birth: Union[str, object] = values.unset,
    ) -> PhoneNumberInstance:
        """
        Asynchronous coroutine to fetch the PhoneNumberInstance

        :param fields: A comma-separated list of fields to return. Possible values are caller_name, sim_swap, call_forwarding, live_activity, line_type_intelligence, identity_match.
        :param country_code: The [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) used if the phone number provided is in national format.
        :param first_name: User’s first name. This query parameter is only used (optionally) for identity_match package requests.
        :param last_name: User’s last name. This query parameter is only used (optionally) for identity_match package requests.
        :param address_line1: User’s first address line. This query parameter is only used (optionally) for identity_match package requests.
        :param address_line2: User’s second address line. This query parameter is only used (optionally) for identity_match package requests.
        :param city: User’s city. This query parameter is only used (optionally) for identity_match package requests.
        :param state: User’s country subdivision, such as state, province, or locality. This query parameter is only used (optionally) for identity_match package requests.
        :param postal_code: User’s postal zip code. This query parameter is only used (optionally) for identity_match package requests.
        :param address_country_code: User’s country, up to two characters. This query parameter is only used (optionally) for identity_match package requests.
        :param national_id: User’s national ID, such as SSN or Passport ID. This query parameter is only used (optionally) for identity_match package requests.
        :param date_of_birth: User’s date of birth, in YYYYMMDD format. This query parameter is only used (optionally) for identity_match package requests.

        :returns: The fetched PhoneNumberInstance
        """

        data = values.of(
            {
                "Fields": fields,
                "CountryCode": country_code,
                "FirstName": first_name,
                "LastName": last_name,
                "AddressLine1": address_line1,
                "AddressLine2": address_line2,
                "City": city,
                "State": state,
                "PostalCode": postal_code,
                "AddressCountryCode": address_country_code,
                "NationalId": national_id,
                "DateOfBirth": date_of_birth,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return PhoneNumberInstance(
            self._version,
            payload,
            phone_number=self._solution["phone_number"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Lookups.V2.PhoneNumberContext {}>".format(context)


class PhoneNumberList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the PhoneNumberList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self, phone_number: str) -> PhoneNumberContext:
        """
        Constructs a PhoneNumberContext

        :param phone_number: The phone number to lookup in E.164 or national format. Default country code is +1 (North America).
        """
        return PhoneNumberContext(self._version, phone_number=phone_number)

    def __call__(self, phone_number: str) -> PhoneNumberContext:
        """
        Constructs a PhoneNumberContext

        :param phone_number: The phone number to lookup in E.164 or national format. Default country code is +1 (North America).
        """
        return PhoneNumberContext(self._version, phone_number=phone_number)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Lookups.V2.PhoneNumberList>"
