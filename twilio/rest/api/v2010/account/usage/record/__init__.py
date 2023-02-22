"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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
from twilio.rest.api.v2010.account.usage.record.all_time import AllTimeList
from twilio.rest.api.v2010.account.usage.record.daily import DailyList
from twilio.rest.api.v2010.account.usage.record.last_month import LastMonthList
from twilio.rest.api.v2010.account.usage.record.monthly import MonthlyList
from twilio.rest.api.v2010.account.usage.record.this_month import ThisMonthList
from twilio.rest.api.v2010.account.usage.record.today import TodayList
from twilio.rest.api.v2010.account.usage.record.yearly import YearlyList
from twilio.rest.api.v2010.account.usage.record.yesterday import YesterdayList


class RecordList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the RecordList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read.
        
        :returns: twilio.rest.api.v2010.account.usage.record.RecordList
        :rtype: twilio.rest.api.v2010.account.usage.record.RecordList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/${account_sid}/Usage/Records.json'.format(**self._solution)
        
        self._all_time = None
        self._daily = None
        self._last_month = None
        self._monthly = None
        self._this_month = None
        self._today = None
        self._yearly = None
        self._yesterday = None
        
    
    def stream(self, category=values.unset, start_date=values.unset, end_date=values.unset, include_subaccounts=values.unset, limit=None, page_size=None):
        """
        Streams RecordInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param UsageRecordCategory category: The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved.
        :param date start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`. You can also specify offsets from the current date, such as: `-30days`, which will set the start date to be 30 days before the current date.
        :param date end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.  You can also specify offsets from the current date, such as: `+30days`, which will set the end date to 30 days from the current date.
        :param bool include_subaccounts: Whether to include usage from the master account and all its subaccounts. Can be: `true` (the default) to include usage from the master account and all subaccounts or `false` to retrieve usage from only the specified account.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.usage.record.RecordInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            category=category,
            start_date=start_date,
            end_date=end_date,
            include_subaccounts=include_subaccounts,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, category=values.unset, start_date=values.unset, end_date=values.unset, include_subaccounts=values.unset, limit=None, page_size=None):
        """
        Lists RecordInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param UsageRecordCategory category: The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved.
        :param date start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`. You can also specify offsets from the current date, such as: `-30days`, which will set the start date to be 30 days before the current date.
        :param date end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.  You can also specify offsets from the current date, such as: `+30days`, which will set the end date to 30 days from the current date.
        :param bool include_subaccounts: Whether to include usage from the master account and all its subaccounts. Can be: `true` (the default) to include usage from the master account and all subaccounts or `false` to retrieve usage from only the specified account.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.usage.record.RecordInstance]
        """
        return list(self.stream(
            category=category,
            start_date=start_date,
            end_date=end_date,
            include_subaccounts=include_subaccounts,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, category=values.unset, start_date=values.unset, end_date=values.unset, include_subaccounts=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of RecordInstance records from the API.
        Request is executed immediately
        
        :param UsageRecordCategory category: The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved.
        :param date start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`. You can also specify offsets from the current date, such as: `-30days`, which will set the start date to be 30 days before the current date.
        :param date end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.  You can also specify offsets from the current date, such as: `+30days`, which will set the end date to 30 days from the current date.
        :param bool include_subaccounts: Whether to include usage from the master account and all its subaccounts. Can be: `true` (the default) to include usage from the master account and all subaccounts or `false` to retrieve usage from only the specified account.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RecordInstance
        :rtype: twilio.rest.api.v2010.account.usage.record.RecordPage
        """
        data = values.of({ 
            'Category': category,
            'StartDate': serialize.iso8601_date(start_date),
            'EndDate': serialize.iso8601_date(end_date),
            'IncludeSubaccounts': include_subaccounts,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return RecordPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of RecordInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RecordInstance
        :rtype: twilio.rest.api.v2010.account.usage.record.RecordPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return RecordPage(self._version, response, self._solution)


    @property
    def all_time(self):
        """
        Access the all_time

        :returns: twilio.rest.api.v2010.account.usage.record.AllTimeList
        :rtype: twilio.rest.api.v2010.account.usage.record.AllTimeList
        """
        if self._all_time is None:
            self._all_time = AllTimeList(self._version, account_sid=self._solution['account_sid'])
        return self.all_time

    @property
    def daily(self):
        """
        Access the daily

        :returns: twilio.rest.api.v2010.account.usage.record.DailyList
        :rtype: twilio.rest.api.v2010.account.usage.record.DailyList
        """
        if self._daily is None:
            self._daily = DailyList(self._version, account_sid=self._solution['account_sid'])
        return self.daily

    @property
    def last_month(self):
        """
        Access the last_month

        :returns: twilio.rest.api.v2010.account.usage.record.LastMonthList
        :rtype: twilio.rest.api.v2010.account.usage.record.LastMonthList
        """
        if self._last_month is None:
            self._last_month = LastMonthList(self._version, account_sid=self._solution['account_sid'])
        return self.last_month

    @property
    def monthly(self):
        """
        Access the monthly

        :returns: twilio.rest.api.v2010.account.usage.record.MonthlyList
        :rtype: twilio.rest.api.v2010.account.usage.record.MonthlyList
        """
        if self._monthly is None:
            self._monthly = MonthlyList(self._version, account_sid=self._solution['account_sid'])
        return self.monthly

    @property
    def this_month(self):
        """
        Access the this_month

        :returns: twilio.rest.api.v2010.account.usage.record.ThisMonthList
        :rtype: twilio.rest.api.v2010.account.usage.record.ThisMonthList
        """
        if self._this_month is None:
            self._this_month = ThisMonthList(self._version, account_sid=self._solution['account_sid'])
        return self.this_month

    @property
    def today(self):
        """
        Access the today

        :returns: twilio.rest.api.v2010.account.usage.record.TodayList
        :rtype: twilio.rest.api.v2010.account.usage.record.TodayList
        """
        if self._today is None:
            self._today = TodayList(self._version, account_sid=self._solution['account_sid'])
        return self.today

    @property
    def yearly(self):
        """
        Access the yearly

        :returns: twilio.rest.api.v2010.account.usage.record.YearlyList
        :rtype: twilio.rest.api.v2010.account.usage.record.YearlyList
        """
        if self._yearly is None:
            self._yearly = YearlyList(self._version, account_sid=self._solution['account_sid'])
        return self.yearly

    @property
    def yesterday(self):
        """
        Access the yesterday

        :returns: twilio.rest.api.v2010.account.usage.record.YesterdayList
        :rtype: twilio.rest.api.v2010.account.usage.record.YesterdayList
        """
        if self._yesterday is None:
            self._yesterday = YesterdayList(self._version, account_sid=self._solution['account_sid'])
        return self.yesterday


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.RecordList>'


class RecordPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the RecordPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.usage.record.RecordPage
        :rtype: twilio.rest.api.v2010.account.usage.record.RecordPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of RecordInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.usage.record.RecordInstance
        :rtype: twilio.rest.api.v2010.account.usage.record.RecordInstance
        """
        return RecordInstance(self._version, payload, account_sid=self._solution['account_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.RecordPage>'






class RecordInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'api_version' : payload.get('api_version'),
            'as_of' : payload.get('as_of'),
            'category' : payload.get('category'),
            'count' : payload.get('count'),
            'count_unit' : payload.get('count_unit'),
            'description' : payload.get('description'),
            'end_date' : payload.get('end_date'),
            'price' : payload.get('price'),
            'price_unit' : payload.get('price_unit'),
            'start_date' : payload.get('start_date'),
            'subresource_uris' : payload.get('subresource_uris'),
            'uri' : payload.get('uri'),
            'usage' : payload.get('usage'),
            'usage_unit' : payload.get('usage_unit'),
        }

        self._context = None
        self._solution = {
            'account_sid': account_sid or self._properties['account_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = RecordContext(
                self._version,
                account_sid=self._solution['account_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.RecordInstance {}>'.format(context)



