# (generated with --quick)

import asyncio.locks
import contextvars
import databases.interfaces
import types
from typing import Any, AsyncGenerator, Callable, Coroutine, Dict, List, Mapping, Optional, Tuple, Type, TypeVar, Union
import urllib.parse

CONNECT_EXTRA: Dict[str, str]
ClauseElement: Any
ConnectionBackend: Type[databases.interfaces.ConnectionBackend]
ContextVar: Type[contextvars.ContextVar]
DISCONNECT_EXTRA: Dict[str, str]
DatabaseBackend: Type[databases.interfaces.DatabaseBackend]
LOG_EXTRA: Dict[str, str]
SplitResult: Type[urllib.parse.SplitResult]
TracebackType: Type[types.TracebackType]
TransactionBackend: Type[databases.interfaces.TransactionBackend]
asyncio: module
click: module
contextlib: module
functools: module
logger: logging.Logger
logging: module
sys: module
text: Any
typing: module

AnyStr = TypeVar('AnyStr', str, bytes)
_TDatabaseURL = TypeVar('_TDatabaseURL', bound=DatabaseURL)

class Connection:
    _backend: databases.interfaces.DatabaseBackend
    _connection: databases.interfaces.ConnectionBackend
    _connection_counter: int
    _connection_lock: asyncio.locks.Lock
    _query_lock: asyncio.locks.Lock
    _transaction_lock: asyncio.locks.Lock
    _transaction_stack: List[Transaction]
    raw_connection: Any
    def __aenter__(self) -> Coroutine[Any, Any, Connection]: ...
    def __aexit__(self, exc_type: Type[BaseException] = ..., exc_value: BaseException = ..., traceback: types.TracebackType = ...) -> Coroutine[Any, Any, None]: ...
    def __init__(self, backend: databases.interfaces.DatabaseBackend) -> None: ...
    @staticmethod
    def _build_query(query, values: dict = ...) -> Any: ...
    def execute(self, query, values: dict = ...) -> coroutine: ...
    def execute_many(self, query, values: list) -> Coroutine[Any, Any, None]: ...
    def fetch_all(self, query, values: dict = ...) -> Coroutine[Any, Any, List[Mapping]]: ...
    def fetch_one(self, query, values: dict = ...) -> Coroutine[Any, Any, Optional[Mapping]]: ...
    def fetch_val(self, query, values: dict = ..., column = ...) -> coroutine: ...
    def iterate(self, query, values: dict = ...) -> AsyncGenerator[Any, None]: ...
    def transaction(self, *, force_rollback: bool = ...) -> Transaction: ...

class Database:
    SUPPORTED_BACKENDS: Dict[str, str]
    _backend: Any
    _connection_context: contextvars.ContextVar
    _force_rollback: bool
    _global_connection: Optional[Connection]
    _global_transaction: Optional[Transaction]
    force_rollback: Callable[..., contextlib._GeneratorContextManager[None]]
    is_connected: bool
    options: Dict[str, Any]
    url: DatabaseURL
    def __aenter__(self) -> Coroutine[Any, Any, Database]: ...
    def __aexit__(self, exc_type: Type[BaseException] = ..., exc_value: BaseException = ..., traceback: types.TracebackType = ...) -> Coroutine[Any, Any, None]: ...
    def __init__(self, url: Union[DatabaseURL, str], *, force_rollback: bool = ..., **options) -> None: ...
    def connect(self) -> Coroutine[Any, Any, None]: ...
    def connection(self) -> Connection: ...
    def disconnect(self) -> Coroutine[Any, Any, None]: ...
    def execute(self, query, values: dict = ...) -> coroutine: ...
    def execute_many(self, query, values: list) -> Coroutine[Any, Any, None]: ...
    def fetch_all(self, query, values: dict = ...) -> Coroutine[Any, Any, List[Mapping]]: ...
    def fetch_one(self, query, values: dict = ...) -> Coroutine[Any, Any, Optional[Mapping]]: ...
    def fetch_val(self, query, values: dict = ..., column = ...) -> coroutine: ...
    def iterate(self, query, values: dict = ...) -> AsyncGenerator[Mapping, None]: ...
    def transaction(self, *, force_rollback: bool = ...) -> Transaction: ...

class DatabaseURL:
    _url: str
    components: urllib.parse.SplitResult
    database: str
    dialect: str
    driver: str
    hostname: Optional[str]
    netloc: Optional[str]
    obscure_password: str
    options: dict
    password: Optional[str]
    port: Optional[int]
    scheme: str
    username: Optional[str]
    def __eq__(self, other) -> bool: ...
    def __init__(self, url: Union[DatabaseURL, str]) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def replace(self: _TDatabaseURL, **kwargs) -> _TDatabaseURL: ...

class Transaction:
    _connection_callable: Callable[[], Connection]
    _force_rollback: bool
    def __aenter__(self) -> Coroutine[Any, Any, Transaction]: ...
    def __aexit__(self, exc_type: Type[BaseException] = ..., exc_value: BaseException = ..., traceback: types.TracebackType = ...) -> Coroutine[Any, Any, None]: ...
    def __await__(self) -> generator: ...
    def __call__(self, func: Callable) -> Callable: ...
    def __init__(self, connection_callable: Callable[[], Connection], force_rollback: bool) -> None: ...
    def commit(self) -> Coroutine[Any, Any, None]: ...
    def rollback(self) -> Coroutine[Any, Any, None]: ...
    def start(self) -> Coroutine[Any, Any, Transaction]: ...

class _EmptyNetloc(str):
    def __bool__(self) -> bool: ...

def import_from_string(import_str: str) -> Any: ...
def parse_qsl(qs: Optional[AnyStr], keep_blank_values: bool = ..., strict_parsing: bool = ..., encoding: str = ..., errors: str = ..., max_num_fields: Optional[int] = ...) -> List[Tuple[AnyStr, AnyStr]]: ...
@overload
def urlsplit(url: str, scheme: Optional[str] = ..., allow_fragments: bool = ...) -> urllib.parse.SplitResult: ...
@overload
def urlsplit(url: Optional[bytes], scheme: Optional[bytes] = ..., allow_fragments: bool = ...) -> urllib.parse.SplitResultBytes: ...
