"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Events
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


class SubscribedEventContext(InstanceContext):
    def __init__(self, version: Version, subscription_sid: str, type: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'subscription_sid': subscription_sid, 'type': type,  }
        self._uri = '/Subscriptions/${subscription_sid}/SubscribedEvents/${type}'
        
    
    def delete(self):
        
        

        """
        Deletes the SubscribedEventInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the SubscribedEventInstance

        :returns: The fetched SubscribedEventInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SubscribedEventInstance(self._version, payload, subscription_sid=self._solution['subscription_sid'], type=self._solution['type'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return SubscribedEventInstance(self._version, payload, subscription_sid=self._solution['subscription_sid'], type=self._solution['type'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.SubscribedEventContext>'



class SubscribedEventInstance(InstanceResource):
    def __init__(self, version, payload, subscription_sid: str, type: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'type' : payload.get('type'),
            'schema_version' : payload.get('schema_version'),
            'subscription_sid' : payload.get('subscription_sid'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'subscription_sid': subscription_sid or self._properties['subscription_sid'],'type': type or self._properties['type'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = SubscribedEventContext(
                self._version,
                subscription_sid=self._solution['subscription_sid'],type=self._solution['type'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.SubscribedEventInstance {}>'.format(context)



class SubscribedEventListInstance(ListResource):
    def __init__(self, version: Version, subscription_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'subscription_sid': subscription_sid,  }
        self._uri = '/Subscriptions/${subscription_sid}/SubscribedEvents'
        
    
    """
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return SubscribedEventInstance(self._version, payload, subscription_sid=self._solution['subscription_sid'])
        
    """
    
    """
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return SubscribedEventPage(self._version, payload, subscription_sid=self._solution['subscription_sid'], )
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.SubscribedEventListInstance>'

