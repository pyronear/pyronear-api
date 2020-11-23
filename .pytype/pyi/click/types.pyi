# (generated with --quick)

import click.exceptions
import click.utils
import typing
from typing import Any, Callable, NoReturn, Optional, Type, TypeVar
import uuid

BOOL: BoolParamType
BadParameter: Type[click.exceptions.BadParameter]
FLOAT: FloatParamType
INT: IntParamType
LazyFile: Type[click.utils.LazyFile]
PY2: bool
STRING: StringParamType
UNPROCESSED: UnprocessedParamType
UUID: UUIDParameterType
datetime: Type[datetime.datetime]
os: module
stat: module
text_type: Type[str]

_T0 = TypeVar('_T0')
_T1 = TypeVar('_T1')

class BoolParamType(ParamType):
    name: str
    def __repr__(self) -> str: ...
    def convert(self, value, param, ctx) -> Optional[bool]: ...

class Choice(ParamType):
    __doc__: str
    case_sensitive: Any
    choices: Any
    name: str
    def __init__(self, choices, case_sensitive = ...) -> None: ...
    def __repr__(self) -> str: ...
    def convert(self, value, param, ctx) -> Any: ...
    def get_metavar(self, param) -> str: ...
    def get_missing_message(self, param) -> str: ...

class CompositeParamType(ParamType):
    is_composite: bool

class DateTime(ParamType):
    __doc__: str
    formats: Any
    name: str
    def __init__(self, formats = ...) -> None: ...
    def __repr__(self) -> str: ...
    def _try_to_convert_date(self, value, format) -> Optional[datetime.datetime]: ...
    def convert(self, value, param, ctx) -> Any: ...
    def get_metavar(self, param) -> str: ...

class File(ParamType):
    __doc__: str
    atomic: Any
    encoding: Any
    envvar_list_splitter: str
    errors: Any
    lazy: Any
    mode: Any
    name: str
    def __init__(self, mode = ..., encoding = ..., errors = ..., lazy = ..., atomic = ...) -> None: ...
    def convert(self, value, param, ctx) -> Any: ...
    def resolve_lazy_flag(self, value) -> Any: ...

class FloatParamType(ParamType):
    name: str
    def __repr__(self) -> str: ...
    def convert(self, value, param, ctx) -> Optional[float]: ...

class FloatRange(FloatParamType):
    __doc__: str
    clamp: Any
    max: Any
    min: Any
    name: str
    def __init__(self, min = ..., max = ..., clamp = ...) -> None: ...
    def __repr__(self) -> str: ...
    def convert(self, value, param, ctx) -> Any: ...

class FuncParamType(ParamType):
    func: Any
    name: Any
    def __init__(self, func) -> None: ...
    def convert(self, value, param, ctx) -> Any: ...

class IntParamType(ParamType):
    name: str
    def __repr__(self) -> str: ...
    def convert(self, value, param, ctx) -> Optional[int]: ...

class IntRange(IntParamType):
    __doc__: str
    clamp: Any
    max: Any
    min: Any
    name: str
    def __init__(self, min = ..., max = ..., clamp = ...) -> None: ...
    def __repr__(self) -> str: ...
    def convert(self, value, param, ctx) -> Any: ...

class ParamType:
    __doc__: str
    envvar_list_splitter: None
    is_composite: bool
    name: None
    def __call__(self, value, param = ..., ctx = ...) -> Any: ...
    def convert(self, value: _T0, param, ctx) -> _T0: ...
    def fail(self, message, param = ..., ctx = ...) -> NoReturn: ...
    def get_metavar(self, param) -> None: ...
    def get_missing_message(self, param) -> None: ...
    def split_envvar_value(self, rv) -> Any: ...

class Path(ParamType):
    __doc__: str
    allow_dash: Any
    dir_okay: Any
    envvar_list_splitter: str
    exists: Any
    file_okay: Any
    name: str
    path_type: str
    readable: Any
    resolve_path: Any
    type: Any
    writable: Any
    def __init__(self, exists = ..., file_okay = ..., dir_okay = ..., writable = ..., readable = ..., resolve_path = ..., allow_dash = ..., path_type = ...) -> None: ...
    def coerce_path_result(self, rv) -> Any: ...
    def convert(self, value, param, ctx) -> Any: ...

class StringParamType(ParamType):
    name: str
    def __repr__(self) -> str: ...
    def convert(self, value, param, ctx) -> Any: ...

class Tuple(CompositeParamType):
    __doc__: str
    arity: int
    name: str
    types: Any
    def __init__(self, types) -> None: ...
    def convert(self, value, param, ctx) -> tuple: ...

class UUIDParameterType(ParamType):
    name: str
    def __repr__(self) -> str: ...
    def convert(self, value, param, ctx) -> Optional[uuid.UUID]: ...

class UnprocessedParamType(ParamType):
    name: str
    def __repr__(self) -> str: ...
    def convert(self, value: _T0, param, ctx) -> _T0: ...

def _get_argv_encoding() -> Any: ...
def convert_type(ty: _T0, default: _T1 = ...) -> Any: ...
def filename_to_ui(value) -> Any: ...
def get_filesystem_encoding() -> str: ...
def get_streerror(e, default = ...) -> Any: ...
def open_stream(filename, mode = ..., encoding = ..., errors = ..., atomic = ...) -> typing.Tuple[Any, bool]: ...
def safecall(func) -> Callable: ...
