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

# from twilio.rest.conference.conference_participant import ConferenceParticipantListInstance


class ConferenceContext(InstanceContext):
    def __init__(self, version: Version, conference_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'conference_sid': conference_sid,  }
        self._uri = '/Conferences/${conference_sid}'
        
        self._conference_participants = None
    
    def fetch(self):
        
        """
        Fetch the ConferenceInstance

        :returns: The fetched ConferenceInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ConferenceInstance(self._version, payload, conference_sid=self._solution['conference_sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ConferenceContext>'



class ConferenceInstance(InstanceResource):
    def __init__(self, version, payload, conference_sid: str):
        super().__init__(version)
        self._properties = { 
            'conference_sid' : payload.get('conference_sid'),
            'account_sid' : payload.get('account_sid'),
            'friendly_name' : payload.get('friendly_name'),
            'create_time' : payload.get('create_time'),
            'start_time' : payload.get('start_time'),
            'end_time' : payload.get('end_time'),
            'duration_seconds' : payload.get('duration_seconds'),
            'connect_duration_seconds' : payload.get('connect_duration_seconds'),
            'status' : payload.get('status'),
            'max_participants' : payload.get('max_participants'),
            'max_concurrent_participants' : payload.get('max_concurrent_participants'),
            'unique_participants' : payload.get('unique_participants'),
            'end_reason' : payload.get('end_reason'),
            'ended_by' : payload.get('ended_by'),
            'mixer_region' : payload.get('mixer_region'),
            'mixer_region_requested' : payload.get('mixer_region_requested'),
            'recording_enabled' : payload.get('recording_enabled'),
            'detected_issues' : payload.get('detected_issues'),
            'tags' : payload.get('tags'),
            'tag_info' : payload.get('tag_info'),
            'processing_state' : payload.get('processing_state'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'conference_sid': conference_sid or self._properties['conference_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ConferenceContext(
                self._version,
                conference_sid=self._solution['conference_sid'],
            )
        return self._context

    @property
    def conference_participants(self):
        return self._proxy.conference_participants
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.ConferenceInstance {}>'.format(context)



class ConferenceListInstance(ListResource):
    def __init__(self, version: Version):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Conferences'
        
    
    """
    def page(self, conference_sid, friendly_name, status, created_after, created_before, mixer_region, tags, subaccount, detected_issues, end_reason, page_size):
        
        data = values.of({
            'conference_sid': conference_sid,'friendly_name': friendly_name,'status': status,'created_after': created_after,'created_before': created_before,'mixer_region': mixer_region,'tags': tags,'subaccount': subaccount,'detected_issues': detected_issues,'end_reason': end_reason,'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return ConferencePage(self._version, payload, )
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ConferenceListInstance>'
