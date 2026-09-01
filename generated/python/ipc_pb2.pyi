import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SenderHello(_message.Message):
    __slots__ = ("sender_id", "pid", "proto_hash")
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    PROTO_HASH_FIELD_NUMBER: _ClassVar[int]
    sender_id: int
    pid: int
    proto_hash: bytes
    def __init__(self, sender_id: _Optional[int] = ..., pid: _Optional[int] = ..., proto_hash: _Optional[bytes] = ...) -> None: ...

class AssignSession(_message.Message):
    __slots__ = ("manifest", "total_senders", "target_host", "target_port")
    MANIFEST_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SENDERS_FIELD_NUMBER: _ClassVar[int]
    TARGET_HOST_FIELD_NUMBER: _ClassVar[int]
    TARGET_PORT_FIELD_NUMBER: _ClassVar[int]
    manifest: _common_pb2.Manifest
    total_senders: int
    target_host: str
    target_port: int
    def __init__(self, manifest: _Optional[_Union[_common_pb2.Manifest, _Mapping]] = ..., total_senders: _Optional[int] = ..., target_host: _Optional[str] = ..., target_port: _Optional[int] = ...) -> None: ...

class UpdateRate(_message.Message):
    __slots__ = ("session_id", "rate_bps")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    RATE_BPS_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    rate_bps: int
    def __init__(self, session_id: _Optional[str] = ..., rate_bps: _Optional[int] = ...) -> None: ...

class Abort(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class SenderProgress(_message.Message):
    __slots__ = ("session_id", "stripes_done", "packets_sent", "bytes_sent")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    STRIPES_DONE_FIELD_NUMBER: _ClassVar[int]
    PACKETS_SENT_FIELD_NUMBER: _ClassVar[int]
    BYTES_SENT_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    stripes_done: int
    packets_sent: int
    bytes_sent: int
    def __init__(self, session_id: _Optional[str] = ..., stripes_done: _Optional[int] = ..., packets_sent: _Optional[int] = ..., bytes_sent: _Optional[int] = ...) -> None: ...

class SessionComplete(_message.Message):
    __slots__ = ("session_id", "packets_sent")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PACKETS_SENT_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    packets_sent: int
    def __init__(self, session_id: _Optional[str] = ..., packets_sent: _Optional[int] = ...) -> None: ...

class Heartbeat(_message.Message):
    __slots__ = ("process_id", "timestamp_unix_ms")
    PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    process_id: int
    timestamp_unix_ms: int
    def __init__(self, process_id: _Optional[int] = ..., timestamp_unix_ms: _Optional[int] = ...) -> None: ...
