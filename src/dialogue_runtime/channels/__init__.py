# -*- coding: utf-8 -*-
"""
通道模块

提供与用户交互的通道（Channel）实现。
"""

from dialogue_runtime.channels.base_channel import (
    InputChannel,
    OutputChannel,
    UserMessage,
    CollectingOutputChannel,
)
from dialogue_runtime.channels.rest_channel import RestChannel
from dialogue_runtime.channels.socketio_channel import SocketIOChannel
from dialogue_runtime.channels.console_channel import ConsoleChannel
from dialogue_runtime.channels.inspect_proxy import InspectProxy

__all__ = [
    "InputChannel",
    "OutputChannel",
    "UserMessage",
    "CollectingOutputChannel",
    "RestChannel",
    "SocketIOChannel",
    "ConsoleChannel",
    "InspectProxy",
]
