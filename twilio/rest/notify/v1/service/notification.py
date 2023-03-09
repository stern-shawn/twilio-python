r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Notify
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



class NotificationList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the NotificationList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to create the resource under.
        
        :returns: twilio.rest.notify.v1.service.notification.NotificationList
        :rtype: twilio.rest.notify.v1.service.notification.NotificationList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/{service_sid}/Notifications'.format(**self._solution)
        
        
    
    def create(self, body=values.unset, priority=values.unset, ttl=values.unset, title=values.unset, sound=values.unset, action=values.unset, data=values.unset, apn=values.unset, gcm=values.unset, sms=values.unset, facebook_messenger=values.unset, fcm=values.unset, segment=values.unset, alexa=values.unset, to_binding=values.unset, delivery_callback_url=values.unset, identity=values.unset, tag=values.unset):
        """
        Create the NotificationInstance

        :param str body: The notification text. For FCM and GCM, translates to `data.twi_body`. For APNS, translates to `aps.alert.body`. For SMS, translates to `body`. SMS requires either this `body` value, or `media_urls` attribute defined in the `sms` parameter of the notification.
        :param NotificationInstance.Priority priority: 
        :param int ttl: How long, in seconds, the notification is valid. Can be an integer between 0 and 2,419,200, which is 4 weeks, the default and the maximum supported time to live (TTL). Delivery should be attempted if the device is offline until the TTL elapses. Zero means that the notification delivery is attempted immediately, only once, and is not stored for future delivery. SMS does not support this property.
        :param str title: The notification title. For FCM and GCM, this translates to the `data.twi_title` value. For APNS, this translates to the `aps.alert.title` value. SMS does not support this property. This field is not visible on iOS phones and tablets but appears on Apple Watch and Android devices.
        :param str sound: The name of the sound to be played for the notification. For FCM and GCM, this Translates to `data.twi_sound`.  For APNS, this translates to `aps.sound`.  SMS does not support this property.
        :param str action: The actions to display for the notification. For APNS, translates to the `aps.category` value. For GCM, translates to the `data.twi_action` value. For SMS, this parameter is not supported and is omitted from deliveries to those channels.
        :param object data: The custom key-value pairs of the notification's payload. For FCM and GCM, this value translates to `data` in the FCM and GCM payloads. FCM and GCM [reserve certain keys](https://firebase.google.com/docs/cloud-messaging/http-server-ref) that cannot be used in those channels. For APNS, attributes of `data` are inserted into the APNS payload as custom properties outside of the `aps` dictionary. In all channels, we reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed and are rejected as 400 Bad request with no delivery attempted. For SMS, this parameter is not supported and is omitted from deliveries to those channels.
        :param object apn: The APNS-specific payload that overrides corresponding attributes in the generic payload for APNS Bindings. This property maps to the APNS `Payload` item, therefore the `aps` key must be used to change standard attributes. Adds custom key-value pairs to the root of the dictionary. See the [APNS documentation](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html) for more details. We reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed.
        :param object gcm: The GCM-specific payload that overrides corresponding attributes in the generic payload for GCM Bindings.  This property maps to the root JSON dictionary. See the [GCM documentation](https://firebase.google.com/docs/cloud-messaging/http-server-ref) for more details. Target parameters `to`, `registration_ids`, and `notification_key` are not allowed. We reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed. GCM also [reserves certain keys](https://firebase.google.com/docs/cloud-messaging/http-server-ref).
        :param object sms: The SMS-specific payload that overrides corresponding attributes in the generic payload for SMS Bindings.  Each attribute in this value maps to the corresponding `form` parameter of the Twilio [Message](https://www.twilio.com/docs/sms/send-messages) resource.  These parameters of the Message resource are supported in snake case format: `body`, `media_urls`, `status_callback`, and `max_price`.  The `status_callback` parameter overrides the corresponding parameter in the messaging service, if configured. The `media_urls` property expects a JSON array.
        :param object facebook_messenger: Deprecated.
        :param object fcm: The FCM-specific payload that overrides corresponding attributes in the generic payload for FCM Bindings. This property maps to the root JSON dictionary. See the [FCM documentation](https://firebase.google.com/docs/cloud-messaging/http-server-ref#downstream) for more details. Target parameters `to`, `registration_ids`, `condition`, and `notification_key` are not allowed in this parameter. We reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed. FCM also [reserves certain keys](https://firebase.google.com/docs/cloud-messaging/http-server-ref), which cannot be used in that channel.
        :param list[str] segment: The Segment resource is deprecated. Use the `tag` parameter, instead.
        :param object alexa: Deprecated.
        :param list[str] to_binding: The destination address specified as a JSON string.  Multiple `to_binding` parameters can be included but the total size of the request entity should not exceed 1MB. This is typically sufficient for 10,000 phone numbers.
        :param str delivery_callback_url: URL to send webhooks.
        :param list[str] identity: The `identity` value that uniquely identifies the new resource's [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/notify/api/service-resource). Delivery will be attempted only to Bindings with an Identity in this list. No more than 20 items are allowed in this list.
        :param list[str] tag: A tag that selects the Bindings to notify. Repeat this parameter to specify more than one tag, up to a total of 5 tags. The implicit tag `all` is available to notify all Bindings in a Service instance. Similarly, the implicit tags `apn`, `fcm`, `gcm`, `sms` and `facebook-messenger` are available to notify all Bindings in a specific channel.
        
        :returns: The created NotificationInstance
        :rtype: twilio.rest.notify.v1.service.notification.NotificationInstance
        """
        data = values.of({ 
            'Body': body,
            'Priority': priority,
            'Ttl': ttl,
            'Title': title,
            'Sound': sound,
            'Action': action,
            'Data': serialize.object(data),
            'Apn': serialize.object(apn),
            'Gcm': serialize.object(gcm),
            'Sms': serialize.object(sms),
            'FacebookMessenger': serialize.object(facebook_messenger),
            'Fcm': serialize.object(fcm),
            'Segment': serialize.map(segment, lambda e: e),
            'Alexa': serialize.object(alexa),
            'ToBinding': serialize.map(to_binding, lambda e: e),
            'DeliveryCallbackUrl': delivery_callback_url,
            'Identity': serialize.map(identity, lambda e: e),
            'Tag': serialize.map(tag, lambda e: e),
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return NotificationInstance(self._version, payload, service_sid=self._solution['service_sid'])

    async def create_async(self, body=values.unset, priority=values.unset, ttl=values.unset, title=values.unset, sound=values.unset, action=values.unset, data=values.unset, apn=values.unset, gcm=values.unset, sms=values.unset, facebook_messenger=values.unset, fcm=values.unset, segment=values.unset, alexa=values.unset, to_binding=values.unset, delivery_callback_url=values.unset, identity=values.unset, tag=values.unset):
        """
        Asynchronous coroutine to create the NotificationInstance

        :param str body: The notification text. For FCM and GCM, translates to `data.twi_body`. For APNS, translates to `aps.alert.body`. For SMS, translates to `body`. SMS requires either this `body` value, or `media_urls` attribute defined in the `sms` parameter of the notification.
        :param NotificationInstance.Priority priority: 
        :param int ttl: How long, in seconds, the notification is valid. Can be an integer between 0 and 2,419,200, which is 4 weeks, the default and the maximum supported time to live (TTL). Delivery should be attempted if the device is offline until the TTL elapses. Zero means that the notification delivery is attempted immediately, only once, and is not stored for future delivery. SMS does not support this property.
        :param str title: The notification title. For FCM and GCM, this translates to the `data.twi_title` value. For APNS, this translates to the `aps.alert.title` value. SMS does not support this property. This field is not visible on iOS phones and tablets but appears on Apple Watch and Android devices.
        :param str sound: The name of the sound to be played for the notification. For FCM and GCM, this Translates to `data.twi_sound`.  For APNS, this translates to `aps.sound`.  SMS does not support this property.
        :param str action: The actions to display for the notification. For APNS, translates to the `aps.category` value. For GCM, translates to the `data.twi_action` value. For SMS, this parameter is not supported and is omitted from deliveries to those channels.
        :param object data: The custom key-value pairs of the notification's payload. For FCM and GCM, this value translates to `data` in the FCM and GCM payloads. FCM and GCM [reserve certain keys](https://firebase.google.com/docs/cloud-messaging/http-server-ref) that cannot be used in those channels. For APNS, attributes of `data` are inserted into the APNS payload as custom properties outside of the `aps` dictionary. In all channels, we reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed and are rejected as 400 Bad request with no delivery attempted. For SMS, this parameter is not supported and is omitted from deliveries to those channels.
        :param object apn: The APNS-specific payload that overrides corresponding attributes in the generic payload for APNS Bindings. This property maps to the APNS `Payload` item, therefore the `aps` key must be used to change standard attributes. Adds custom key-value pairs to the root of the dictionary. See the [APNS documentation](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html) for more details. We reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed.
        :param object gcm: The GCM-specific payload that overrides corresponding attributes in the generic payload for GCM Bindings.  This property maps to the root JSON dictionary. See the [GCM documentation](https://firebase.google.com/docs/cloud-messaging/http-server-ref) for more details. Target parameters `to`, `registration_ids`, and `notification_key` are not allowed. We reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed. GCM also [reserves certain keys](https://firebase.google.com/docs/cloud-messaging/http-server-ref).
        :param object sms: The SMS-specific payload that overrides corresponding attributes in the generic payload for SMS Bindings.  Each attribute in this value maps to the corresponding `form` parameter of the Twilio [Message](https://www.twilio.com/docs/sms/send-messages) resource.  These parameters of the Message resource are supported in snake case format: `body`, `media_urls`, `status_callback`, and `max_price`.  The `status_callback` parameter overrides the corresponding parameter in the messaging service, if configured. The `media_urls` property expects a JSON array.
        :param object facebook_messenger: Deprecated.
        :param object fcm: The FCM-specific payload that overrides corresponding attributes in the generic payload for FCM Bindings. This property maps to the root JSON dictionary. See the [FCM documentation](https://firebase.google.com/docs/cloud-messaging/http-server-ref#downstream) for more details. Target parameters `to`, `registration_ids`, `condition`, and `notification_key` are not allowed in this parameter. We reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed. FCM also [reserves certain keys](https://firebase.google.com/docs/cloud-messaging/http-server-ref), which cannot be used in that channel.
        :param list[str] segment: The Segment resource is deprecated. Use the `tag` parameter, instead.
        :param object alexa: Deprecated.
        :param list[str] to_binding: The destination address specified as a JSON string.  Multiple `to_binding` parameters can be included but the total size of the request entity should not exceed 1MB. This is typically sufficient for 10,000 phone numbers.
        :param str delivery_callback_url: URL to send webhooks.
        :param list[str] identity: The `identity` value that uniquely identifies the new resource's [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/notify/api/service-resource). Delivery will be attempted only to Bindings with an Identity in this list. No more than 20 items are allowed in this list.
        :param list[str] tag: A tag that selects the Bindings to notify. Repeat this parameter to specify more than one tag, up to a total of 5 tags. The implicit tag `all` is available to notify all Bindings in a Service instance. Similarly, the implicit tags `apn`, `fcm`, `gcm`, `sms` and `facebook-messenger` are available to notify all Bindings in a specific channel.
        
        :returns: The created NotificationInstance
        :rtype: twilio.rest.notify.v1.service.notification.NotificationInstance
        """
        data = values.of({ 
            'Body': body,
            'Priority': priority,
            'Ttl': ttl,
            'Title': title,
            'Sound': sound,
            'Action': action,
            'Data': serialize.object(data),
            'Apn': serialize.object(apn),
            'Gcm': serialize.object(gcm),
            'Sms': serialize.object(sms),
            'FacebookMessenger': serialize.object(facebook_messenger),
            'Fcm': serialize.object(fcm),
            'Segment': serialize.map(segment, lambda e: e),
            'Alexa': serialize.object(alexa),
            'ToBinding': serialize.map(to_binding, lambda e: e),
            'DeliveryCallbackUrl': delivery_callback_url,
            'Identity': serialize.map(identity, lambda e: e),
            'Tag': serialize.map(tag, lambda e: e),
        })
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data,)

        return NotificationInstance(self._version, payload, service_sid=self._solution['service_sid'])
    


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notify.V1.NotificationList>'


class NotificationInstance(InstanceResource):

    class Priority(object):
        HIGH = "high"
        LOW = "low"

    def __init__(self, version, payload, service_sid: str):
        """
        Initialize the NotificationInstance
        :returns: twilio.rest.notify.v1.service.notification.NotificationInstance
        :rtype: twilio.rest.notify.v1.service.notification.NotificationInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'identities': payload.get('identities'),
            'tags': payload.get('tags'),
            'segments': payload.get('segments'),
            'priority': payload.get('priority'),
            'ttl': deserialize.integer(payload.get('ttl')),
            'title': payload.get('title'),
            'body': payload.get('body'),
            'sound': payload.get('sound'),
            'action': payload.get('action'),
            'data': payload.get('data'),
            'apn': payload.get('apn'),
            'gcm': payload.get('gcm'),
            'fcm': payload.get('fcm'),
            'sms': payload.get('sms'),
            'facebook_messenger': payload.get('facebook_messenger'),
            'alexa': payload.get('alexa'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid,  }
    
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Notification resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Notification resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) the resource is associated with.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def identities(self):
        """
        :returns: The list of `identity` values of the Users to notify. We will attempt to deliver notifications only to Bindings with an identity in this list.
        :rtype: list[str]
        """
        return self._properties['identities']
    
    @property
    def tags(self):
        """
        :returns: The tags that select the Bindings to notify. Notifications will be attempted only to Bindings that have all of the tags listed in this property.
        :rtype: list[str]
        """
        return self._properties['tags']
    
    @property
    def segments(self):
        """
        :returns: The list of Segments to notify. The [Segment](https://www.twilio.com/docs/notify/api/segment-resource) resource is deprecated. Use the `tags` property, instead.
        :rtype: list[str]
        """
        return self._properties['segments']
    
    @property
    def priority(self):
        """
        :returns: 
        :rtype: NotificationInstance.Priority
        """
        return self._properties['priority']
    
    @property
    def ttl(self):
        """
        :returns: How long, in seconds, the notification is valid. Can be an integer between 0 and 2,419,200, which is 4 weeks, the default and the maximum supported time to live (TTL). Delivery should be attempted if the device is offline until the TTL elapses. Zero means that the notification delivery is attempted immediately, only once, and is not stored for future delivery. SMS does not support this property.
        :rtype: int
        """
        return self._properties['ttl']
    
    @property
    def title(self):
        """
        :returns: The notification title. For FCM and GCM, this translates to the `data.twi_title` value. For APNS, this translates to the `aps.alert.title` value. SMS does not support this property. This field is not visible on iOS phones and tablets but appears on Apple Watch and Android devices.
        :rtype: str
        """
        return self._properties['title']
    
    @property
    def body(self):
        """
        :returns: The notification text. For FCM and GCM, translates to `data.twi_body`. For APNS, translates to `aps.alert.body`. For SMS, translates to `body`. SMS requires either this `body` value, or `media_urls` attribute defined in the `sms` parameter of the notification.
        :rtype: str
        """
        return self._properties['body']
    
    @property
    def sound(self):
        """
        :returns: The name of the sound to be played for the notification. For FCM and GCM, this Translates to `data.twi_sound`.  For APNS, this translates to `aps.sound`.  SMS does not support this property.
        :rtype: str
        """
        return self._properties['sound']
    
    @property
    def action(self):
        """
        :returns: The actions to display for the notification. For APNS, translates to the `aps.category` value. For GCM, translates to the `data.twi_action` value. For SMS, this parameter is not supported and is omitted from deliveries to those channels.
        :rtype: str
        """
        return self._properties['action']
    
    @property
    def data(self):
        """
        :returns: The custom key-value pairs of the notification's payload. For FCM and GCM, this value translates to `data` in the FCM and GCM payloads. FCM and GCM [reserve certain keys](https://firebase.google.com/docs/cloud-messaging/http-server-ref) that cannot be used in those channels. For APNS, attributes of `data` are inserted into the APNS payload as custom properties outside of the `aps` dictionary. In all channels, we reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed and are rejected as 400 Bad request with no delivery attempted. For SMS, this parameter is not supported and is omitted from deliveries to those channels.
        :rtype: dict
        """
        return self._properties['data']
    
    @property
    def apn(self):
        """
        :returns: The APNS-specific payload that overrides corresponding attributes in the generic payload for APNS Bindings. This property maps to the APNS `Payload` item, therefore the `aps` key must be used to change standard attributes. Adds custom key-value pairs to the root of the dictionary. See the [APNS documentation](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html) for more details. We reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed.
        :rtype: dict
        """
        return self._properties['apn']
    
    @property
    def gcm(self):
        """
        :returns: The GCM-specific payload that overrides corresponding attributes in the generic payload for GCM Bindings.  This property maps to the root JSON dictionary. Target parameters `to`, `registration_ids`, and `notification_key` are not allowed. We reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed.
        :rtype: dict
        """
        return self._properties['gcm']
    
    @property
    def fcm(self):
        """
        :returns: The FCM-specific payload that overrides corresponding attributes in the generic payload for FCM Bindings. This property maps to the root JSON dictionary. See the [FCM documentation](https://firebase.google.com/docs/cloud-messaging/http-server-ref#downstream) for more details. Target parameters `to`, `registration_ids`, `condition`, and `notification_key` are not allowed in this parameter. We reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed. FCM also [reserves certain keys](https://firebase.google.com/docs/cloud-messaging/http-server-ref), which cannot be used in that channel.
        :rtype: dict
        """
        return self._properties['fcm']
    
    @property
    def sms(self):
        """
        :returns: The SMS-specific payload that overrides corresponding attributes in the generic payload for SMS Bindings.  Each attribute in this value maps to the corresponding `form` parameter of the Twilio [Message](https://www.twilio.com/docs/sms/api/message-resource) resource.  These parameters of the Message resource are supported in snake case format: `body`, `media_urls`, `status_callback`, and `max_price`.  The `status_callback` parameter overrides the corresponding parameter in the messaging service, if configured. The `media_urls` property expects a JSON array.
        :rtype: dict
        """
        return self._properties['sms']
    
    @property
    def facebook_messenger(self):
        """
        :returns: Deprecated.
        :rtype: dict
        """
        return self._properties['facebook_messenger']
    
    @property
    def alexa(self):
        """
        :returns: Deprecated.
        :rtype: dict
        """
        return self._properties['alexa']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Notify.V1.NotificationInstance {}>'.format(context)


