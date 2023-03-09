r"""
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

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.flex_api.v1.assessments import AssessmentsList
from twilio.rest.flex_api.v1.channel import ChannelList
from twilio.rest.flex_api.v1.configuration import ConfigurationList
from twilio.rest.flex_api.v1.flex_flow import FlexFlowList
from twilio.rest.flex_api.v1.insights_assessments_comment import InsightsAssessmentsCommentList
from twilio.rest.flex_api.v1.insights_questionnaires import InsightsQuestionnairesList
from twilio.rest.flex_api.v1.insights_questionnaires_category import InsightsQuestionnairesCategoryList
from twilio.rest.flex_api.v1.insights_questionnaires_question import InsightsQuestionnairesQuestionList
from twilio.rest.flex_api.v1.insights_segments import InsightsSegmentsList
from twilio.rest.flex_api.v1.insights_session import InsightsSessionList
from twilio.rest.flex_api.v1.insights_settings_answer_sets import InsightsSettingsAnswerSetsList
from twilio.rest.flex_api.v1.insights_settings_comment import InsightsSettingsCommentList
from twilio.rest.flex_api.v1.insights_user_roles import InsightsUserRolesList
from twilio.rest.flex_api.v1.interaction import InteractionList
from twilio.rest.flex_api.v1.web_channel import WebChannelList


class V1(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of FlexApi

        :param domain: The Twilio.flex_api domain
        """
        super().__init__(domain)
        self.version = 'v1'
        self._assessments = None
        self._channel = None
        self._configuration = None
        self._flex_flow = None
        self._insights_assessments_comment = None
        self._insights_questionnaires = None
        self._insights_questionnaires_category = None
        self._insights_questionnaires_question = None
        self._insights_segments = None
        self._insights_session = None
        self._insights_settings_answer_sets = None
        self._insights_settings_comment = None
        self._insights_user_roles = None
        self._interaction = None
        self._web_channel = None
        
    @property
    def assessments(self) -> AssessmentsList:
        """
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsList
        """
        if self._assessments is None:
            self._assessments = AssessmentsList(self)
        return self._assessments

    @property
    def channel(self) -> ChannelList:
        """
        :rtype: twilio.rest.flex_api.v1.channel.ChannelList
        """
        if self._channel is None:
            self._channel = ChannelList(self)
        return self._channel

    @property
    def configuration(self) -> ConfigurationList:
        """
        :rtype: twilio.rest.flex_api.v1.configuration.ConfigurationList
        """
        if self._configuration is None:
            self._configuration = ConfigurationList(self)
        return self._configuration

    @property
    def flex_flow(self) -> FlexFlowList:
        """
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowList
        """
        if self._flex_flow is None:
            self._flex_flow = FlexFlowList(self)
        return self._flex_flow

    @property
    def insights_assessments_comment(self) -> InsightsAssessmentsCommentList:
        """
        :rtype: twilio.rest.flex_api.v1.insights_assessments_comment.InsightsAssessmentsCommentList
        """
        if self._insights_assessments_comment is None:
            self._insights_assessments_comment = InsightsAssessmentsCommentList(self)
        return self._insights_assessments_comment

    @property
    def insights_questionnaires(self) -> InsightsQuestionnairesList:
        """
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesList
        """
        if self._insights_questionnaires is None:
            self._insights_questionnaires = InsightsQuestionnairesList(self)
        return self._insights_questionnaires

    @property
    def insights_questionnaires_category(self) -> InsightsQuestionnairesCategoryList:
        """
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryList
        """
        if self._insights_questionnaires_category is None:
            self._insights_questionnaires_category = InsightsQuestionnairesCategoryList(self)
        return self._insights_questionnaires_category

    @property
    def insights_questionnaires_question(self) -> InsightsQuestionnairesQuestionList:
        """
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionList
        """
        if self._insights_questionnaires_question is None:
            self._insights_questionnaires_question = InsightsQuestionnairesQuestionList(self)
        return self._insights_questionnaires_question

    @property
    def insights_segments(self) -> InsightsSegmentsList:
        """
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsList
        """
        if self._insights_segments is None:
            self._insights_segments = InsightsSegmentsList(self)
        return self._insights_segments

    @property
    def insights_session(self) -> InsightsSessionList:
        """
        :rtype: twilio.rest.flex_api.v1.insights_session.InsightsSessionList
        """
        if self._insights_session is None:
            self._insights_session = InsightsSessionList(self)
        return self._insights_session

    @property
    def insights_settings_answer_sets(self) -> InsightsSettingsAnswerSetsList:
        """
        :rtype: twilio.rest.flex_api.v1.insights_settings_answer_sets.InsightsSettingsAnswerSetsList
        """
        if self._insights_settings_answer_sets is None:
            self._insights_settings_answer_sets = InsightsSettingsAnswerSetsList(self)
        return self._insights_settings_answer_sets

    @property
    def insights_settings_comment(self) -> InsightsSettingsCommentList:
        """
        :rtype: twilio.rest.flex_api.v1.insights_settings_comment.InsightsSettingsCommentList
        """
        if self._insights_settings_comment is None:
            self._insights_settings_comment = InsightsSettingsCommentList(self)
        return self._insights_settings_comment

    @property
    def insights_user_roles(self) -> InsightsUserRolesList:
        """
        :rtype: twilio.rest.flex_api.v1.insights_user_roles.InsightsUserRolesList
        """
        if self._insights_user_roles is None:
            self._insights_user_roles = InsightsUserRolesList(self)
        return self._insights_user_roles

    @property
    def interaction(self) -> InteractionList:
        """
        :rtype: twilio.rest.flex_api.v1.interaction.InteractionList
        """
        if self._interaction is None:
            self._interaction = InteractionList(self)
        return self._interaction

    @property
    def web_channel(self) -> WebChannelList:
        """
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelList
        """
        if self._web_channel is None:
            self._web_channel = WebChannelList(self)
        return self._web_channel

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1>'
