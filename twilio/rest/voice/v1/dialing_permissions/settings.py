r"""
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



class SettingsList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the SettingsList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.voice.v1.dialing_permissions.settings.SettingsList
        :rtype: twilio.rest.voice.v1.dialing_permissions.settings.SettingsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    
    

    def get(self):
        """
        Constructs a SettingsContext
        
        :returns: twilio.rest.voice.v1.dialing_permissions.settings.SettingsContext
        :rtype: twilio.rest.voice.v1.dialing_permissions.settings.SettingsContext
        """
        return SettingsContext(self._version)

    def __call__(self):
        """
        Constructs a SettingsContext
        
        :returns: twilio.rest.voice.v1.dialing_permissions.settings.SettingsContext
        :rtype: twilio.rest.voice.v1.dialing_permissions.settings.SettingsContext
        """
        return SettingsContext(self._version)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Voice.V1.SettingsList>'

class SettingsContext(InstanceContext):

    def __init__(self, version: Version):
        """
        Initialize the SettingsContext

        :param Version version: Version that contains the resource
        

        :returns: twilio.rest.voice.v1.dialing_permissions.settings.SettingsContext
        :rtype: twilio.rest.voice.v1.dialing_permissions.settings.SettingsContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
        }
        self._uri = '/Settings'.format(**self._solution)
        
    
    
    def fetch(self):
        """
        Fetch the SettingsInstance
        

        :returns: The fetched SettingsInstance
        :rtype: twilio.rest.voice.v1.dialing_permissions.settings.SettingsInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SettingsInstance(
            self._version,
            payload,
            
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the SettingsInstance
        

        :returns: The fetched SettingsInstance
        :rtype: twilio.rest.voice.v1.dialing_permissions.settings.SettingsInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return SettingsInstance(
            self._version,
            payload,
            
        )
    
    
    def update(self, dialing_permissions_inheritance=values.unset):
        """
        Update the SettingsInstance
        
        :params bool dialing_permissions_inheritance: `true` for the sub-account to inherit voice dialing permissions from the Master Project; otherwise `false`.

        :returns: The updated SettingsInstance
        :rtype: twilio.rest.voice.v1.dialing_permissions.settings.SettingsInstance
        """
        data = values.of({ 
            'DialingPermissionsInheritance': dialing_permissions_inheritance,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return SettingsInstance(
            self._version,
            payload
        )

    async def update_async(self, dialing_permissions_inheritance=values.unset):
        """
        Asynchronous coroutine to update the SettingsInstance
        
        :params bool dialing_permissions_inheritance: `true` for the sub-account to inherit voice dialing permissions from the Master Project; otherwise `false`.

        :returns: The updated SettingsInstance
        :rtype: twilio.rest.voice.v1.dialing_permissions.settings.SettingsInstance
        """
        data = values.of({ 
            'DialingPermissionsInheritance': dialing_permissions_inheritance,
        })
        

        payload = await self._version.update_async(method='POST', uri=self._uri, data=data,)

        return SettingsInstance(
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
        return '<Twilio.Voice.V1.SettingsContext {}>'.format(context)

class SettingsInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the SettingsInstance
        :returns: twilio.rest.voice.v1.dialing_permissions.settings.SettingsInstance
        :rtype: twilio.rest.voice.v1.dialing_permissions.settings.SettingsInstance
        """
        super().__init__(version)

        self._properties = { 
            'dialing_permissions_inheritance': payload.get('dialing_permissions_inheritance'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = {  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SettingsContext for this SettingsInstance
        :rtype: twilio.rest.voice.v1.dialing_permissions.settings.SettingsContext
        """
        if self._context is None:
            self._context = SettingsContext(self._version,)
        return self._context
    
    @property
    def dialing_permissions_inheritance(self):
        """
        :returns: `true` if the sub-account will inherit voice dialing permissions from the Master Project; otherwise `false`.
        :rtype: bool
        """
        return self._properties['dialing_permissions_inheritance']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of this resource.
        :rtype: str
        """
        return self._properties['url']
    
    
    def fetch(self):
        """
        Fetch the SettingsInstance
        

        :returns: The fetched SettingsInstance
        :rtype: twilio.rest.voice.v1.dialing_permissions.settings.SettingsInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the SettingsInstance
        

        :returns: The fetched SettingsInstance
        :rtype: twilio.rest.voice.v1.dialing_permissions.settings.SettingsInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, dialing_permissions_inheritance=values.unset):
        """
        Update the SettingsInstance
        
        :params bool dialing_permissions_inheritance: `true` for the sub-account to inherit voice dialing permissions from the Master Project; otherwise `false`.

        :returns: The updated SettingsInstance
        :rtype: twilio.rest.voice.v1.dialing_permissions.settings.SettingsInstance
        """
        return self._proxy.update(dialing_permissions_inheritance=dialing_permissions_inheritance, )

    async def update_async(self, dialing_permissions_inheritance=values.unset):
        """
        Asynchronous coroutine to update the SettingsInstance
        
        :params bool dialing_permissions_inheritance: `true` for the sub-account to inherit voice dialing permissions from the Master Project; otherwise `false`.

        :returns: The updated SettingsInstance
        :rtype: twilio.rest.voice.v1.dialing_permissions.settings.SettingsInstance
        """
        return await self._proxy.update_async(dialing_permissions_inheritance=dialing_permissions_inheritance, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Voice.V1.SettingsInstance {}>'.format(context)


