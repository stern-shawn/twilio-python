r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Conversations
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



class WebhookList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the WebhookList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.conversations.v1.configuration.webhook.WebhookList
        :rtype: twilio.rest.conversations.v1.configuration.webhook.WebhookList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    
    

    def get(self):
        """
        Constructs a WebhookContext
        
        :returns: twilio.rest.conversations.v1.configuration.webhook.WebhookContext
        :rtype: twilio.rest.conversations.v1.configuration.webhook.WebhookContext
        """
        return WebhookContext(self._version)

    def __call__(self):
        """
        Constructs a WebhookContext
        
        :returns: twilio.rest.conversations.v1.configuration.webhook.WebhookContext
        :rtype: twilio.rest.conversations.v1.configuration.webhook.WebhookContext
        """
        return WebhookContext(self._version)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.WebhookList>'

class WebhookContext(InstanceContext):

    def __init__(self, version: Version):
        """
        Initialize the WebhookContext

        :param Version version: Version that contains the resource
        

        :returns: twilio.rest.conversations.v1.configuration.webhook.WebhookContext
        :rtype: twilio.rest.conversations.v1.configuration.webhook.WebhookContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
        }
        self._uri = '/Configuration/Webhooks'.format(**self._solution)
        
    
    
    def fetch(self):
        """
        Fetch the WebhookInstance
        

        :returns: The fetched WebhookInstance
        :rtype: twilio.rest.conversations.v1.configuration.webhook.WebhookInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return WebhookInstance(
            self._version,
            payload,
            
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the WebhookInstance
        

        :returns: The fetched WebhookInstance
        :rtype: twilio.rest.conversations.v1.configuration.webhook.WebhookInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return WebhookInstance(
            self._version,
            payload,
            
        )
    
    
    def update(self, method=values.unset, filters=values.unset, pre_webhook_url=values.unset, post_webhook_url=values.unset, target=values.unset):
        """
        Update the WebhookInstance
        
        :params str method: The HTTP method to be used when sending a webhook request.
        :params list[str] filters: The list of webhook event triggers that are enabled for this Service: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`
        :params str pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
        :params str post_webhook_url: The absolute url the post-event webhook request should be sent to.
        :params WebhookInstance.Target target: 

        :returns: The updated WebhookInstance
        :rtype: twilio.rest.conversations.v1.configuration.webhook.WebhookInstance
        """
        data = values.of({ 
            'Method': method,
            'Filters': serialize.map(filters, lambda e: e),
            'PreWebhookUrl': pre_webhook_url,
            'PostWebhookUrl': post_webhook_url,
            'Target': target,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return WebhookInstance(
            self._version,
            payload
        )

    async def update_async(self, method=values.unset, filters=values.unset, pre_webhook_url=values.unset, post_webhook_url=values.unset, target=values.unset):
        """
        Asynchronous coroutine to update the WebhookInstance
        
        :params str method: The HTTP method to be used when sending a webhook request.
        :params list[str] filters: The list of webhook event triggers that are enabled for this Service: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`
        :params str pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
        :params str post_webhook_url: The absolute url the post-event webhook request should be sent to.
        :params WebhookInstance.Target target: 

        :returns: The updated WebhookInstance
        :rtype: twilio.rest.conversations.v1.configuration.webhook.WebhookInstance
        """
        data = values.of({ 
            'Method': method,
            'Filters': serialize.map(filters, lambda e: e),
            'PreWebhookUrl': pre_webhook_url,
            'PostWebhookUrl': post_webhook_url,
            'Target': target,
        })
        

        payload = await self._version.update_async(method='POST', uri=self._uri, data=data,)

        return WebhookInstance(
            self._version,
            payload
        )
    
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.WebhookContext {}>'.format(context)

class WebhookInstance(InstanceResource):

    class Method(object):
        GET = "GET"
        POST = "POST"

    class Target(object):
        WEBHOOK = "webhook"
        FLEX = "flex"

    def __init__(self, version, payload):
        """
        Initialize the WebhookInstance
        :returns: twilio.rest.conversations.v1.configuration.webhook.WebhookInstance
        :rtype: twilio.rest.conversations.v1.configuration.webhook.WebhookInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'method': payload.get('method'),
            'filters': payload.get('filters'),
            'pre_webhook_url': payload.get('pre_webhook_url'),
            'post_webhook_url': payload.get('post_webhook_url'),
            'target': payload.get('target'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = {  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: WebhookContext for this WebhookInstance
        :rtype: twilio.rest.conversations.v1.configuration.webhook.WebhookContext
        """
        if self._context is None:
            self._context = WebhookContext(self._version,)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this conversation.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def method(self):
        """
        :returns: 
        :rtype: WebhookInstance.Method
        """
        return self._properties['method']
    
    @property
    def filters(self):
        """
        :returns: The list of webhook event triggers that are enabled for this Service: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`
        :rtype: list[str]
        """
        return self._properties['filters']
    
    @property
    def pre_webhook_url(self):
        """
        :returns: The absolute url the pre-event webhook request should be sent to.
        :rtype: str
        """
        return self._properties['pre_webhook_url']
    
    @property
    def post_webhook_url(self):
        """
        :returns: The absolute url the post-event webhook request should be sent to.
        :rtype: str
        """
        return self._properties['post_webhook_url']
    
    @property
    def target(self):
        """
        :returns: 
        :rtype: WebhookInstance.Target
        """
        return self._properties['target']
    
    @property
    def url(self):
        """
        :returns: An absolute API resource API resource URL for this webhook.
        :rtype: str
        """
        return self._properties['url']
    
    
    def fetch(self):
        """
        Fetch the WebhookInstance
        

        :returns: The fetched WebhookInstance
        :rtype: twilio.rest.conversations.v1.configuration.webhook.WebhookInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the WebhookInstance
        

        :returns: The fetched WebhookInstance
        :rtype: twilio.rest.conversations.v1.configuration.webhook.WebhookInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, method=values.unset, filters=values.unset, pre_webhook_url=values.unset, post_webhook_url=values.unset, target=values.unset):
        """
        Update the WebhookInstance
        
        :params str method: The HTTP method to be used when sending a webhook request.
        :params list[str] filters: The list of webhook event triggers that are enabled for this Service: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`
        :params str pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
        :params str post_webhook_url: The absolute url the post-event webhook request should be sent to.
        :params WebhookInstance.Target target: 

        :returns: The updated WebhookInstance
        :rtype: twilio.rest.conversations.v1.configuration.webhook.WebhookInstance
        """
        return self._proxy.update(method=method, filters=filters, pre_webhook_url=pre_webhook_url, post_webhook_url=post_webhook_url, target=target, )

    async def update_async(self, method=values.unset, filters=values.unset, pre_webhook_url=values.unset, post_webhook_url=values.unset, target=values.unset):
        """
        Asynchronous coroutine to update the WebhookInstance
        
        :params str method: The HTTP method to be used when sending a webhook request.
        :params list[str] filters: The list of webhook event triggers that are enabled for this Service: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`
        :params str pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
        :params str post_webhook_url: The absolute url the post-event webhook request should be sent to.
        :params WebhookInstance.Target target: 

        :returns: The updated WebhookInstance
        :rtype: twilio.rest.conversations.v1.configuration.webhook.WebhookInstance
        """
        return await self._proxy.update_async(method=method, filters=filters, pre_webhook_url=pre_webhook_url, post_webhook_url=post_webhook_url, target=target, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.WebhookInstance {}>'.format(context)


