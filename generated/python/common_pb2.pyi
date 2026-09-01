from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Manifest(_message.Message):
    __slots__ = ("session_id", "filepath", "file_size", "file_hash", "k", "n", "block_bytes", "total_blocks", "sender_id", "sender_bps_limit")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    FILE_HASH_FIELD_NUMBER: _ClassVar[int]
    K_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    BLOCK_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_BPS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    filepath: str
    file_size: int
    file_hash: bytes
    k: int
    n: int
    block_bytes: int
    total_blocks: int
    sender_id: int
    sender_bps_limit: int
    def __init__(self, session_id: _Optional[str] = ..., filepath: _Optional[str] = ..., file_size: _Optional[int] = ..., file_hash: _Optional[bytes] = ..., k: _Optional[int] = ..., n: _Optional[int] = ..., block_bytes: _Optional[int] = ..., total_blocks: _Optional[int] = ..., sender_id: _Optional[int] = ..., sender_bps_limit: _Optional[int] = ...) -> None: ...

class SessionEnd(_message.Message):
    __slots__ = ("session_id", "total_blocks", "hash")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    total_blocks: int
    hash: bytes
    def __init__(self, session_id: _Optional[str] = ..., total_blocks: _Optional[int] = ..., hash: _Optional[bytes] = ...) -> None: ...
