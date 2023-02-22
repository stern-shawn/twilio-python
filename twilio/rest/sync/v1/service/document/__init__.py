"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Sync
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
from twilio.rest.sync.v1.service.document.document_permission import DocumentPermissionList


class DocumentList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the DocumentList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document resources to read.
        
        :returns: twilio.rest.sync.v1.service.document.DocumentList
        :rtype: twilio.rest.sync.v1.service.document.DocumentList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/${service_sid}/Documents'.format(**self._solution)
        
        
    
    
    
    
    def create(self, unique_name=values.unset, data=values.unset, ttl=values.unset):
        """
        Create the DocumentInstance
        :param str unique_name: An application-defined string that uniquely identifies the Sync Document
        :param object data: A JSON string that represents an arbitrary, schema-less object that the Sync Document stores. Can be up to 16 KiB in length.
        :param int ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Sync Document expires and is deleted (the Sync Document's time-to-live).
        
        :returns: The created DocumentInstance
        :rtype: twilio.rest.sync.v1.service.document.DocumentInstance
        """
        data = values.of({ 
            'UniqueName': unique_name,
            'Data': serialize.object(data),
            'Ttl': ttl,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return DocumentInstance(self._version, payload, service_sid=self._solution['service_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams DocumentInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.sync.v1.service.document.DocumentInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists DocumentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.sync.v1.service.document.DocumentInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of DocumentInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DocumentInstance
        :rtype: twilio.rest.sync.v1.service.document.DocumentPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return DocumentPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of DocumentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DocumentInstance
        :rtype: twilio.rest.sync.v1.service.document.DocumentPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return DocumentPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a DocumentContext
        
        :param sid: The SID of the Document resource to update. Can be the Document resource's `sid` or its `unique_name`.
        
        :returns: twilio.rest.sync.v1.service.document.DocumentContext
        :rtype: twilio.rest.sync.v1.service.document.DocumentContext
        """
        return DocumentContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a DocumentContext
        
        :param sid: The SID of the Document resource to update. Can be the Document resource's `sid` or its `unique_name`.
        
        :returns: twilio.rest.sync.v1.service.document.DocumentContext
        :rtype: twilio.rest.sync.v1.service.document.DocumentContext
        """
        return DocumentContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.DocumentList>'










class DocumentPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the DocumentPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.sync.v1.service.document.DocumentPage
        :rtype: twilio.rest.sync.v1.service.document.DocumentPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DocumentInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.sync.v1.service.document.DocumentInstance
        :rtype: twilio.rest.sync.v1.service.document.DocumentInstance
        """
        return DocumentInstance(self._version, payload, service_sid=self._solution['service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.DocumentPage>'





class DocumentContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'sid': sid,  }
        self._uri = '/Services/${service_sid}/Documents/${sid}'
        
        self._document_permissions = None
    
    def delete(self):
        
        

        """
        Deletes the DocumentInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the DocumentInstance

        :returns: The fetched DocumentInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return DocumentInstance(self._version, payload, service_sid=self._solution['service_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, if_match, data, ttl):
        data = values.of({
            'if_match': if_match,'data': data,'ttl': ttl,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return DocumentInstance(self._version, payload, service_sid=self._solution['service_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.DocumentContext>'



class DocumentInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'unique_name' : payload.get('unique_name'),
            'account_sid' : payload.get('account_sid'),
            'service_sid' : payload.get('service_sid'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
            'revision' : payload.get('revision'),
            'data' : payload.get('data'),
            'date_expires' : payload.get('date_expires'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'created_by' : payload.get('created_by'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = DocumentContext(
                self._version,
                service_sid=self._solution['service_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def document_permissions(self):
        return self._proxy.document_permissions
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Sync.V1.DocumentInstance {}>'.format(context)



