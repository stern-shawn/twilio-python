"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Conversations
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.conversations.v1.address_configuration import AddressConfigurationList
from twilio.rest.conversations.v1.configuration import ConfigurationList
from twilio.rest.conversations.v1.conversation import ConversationList
from twilio.rest.conversations.v1.credential import CredentialList
from twilio.rest.conversations.v1.participant_conversation import ParticipantConversationList
from twilio.rest.conversations.v1.role import RoleList
from twilio.rest.conversations.v1.service import ServiceList
from twilio.rest.conversations.v1.user import UserList


class V1(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of Conversations

        :param domain: The Twilio.conversations domain
        """
        super().__init__(domain)
        self.version = 'v1'
        self._address_configurations = None
        self._configuration = None
        self._conversations = None
        self._credentials = None
        self._participant_conversations = None
        self._roles = None
        self._services = None
        self._users = None
        
    @property
    def address_configurations(self) -> AddressConfigurationList:
        """
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationList
        """
        if self._address_configurations is None:
            self._address_configurations = AddressConfigurationList(self)
        return self._address_configurations

    @property
    def configuration(self) -> ConfigurationList:
        """
        :rtype: twilio.rest.conversations.v1.configuration.ConfigurationList
        """
        if self._configuration is None:
            self._configuration = ConfigurationList(self)
        return self._configuration

    @property
    def conversations(self) -> ConversationList:
        """
        :rtype: twilio.rest.conversations.v1.conversation.ConversationList
        """
        if self._conversations is None:
            self._conversations = ConversationList(self)
        return self._conversations

    @property
    def credentials(self) -> CredentialList:
        """
        :rtype: twilio.rest.conversations.v1.credential.CredentialList
        """
        if self._credentials is None:
            self._credentials = CredentialList(self)
        return self._credentials

    @property
    def participant_conversations(self) -> ParticipantConversationList:
        """
        :rtype: twilio.rest.conversations.v1.participant_conversation.ParticipantConversationList
        """
        if self._participant_conversations is None:
            self._participant_conversations = ParticipantConversationList(self)
        return self._participant_conversations

    @property
    def roles(self) -> RoleList:
        """
        :rtype: twilio.rest.conversations.v1.role.RoleList
        """
        if self._roles is None:
            self._roles = RoleList(self)
        return self._roles

    @property
    def services(self) -> ServiceList:
        """
        :rtype: twilio.rest.conversations.v1.service.ServiceList
        """
        if self._services is None:
            self._services = ServiceList(self)
        return self._services

    @property
    def users(self) -> UserList:
        """
        :rtype: twilio.rest.conversations.v1.user.UserList
        """
        if self._users is None:
            self._users = UserList(self)
        return self._users

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1>'
