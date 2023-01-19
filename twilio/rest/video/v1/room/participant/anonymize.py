"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Video
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


class AnonymizeContext(InstanceContext):
    def __init__(self, version: Version, room_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'room_sid': room_sid, 'sid': sid,  }
        self._uri = '/Rooms/${room_sid}/Participants/${sid}/Anonymize'
        
    
    def update(self):
        data = values.of({
            
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return AnonymizeInstance(self._version, payload, room_sid=self._solution['room_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.AnonymizeContext>'



class AnonymizeInstance(InstanceResource):
    def __init__(self, version, payload, room_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'room_sid' : payload.get('room_sid'),
            'account_sid' : payload.get('account_sid'),
            'status' : payload.get('status'),
            'identity' : payload.get('identity'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'start_time' : payload.get('start_time'),
            'end_time' : payload.get('end_time'),
            'duration' : payload.get('duration'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'room_sid': room_sid or self._properties['room_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = AnonymizeContext(
                self._version,
                room_sid=self._solution['room_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.AnonymizeInstance {}>'.format(context)



class AnonymizeListInstance(ListResource):
    def __init__(self, version: Version, room_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'room_sid': room_sid, 'sid': sid,  }
        self._uri = ''
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.AnonymizeListInstance>'

