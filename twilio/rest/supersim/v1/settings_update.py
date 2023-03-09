r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Supersim
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
from twilio.base.page import Page


class SettingsUpdateList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the SettingsUpdateList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.supersim.v1.settings_update.SettingsUpdateList
        :rtype: twilio.rest.supersim.v1.settings_update.SettingsUpdateList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/SettingsUpdates'.format(**self._solution)
        
        
    
    def stream(self, sim=values.unset, status=values.unset, limit=None, page_size=None):
        """
        Streams SettingsUpdateInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str sim: Filter the Settings Updates by a Super SIM's SID or UniqueName.
        :param SettingsUpdateInstance.Status status: Filter the Settings Updates by status. Can be `scheduled`, `in-progress`, `successful`, or `failed`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.settings_update.SettingsUpdateInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            sim=sim,
            status=status,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, sim=values.unset, status=values.unset, limit=None, page_size=None):
        """
        Asynchronous coroutine that streams SettingsUpdateInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str sim: Filter the Settings Updates by a Super SIM's SID or UniqueName.
        :param SettingsUpdateInstance.Status status: Filter the Settings Updates by status. Can be `scheduled`, `in-progress`, `successful`, or `failed`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.settings_update.SettingsUpdateInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            sim=sim,
            status=status,
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, sim=values.unset, status=values.unset, limit=None, page_size=None):
        """
        Lists SettingsUpdateInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str sim: Filter the Settings Updates by a Super SIM's SID or UniqueName.
        :param SettingsUpdateInstance.Status status: Filter the Settings Updates by status. Can be `scheduled`, `in-progress`, `successful`, or `failed`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.settings_update.SettingsUpdateInstance]
        """
        return list(self.stream(
            sim=sim,
            status=status,
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, sim=values.unset, status=values.unset, limit=None, page_size=None):
        """
        Asynchronous coroutine that lists SettingsUpdateInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str sim: Filter the Settings Updates by a Super SIM's SID or UniqueName.
        :param SettingsUpdateInstance.Status status: Filter the Settings Updates by status. Can be `scheduled`, `in-progress`, `successful`, or `failed`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.settings_update.SettingsUpdateInstance]
        """
        return list(await self.stream_async(
            sim=sim,
            status=status,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, sim=values.unset, status=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of SettingsUpdateInstance records from the API.
        Request is executed immediately
        
        :param str sim: Filter the Settings Updates by a Super SIM's SID or UniqueName.
        :param SettingsUpdateInstance.Status status: Filter the Settings Updates by status. Can be `scheduled`, `in-progress`, `successful`, or `failed`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SettingsUpdateInstance
        :rtype: twilio.rest.supersim.v1.settings_update.SettingsUpdatePage
        """
        data = values.of({ 
            'Sim': sim,
            'Status': status,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return SettingsUpdatePage(self._version, response, self._solution)

    async def page_async(self, sim=values.unset, status=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronous coroutine that retrieve a single page of SettingsUpdateInstance records from the API.
        Request is executed immediately
        
        :param str sim: Filter the Settings Updates by a Super SIM's SID or UniqueName.
        :param SettingsUpdateInstance.Status status: Filter the Settings Updates by status. Can be `scheduled`, `in-progress`, `successful`, or `failed`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SettingsUpdateInstance
        :rtype: twilio.rest.supersim.v1.settings_update.SettingsUpdatePage
        """
        data = values.of({ 
            'Sim': sim,
            'Status': status,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return SettingsUpdatePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SettingsUpdateInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SettingsUpdateInstance
        :rtype: twilio.rest.supersim.v1.settings_update.SettingsUpdatePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return SettingsUpdatePage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronous coroutine that retrieve a specific page of SettingsUpdateInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SettingsUpdateInstance
        :rtype: twilio.rest.supersim.v1.settings_update.SettingsUpdatePage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return SettingsUpdatePage(self._version, response, self._solution)



    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.SettingsUpdateList>'


class SettingsUpdatePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SettingsUpdatePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.supersim.v1.settings_update.SettingsUpdatePage
        :rtype: twilio.rest.supersim.v1.settings_update.SettingsUpdatePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SettingsUpdateInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.supersim.v1.settings_update.SettingsUpdateInstance
        :rtype: twilio.rest.supersim.v1.settings_update.SettingsUpdateInstance
        """
        return SettingsUpdateInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.SettingsUpdatePage>'





class SettingsUpdateInstance(InstanceResource):

    class Status(object):
        SCHEDULED = "scheduled"
        IN_PROGRESS = "in-progress"
        SUCCESSFUL = "successful"
        FAILED = "failed"

    def __init__(self, version, payload):
        """
        Initialize the SettingsUpdateInstance
        :returns: twilio.rest.supersim.v1.settings_update.SettingsUpdateInstance
        :rtype: twilio.rest.supersim.v1.settings_update.SettingsUpdateInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'iccid': payload.get('iccid'),
            'sim_sid': payload.get('sim_sid'),
            'status': payload.get('status'),
            'packages': payload.get('packages'),
            'date_completed': deserialize.iso8601_datetime(payload.get('date_completed')),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
        }

        self._context = None
        self._solution = {  }
    
    
    @property
    def sid(self):
        """
        :returns: The unique identifier of this Settings Update.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def iccid(self):
        """
        :returns: The [ICCID](https://en.wikipedia.org/wiki/SIM_card#ICCID) associated with the SIM.
        :rtype: str
        """
        return self._properties['iccid']
    
    @property
    def sim_sid(self):
        """
        :returns: The SID of the Super SIM to which this Settings Update was applied.
        :rtype: str
        """
        return self._properties['sim_sid']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: SettingsUpdateInstance.Status
        """
        return self._properties['status']
    
    @property
    def packages(self):
        """
        :returns: Array containing the different Settings Packages that will be applied to the SIM after the update completes. Each object within the array indicates the name and the version of the Settings Package that will be on the SIM if the update is successful.
        :rtype: list[object]
        """
        return self._properties['packages']
    
    @property
    def date_completed(self):
        """
        :returns: The time, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, when the update successfully completed and the new settings were applied to the SIM.
        :rtype: datetime
        """
        return self._properties['date_completed']
    
    @property
    def date_created(self):
        """
        :returns: The date that this Settings Update was created, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date that this Settings Update was updated, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Supersim.V1.SettingsUpdateInstance {}>'.format(context)


