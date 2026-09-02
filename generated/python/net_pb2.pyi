import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataPacket(_message.Message):
    __slots__ = ("session_id", "block_id", "symbol_id", "payload")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    block_id: int
    symbol_id: int
    payload: bytes
    def __init__(self, session_id: _Optional[str] = ..., block_id: _Optional[int] = ..., symbol_id: _Optional[int] = ..., payload: _Optional[bytes] = ...) -> None: ...

class NetworkSpeedState(_message.Message):
    __slots__ = ("session_id", "burst_index", "rate_bps")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    BURST_INDEX_FIELD_NUMBER: _ClassVar[int]
    RATE_BPS_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    burst_index: int
    rate_bps: int
    def __init__(self, session_id: _Optional[str] = ..., burst_index: _Optional[int] = ..., rate_bps: _Optional[int] = ...) -> None: ...

class Frame(_message.Message):
    __slots__ = ("data", "manifest", "end")
    DATA_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    data: DataPacket
    manifest: _common_pb2.Manifest
    end: _common_pb2.SessionEnd
    def __init__(self, data: _Optional[_Union[DataPacket, _Mapping]] = ..., manifest: _Optional[_Union[_common_pb2.Manifest, _Mapping]] = ..., end: _Optional[_Union[_common_pb2.SessionEnd, _Mapping]] = ...) -> None: ...
