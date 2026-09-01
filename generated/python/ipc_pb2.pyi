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

class LocalCongestion(_message.Message):
    __slots__ = ("session_id", "enobufs_count", "qdisc_drops", "current_rate_bps")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ENOBUFS_COUNT_FIELD_NUMBER: _ClassVar[int]
    QDISC_DROPS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_RATE_BPS_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    enobufs_count: int
    qdisc_drops: int
    current_rate_bps: int
    def __init__(self, session_id: _Optional[str] = ..., enobufs_count: _Optional[int] = ..., qdisc_drops: _Optional[int] = ..., current_rate_bps: _Optional[int] = ...) -> None: ...

class Envelope(_message.Message):
    __slots__ = ("sender_hello", "heartbeat", "sender_progress", "session_complete", "local_congestion", "assign_session", "update_rate", "abort")
    SENDER_HELLO_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    SENDER_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    SESSION_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_CONGESTION_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_SESSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_RATE_FIELD_NUMBER: _ClassVar[int]
    ABORT_FIELD_NUMBER: _ClassVar[int]
    sender_hello: SenderHello
    heartbeat: Heartbeat
    sender_progress: SenderProgress
    session_complete: SessionComplete
    local_congestion: LocalCongestion
    assign_session: AssignSession
    update_rate: UpdateRate
    abort: Abort
    def __init__(self, sender_hello: _Optional[_Union[SenderHello, _Mapping]] = ..., heartbeat: _Optional[_Union[Heartbeat, _Mapping]] = ..., sender_progress: _Optional[_Union[SenderProgress, _Mapping]] = ..., session_complete: _Optional[_Union[SessionComplete, _Mapping]] = ..., local_congestion: _Optional[_Union[LocalCongestion, _Mapping]] = ..., assign_session: _Optional[_Union[AssignSession, _Mapping]] = ..., update_rate: _Optional[_Union[UpdateRate, _Mapping]] = ..., abort: _Optional[_Union[Abort, _Mapping]] = ...) -> None: ...
