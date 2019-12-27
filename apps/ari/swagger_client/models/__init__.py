# coding: utf-8

# flake8: noqa
"""
    localhost:8088

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 4.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from swagger_client.models.application import Application
from swagger_client.models.asterisk_info import AsteriskInfo
from swagger_client.models.asterisk_ping import AsteriskPing
from swagger_client.models.bridge import Bridge
from swagger_client.models.build_info import BuildInfo
from swagger_client.models.caller_id import CallerID
from swagger_client.models.channel import Channel
from swagger_client.models.config_info import ConfigInfo
from swagger_client.models.config_tuple import ConfigTuple
from swagger_client.models.contact_info import ContactInfo
from swagger_client.models.device_state import DeviceState
from swagger_client.models.dialed import Dialed
from swagger_client.models.dialplan_cep import DialplanCEP
from swagger_client.models.endpoint import Endpoint
from swagger_client.models.external_media import ExternalMedia
from swagger_client.models.format_lang_pair import FormatLangPair
from swagger_client.models.live_recording import LiveRecording
from swagger_client.models.log_channel import LogChannel
from swagger_client.models.mailbox import Mailbox
from swagger_client.models.message import Message
from swagger_client.models.module import Module
from swagger_client.models.peer import Peer
from swagger_client.models.playback import Playback
from swagger_client.models.rt_pstat import RTPstat
from swagger_client.models.set_id import SetId
from swagger_client.models.sound import Sound
from swagger_client.models.status_info import StatusInfo
from swagger_client.models.stored_recording import StoredRecording
from swagger_client.models.system_info import SystemInfo
from swagger_client.models.text_message import TextMessage
from swagger_client.models.text_message_variable import TextMessageVariable
from swagger_client.models.variable import Variable
from swagger_client.models.event import Event
from swagger_client.models.missing_params import MissingParams
from swagger_client.models.application_move_failed import ApplicationMoveFailed
from swagger_client.models.application_replaced import ApplicationReplaced
from swagger_client.models.bridge_attended_transfer import BridgeAttendedTransfer
from swagger_client.models.bridge_blind_transfer import BridgeBlindTransfer
from swagger_client.models.bridge_created import BridgeCreated
from swagger_client.models.bridge_destroyed import BridgeDestroyed
from swagger_client.models.bridge_merged import BridgeMerged
from swagger_client.models.bridge_varset import BridgeVarset
from swagger_client.models.bridge_video_source_changed import BridgeVideoSourceChanged
from swagger_client.models.channel_caller_id import ChannelCallerId
from swagger_client.models.channel_connected_line import ChannelConnectedLine
from swagger_client.models.channel_created import ChannelCreated
from swagger_client.models.channel_destroyed import ChannelDestroyed
from swagger_client.models.channel_dialplan import ChannelDialplan
from swagger_client.models.channel_dtmf_received import ChannelDtmfReceived
from swagger_client.models.channel_entered_bridge import ChannelEnteredBridge
from swagger_client.models.channel_hangup_request import ChannelHangupRequest
from swagger_client.models.channel_hold import ChannelHold
from swagger_client.models.channel_left_bridge import ChannelLeftBridge
from swagger_client.models.channel_moh_start import ChannelMohStart
from swagger_client.models.channel_moh_stop import ChannelMohStop
from swagger_client.models.channel_state_change import ChannelStateChange
from swagger_client.models.channel_talking_finished import ChannelTalkingFinished
from swagger_client.models.channel_talking_started import ChannelTalkingStarted
from swagger_client.models.channel_unhold import ChannelUnhold
from swagger_client.models.channel_userevent import ChannelUserevent
from swagger_client.models.channel_varset import ChannelVarset
from swagger_client.models.contact_status_change import ContactStatusChange
from swagger_client.models.device_state_changed import DeviceStateChanged
from swagger_client.models.dial import Dial
from swagger_client.models.endpoint_state_change import EndpointStateChange
from swagger_client.models.peer_status_change import PeerStatusChange
from swagger_client.models.playback_continuing import PlaybackContinuing
from swagger_client.models.playback_finished import PlaybackFinished
from swagger_client.models.playback_started import PlaybackStarted
from swagger_client.models.recording_failed import RecordingFailed
from swagger_client.models.recording_finished import RecordingFinished
from swagger_client.models.recording_started import RecordingStarted
from swagger_client.models.stasis_end import StasisEnd
from swagger_client.models.stasis_start import StasisStart
from swagger_client.models.text_message_received import TextMessageReceived
