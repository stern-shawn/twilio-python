"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Insights
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


class ConferenceParticipantContext(InstanceContext):
    def __init__(self, version: Version, conference_sid: str, participant_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'conference_sid': conference_sid, 'participant_sid': participant_sid,  }
        self._uri = '/Conferences/${conference_sid}/Participants/${participant_sid}'
        
    
    def fetch(self, events, metrics):
        
        """
        Fetch the ConferenceParticipantInstance

        :returns: The fetched ConferenceParticipantInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ConferenceParticipantInstance(self._version, payload, conference_sid=self._solution['conference_sid'], participant_sid=self._solution['participant_sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ConferenceParticipantContext>'



class ConferenceParticipantInstance(InstanceResource):
    def __init__(self, version, payload, conference_sid: str, participant_sid: str):
        super().__init__(version)
        self._properties = { 
            'participant_sid' : payload.get('participant_sid'),
            'label' : payload.get('label'),
            'conference_sid' : payload.get('conference_sid'),
            'call_sid' : payload.get('call_sid'),
            'account_sid' : payload.get('account_sid'),
            'call_direction' : payload.get('call_direction'),
            '_from' : payload.get('from'),
            'to' : payload.get('to'),
            'call_status' : payload.get('call_status'),
            'country_code' : payload.get('country_code'),
            'is_moderator' : payload.get('is_moderator'),
            'join_time' : payload.get('join_time'),
            'leave_time' : payload.get('leave_time'),
            'duration_seconds' : payload.get('duration_seconds'),
            'outbound_queue_length' : payload.get('outbound_queue_length'),
            'outbound_time_in_queue' : payload.get('outbound_time_in_queue'),
            'jitter_buffer_size' : payload.get('jitter_buffer_size'),
            'is_coach' : payload.get('is_coach'),
            'coached_participants' : payload.get('coached_participants'),
            'participant_region' : payload.get('participant_region'),
            'conference_region' : payload.get('conference_region'),
            'call_type' : payload.get('call_type'),
            'processing_state' : payload.get('processing_state'),
            'properties' : payload.get('properties'),
            'events' : payload.get('events'),
            'metrics' : payload.get('metrics'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'conference_sid': conference_sid or self._properties['conference_sid'],'participant_sid': participant_sid or self._properties['participant_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ConferenceParticipantContext(
                self._version,
                conference_sid=self._solution['conference_sid'],participant_sid=self._solution['participant_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.ConferenceParticipantInstance {}>'.format(context)



class ConferenceParticipantList(ListResource):
    def __init__(self, version: Version, conference_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'conference_sid': conference_sid,  }
        self._uri = '/Conferences/${conference_sid}/Participants'
        

    """
    def page(self, participant_sid, label, events, page_size):
        
        data = values.of({
            'participant_sid': participant_sid,'label': label,'events': events,'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return ConferenceParticipantPage(self._version, payload, conference_sid=self._solution['conference_sid'], )
    """


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ConferenceParticipantList>'

