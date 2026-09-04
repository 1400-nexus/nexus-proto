import common_pb2 as _common_pb2
import ipc_pb2 as _ipc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReceiverHello(_message.Message):
    __slots__ = ("receiver_id", "pid", "listen_port", "proto_hash")
    RECEIVER_ID_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    LISTEN_PORT_FIELD_NUMBER: _ClassVar[int]
    PROTO_HASH_FIELD_NUMBER: _ClassVar[int]
    receiver_id: int
    pid: int
    listen_port: int
    proto_hash: bytes
    def __init__(self, receiver_id: _Optional[int] = ..., pid: _Optional[int] = ..., listen_port: _Optional[int] = ..., proto_hash: _Optional[bytes] = ...) -> None: ...

class ManifestSeen(_message.Message):
    __slots__ = ("receiver_id", "manifest")
    RECEIVER_ID_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_FIELD_NUMBER: _ClassVar[int]
    receiver_id: int
    manifest: _common_pb2.Manifest
    def __init__(self, receiver_id: _Optional[int] = ..., manifest: _Optional[_Union[_common_pb2.Manifest, _Mapping]] = ...) -> None: ...

class BlockDecoded(_message.Message):
    __slots__ = ("session_id", "receiver_id", "block_ids")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_ID_FIELD_NUMBER: _ClassVar[int]
    BLOCK_IDS_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    receiver_id: int
    block_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, session_id: _Optional[str] = ..., receiver_id: _Optional[int] = ..., block_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class ReceiverStats(_message.Message):
    __slots__ = ("receiver_id", "pkts_ok", "crc_fail", "bad_magic", "unparsable", "duplicates", "no_session", "arena_exhausted", "kernel_drops", "arena_high_water_pct")
    RECEIVER_ID_FIELD_NUMBER: _ClassVar[int]
    PKTS_OK_FIELD_NUMBER: _ClassVar[int]
    CRC_FAIL_FIELD_NUMBER: _ClassVar[int]
    BAD_MAGIC_FIELD_NUMBER: _ClassVar[int]
    UNPARSABLE_FIELD_NUMBER: _ClassVar[int]
    DUPLICATES_FIELD_NUMBER: _ClassVar[int]
    NO_SESSION_FIELD_NUMBER: _ClassVar[int]
    ARENA_EXHAUSTED_FIELD_NUMBER: _ClassVar[int]
    KERNEL_DROPS_FIELD_NUMBER: _ClassVar[int]
    ARENA_HIGH_WATER_PCT_FIELD_NUMBER: _ClassVar[int]
    receiver_id: int
    pkts_ok: int
    crc_fail: int
    bad_magic: int
    unparsable: int
    duplicates: int
    no_session: int
    arena_exhausted: int
    kernel_drops: int
    arena_high_water_pct: int
    def __init__(self, receiver_id: _Optional[int] = ..., pkts_ok: _Optional[int] = ..., crc_fail: _Optional[int] = ..., bad_magic: _Optional[int] = ..., unparsable: _Optional[int] = ..., duplicates: _Optional[int] = ..., no_session: _Optional[int] = ..., arena_exhausted: _Optional[int] = ..., kernel_drops: _Optional[int] = ..., arena_high_water_pct: _Optional[int] = ...) -> None: ...

class Config(_message.Message):
    __slots__ = ("shm_name", "staging_dir", "journal_dir")
    SHM_NAME_FIELD_NUMBER: _ClassVar[int]
    STAGING_DIR_FIELD_NUMBER: _ClassVar[int]
    JOURNAL_DIR_FIELD_NUMBER: _ClassVar[int]
    shm_name: str
    staging_dir: str
    journal_dir: str
    def __init__(self, shm_name: _Optional[str] = ..., staging_dir: _Optional[str] = ..., journal_dir: _Optional[str] = ...) -> None: ...

class SessionOpen(_message.Message):
    __slots__ = ("session_id", "dest_path", "total_blocks", "k", "n", "block_bytes", "block_table_offset", "bitmap_offset")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    DEST_PATH_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    K_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    BLOCK_BYTES_FIELD_NUMBER: _ClassVar[int]
    BLOCK_TABLE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    BITMAP_OFFSET_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    dest_path: str
    total_blocks: int
    k: int
    n: int
    block_bytes: int
    block_table_offset: int
    bitmap_offset: int
    def __init__(self, session_id: _Optional[str] = ..., dest_path: _Optional[str] = ..., total_blocks: _Optional[int] = ..., k: _Optional[int] = ..., n: _Optional[int] = ..., block_bytes: _Optional[int] = ..., block_table_offset: _Optional[int] = ..., bitmap_offset: _Optional[int] = ...) -> None: ...

class PurgeSession(_message.Message):
    __slots__ = ("session_id", "reason")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    reason: str
    def __init__(self, session_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class RxEnvelope(_message.Message):
    __slots__ = ("receiver_hello", "manifest_seen", "block_decoded", "receiver_stats", "heartbeat", "config", "session_open", "purge_session")
    RECEIVER_HELLO_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_SEEN_FIELD_NUMBER: _ClassVar[int]
    BLOCK_DECODED_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_STATS_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    SESSION_OPEN_FIELD_NUMBER: _ClassVar[int]
    PURGE_SESSION_FIELD_NUMBER: _ClassVar[int]
    receiver_hello: ReceiverHello
    manifest_seen: ManifestSeen
    block_decoded: BlockDecoded
    receiver_stats: ReceiverStats
    heartbeat: _ipc_pb2.Heartbeat
    config: Config
    session_open: SessionOpen
    purge_session: PurgeSession
    def __init__(self, receiver_hello: _Optional[_Union[ReceiverHello, _Mapping]] = ..., manifest_seen: _Optional[_Union[ManifestSeen, _Mapping]] = ..., block_decoded: _Optional[_Union[BlockDecoded, _Mapping]] = ..., receiver_stats: _Optional[_Union[ReceiverStats, _Mapping]] = ..., heartbeat: _Optional[_Union[_ipc_pb2.Heartbeat, _Mapping]] = ..., config: _Optional[_Union[Config, _Mapping]] = ..., session_open: _Optional[_Union[SessionOpen, _Mapping]] = ..., purge_session: _Optional[_Union[PurgeSession, _Mapping]] = ...) -> None: ...
