r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Video
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.video.v1.composition import CompositionList
from twilio.rest.video.v1.composition_hook import CompositionHookList
from twilio.rest.video.v1.composition_settings import CompositionSettingsList
from twilio.rest.video.v1.recording import RecordingList
from twilio.rest.video.v1.recording_settings import RecordingSettingsList
from twilio.rest.video.v1.room import RoomList


class V1(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of Video

        :param domain: The Twilio.video domain
        """
        super().__init__(domain)
        self.version = 'v1'
        self._compositions = None
        self._composition_hooks = None
        self._composition_settings = None
        self._recordings = None
        self._recording_settings = None
        self._rooms = None
        
    @property
    def compositions(self) -> CompositionList:
        """
        :rtype: twilio.rest.video.v1.composition.CompositionList
        """
        if self._compositions is None:
            self._compositions = CompositionList(self)
        return self._compositions

    @property
    def composition_hooks(self) -> CompositionHookList:
        """
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookList
        """
        if self._composition_hooks is None:
            self._composition_hooks = CompositionHookList(self)
        return self._composition_hooks

    @property
    def composition_settings(self) -> CompositionSettingsList:
        """
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsList
        """
        if self._composition_settings is None:
            self._composition_settings = CompositionSettingsList(self)
        return self._composition_settings

    @property
    def recordings(self) -> RecordingList:
        """
        :rtype: twilio.rest.video.v1.recording.RecordingList
        """
        if self._recordings is None:
            self._recordings = RecordingList(self)
        return self._recordings

    @property
    def recording_settings(self) -> RecordingSettingsList:
        """
        :rtype: twilio.rest.video.v1.recording_settings.RecordingSettingsList
        """
        if self._recording_settings is None:
            self._recording_settings = RecordingSettingsList(self)
        return self._recording_settings

    @property
    def rooms(self) -> RoomList:
        """
        :rtype: twilio.rest.video.v1.room.RoomList
        """
        if self._rooms is None:
            self._rooms = RoomList(self)
        return self._rooms

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1>'
