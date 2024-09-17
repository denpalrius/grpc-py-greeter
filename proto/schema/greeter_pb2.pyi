from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GreetingRequest(_message.Message):
    __slots__ = ("salutation", "name")
    SALUTATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    salutation: str
    name: str
    def __init__(self, salutation: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class GreetingResponse(_message.Message):
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
    __slots__ = ("messages", "timestamp")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedScalarFieldContainer[str]
    timestamp: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, messages: _Optional[_Iterable[str]] = ..., timestamp: _Optional[_Iterable[str]] = ...) -> None: ...
