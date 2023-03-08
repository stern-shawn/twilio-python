"""
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


class SimIpAddressList(ListResource):

    def __init__(self, version: Version, sim_sid: str):
        """
        Initialize the SimIpAddressList

        :param Version version: Version that contains the resource
        :param sim_sid: The SID of the Super SIM to list IP Addresses for.
        
        :returns: twilio.rest.supersim.v1.sim.sim_ip_address.SimIpAddressList
        :rtype: twilio.rest.supersim.v1.sim.sim_ip_address.SimIpAddressList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'sim_sid': sim_sid,  }
        self._uri = '/Sims/{sim_sid}/IpAddresses'.format(**self._solution)
        
        
    
    def stream(self, limit=None, page_size=None):
        """
        Streams SimIpAddressInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.sim.sim_ip_address.SimIpAddressInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists SimIpAddressInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.sim.sim_ip_address.SimIpAddressInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of SimIpAddressInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SimIpAddressInstance
        :rtype: twilio.rest.supersim.v1.sim.sim_ip_address.SimIpAddressPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return SimIpAddressPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SimIpAddressInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SimIpAddressInstance
        :rtype: twilio.rest.supersim.v1.sim.sim_ip_address.SimIpAddressPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return SimIpAddressPage(self._version, response, self._solution)



    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.SimIpAddressList>'


class SimIpAddressPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SimIpAddressPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.supersim.v1.sim.sim_ip_address.SimIpAddressPage
        :rtype: twilio.rest.supersim.v1.sim.sim_ip_address.SimIpAddressPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SimIpAddressInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.supersim.v1.sim.sim_ip_address.SimIpAddressInstance
        :rtype: twilio.rest.supersim.v1.sim.sim_ip_address.SimIpAddressInstance
        """
        return SimIpAddressInstance(self._version, payload, sim_sid=self._solution['sim_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.SimIpAddressPage>'





class SimIpAddressInstance(InstanceResource):

    class IpAddressVersion(object):
        IPV4 = "IPv4"
        IPV6 = "IPv6"

    def __init__(self, version, payload, sim_sid: str):
        """
        Initialize the SimIpAddressInstance
        :returns: twilio.rest.supersim.v1.sim.sim_ip_address.SimIpAddressInstance
        :rtype: twilio.rest.supersim.v1.sim.sim_ip_address.SimIpAddressInstance
        """
        super().__init__(version)

        self._properties = { 
            'ip_address': payload.get('ip_address'),
            'ip_address_version': payload.get('ip_address_version'),
        }

        self._context = None
        self._solution = { 'sim_sid': sim_sid,  }
    
    
    @property
    def ip_address(self):
        """
        :returns: IP address assigned to the given Super SIM
        :rtype: str
        """
        return self._properties['ip_address']
    
    @property
    def ip_address_version(self):
        """
        :returns: 
        :rtype: SimIpAddressInstance.IpAddressVersion
        """
        return self._properties['ip_address_version']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Supersim.V1.SimIpAddressInstance {}>'.format(context)


