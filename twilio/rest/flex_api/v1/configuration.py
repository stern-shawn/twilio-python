"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
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


class ConfigurationContext(InstanceContext):
    def __init__(self, version: Version):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Configuration'
        
    
    def fetch(self, ui_version):
        
        """
        Fetch the ConfigurationInstance

        :returns: The fetched ConfigurationInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ConfigurationInstance(self._version, payload, )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ConfigurationContext>'



class ConfigurationInstance(InstanceResource):
    def __init__(self, version, payload):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'attributes' : payload.get('attributes'),
            'status' : payload.get('status'),
            'taskrouter_workspace_sid' : payload.get('taskrouter_workspace_sid'),
            'taskrouter_target_workflow_sid' : payload.get('taskrouter_target_workflow_sid'),
            'taskrouter_target_taskqueue_sid' : payload.get('taskrouter_target_taskqueue_sid'),
            'taskrouter_taskqueues' : payload.get('taskrouter_taskqueues'),
            'taskrouter_skills' : payload.get('taskrouter_skills'),
            'taskrouter_worker_channels' : payload.get('taskrouter_worker_channels'),
            'taskrouter_worker_attributes' : payload.get('taskrouter_worker_attributes'),
            'taskrouter_offline_activity_sid' : payload.get('taskrouter_offline_activity_sid'),
            'runtime_domain' : payload.get('runtime_domain'),
            'messaging_service_instance_sid' : payload.get('messaging_service_instance_sid'),
            'chat_service_instance_sid' : payload.get('chat_service_instance_sid'),
            'flex_service_instance_sid' : payload.get('flex_service_instance_sid'),
            'ui_language' : payload.get('ui_language'),
            'ui_attributes' : payload.get('ui_attributes'),
            'ui_dependencies' : payload.get('ui_dependencies'),
            'ui_version' : payload.get('ui_version'),
            'service_version' : payload.get('service_version'),
            'call_recording_enabled' : payload.get('call_recording_enabled'),
            'call_recording_webhook_url' : payload.get('call_recording_webhook_url'),
            'crm_enabled' : payload.get('crm_enabled'),
            'crm_type' : payload.get('crm_type'),
            'crm_callback_url' : payload.get('crm_callback_url'),
            'crm_fallback_url' : payload.get('crm_fallback_url'),
            'crm_attributes' : payload.get('crm_attributes'),
            'public_attributes' : payload.get('public_attributes'),
            'plugin_service_enabled' : payload.get('plugin_service_enabled'),
            'plugin_service_attributes' : payload.get('plugin_service_attributes'),
            'integrations' : payload.get('integrations'),
            'outbound_call_flows' : payload.get('outbound_call_flows'),
            'serverless_service_sids' : payload.get('serverless_service_sids'),
            'queue_stats_configuration' : payload.get('queue_stats_configuration'),
            'notifications' : payload.get('notifications'),
            'markdown' : payload.get('markdown'),
            'url' : payload.get('url'),
            'flex_insights_hr' : payload.get('flex_insights_hr'),
            'flex_insights_drilldown' : payload.get('flex_insights_drilldown'),
            'flex_url' : payload.get('flex_url'),
            'channel_configs' : payload.get('channel_configs'),
            'debugger_integration' : payload.get('debugger_integration'),
            'flex_ui_status_report' : payload.get('flex_ui_status_report'),
        }

        self._context = None
        self._solution = {
            
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ConfigurationContext(
                self._version,
                
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.ConfigurationInstance {}>'.format(context)



class ConfigurationListInstance(ListResource):
    def __init__(self, version: Version):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = ''
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ConfigurationListInstance>'

