from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HelloRequest(_message.Message):
    __slots__ = ("name", "language", "formal")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    FORMAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    language: str
    formal: bool
    def __init__(self, name: _Optional[str] = ..., language: _Optional[str] = ..., formal: bool = ...) -> None: ...

class HelloResponse(_message.Message):
    __slots__ = ("message", "timestamp")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    message: str
    timestamp: str
    def __init__(self, message: _Optional[str] = ..., timestamp: _Optional[str] = ...) -> None: ...

class GoodbyeRequest(_message.Message):
    __slots__ = ("name", "language", "formal")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    FORMAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    language: str
    formal: bool
    def __init__(self, name: _Optional[str] = ..., language: _Optional[str] = ..., formal: bool = ...) -> None: ...

class GoodbyeResponse(_message.Message):
    __slots__ = ("message", "timestamp")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    message: str
    timestamp: str
    def __init__(self, message: _Optional[str] = ..., timestamp: _Optional[str] = ...) -> None: ...

class GreetingHistoryRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GreetingHistoryResponse(_message.Message):
    __slots__ = ("messages", "timestamps")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedScalarFieldContainer[str]
    timestamps: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, messages: _Optional[_Iterable[str]] = ..., timestamps: _Optional[_Iterable[str]] = ...) -> None: ...
