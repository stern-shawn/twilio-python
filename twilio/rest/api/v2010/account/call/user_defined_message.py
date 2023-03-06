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

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class UserDefinedMessageList(ListResource):

    def __init__(self, version: Version, account_sid: str, call_sid: str):
        """
        Initialize the UserDefinedMessageList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created User Defined Message.
        :param call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Message is associated with.
        
        :returns: twilio.rest.api.v2010.account.call.user_defined_message.UserDefinedMessageList
        :rtype: twilio.rest.api.v2010.account.call.user_defined_message.UserDefinedMessageList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'call_sid': call_sid,  }
        self._uri = '/Accounts/{account_sid}/Calls/{call_sid}/UserDefinedMessages.json'.format(**self._solution)
        
        
    
    def create(self, content, idempotency_key=values.unset):
        """
        Create the UserDefinedMessageInstance

        :param str content: The User Defined Message in the form of URL-encoded JSON string.
        :param str idempotency_key: A unique string value to identify API call. This should be a unique string value per API call and can be a randomly generated.
        
        :returns: The created UserDefinedMessageInstance
        :rtype: twilio.rest.api.v2010.account.call.user_defined_message.UserDefinedMessageInstance
        """
        data = values.of({ 
            'Content': content,
            'IdempotencyKey': idempotency_key,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return UserDefinedMessageInstance(self._version, payload, account_sid=self._solution['account_sid'], call_sid=self._solution['call_sid'])
    


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.UserDefinedMessageList>'


class UserDefinedMessageInstance(InstanceResource):

    def __init__(self, version, payload, account_sid: str, call_sid: str):
        """
        Initialize the UserDefinedMessageInstance
        :returns: twilio.rest.api.v2010.account.call.user_defined_message.UserDefinedMessageInstance
        :rtype: twilio.rest.api.v2010.account.call.user_defined_message.UserDefinedMessageInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'call_sid': payload.get('call_sid'),
            'sid': payload.get('sid'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid, 'call_sid': call_sid,  }
    
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created User Defined Message.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def call_sid(self):
        """
        :returns: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Message is associated with.
        :rtype: str
        """
        return self._properties['call_sid']
    
    @property
    def sid(self):
        """
        :returns: The SID that uniquely identifies this User Defined Message.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def date_created(self):
        """
        :returns: The date that this User Defined Message was created, given in RFC 2822 format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.UserDefinedMessageInstance {}>'.format(context)


