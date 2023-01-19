"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Autopilot
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.domain import Domain
from twilio.rest.autopilot.v1 import V1

class Autopilot(Domain):
    def __init__(self, twilio):
        """
        Initialize the Autopilot Domain

        :returns: Domain for Autopilot
        :rtype: twilio.rest.v1.Autopilot
        """
        super(Autopilot, self).__init__(twilio)
        self.base_url = 'https://Autopilot.twilio.com'
        self._V1 = None

    @property
    def V1(self):
        """
        :returns: Versions v1 of Autopilot
        :rtype: twilio.rest.Autopilot.v1
        """
        if self._V1 is None:
            self._V1 = V1(self)
        return self._V1
    

    @property
    def assistants(self):
        """
        :rtype: twilio.rest.v1.assistants
        """
        return self.v1.assistants
    

    @property
    def restore_assistant(self):
        """
        :rtype: twilio.rest.v1.restore_assistant
        """
        return self.v1.restore_assistant
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot>'
