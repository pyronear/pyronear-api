# (generated with --quick)

from typing import Any, TypeVar, Union

PY2: bool

_T0 = TypeVar('_T0')

class Abort(RuntimeError):
    __doc__: str

class BadArgumentUsage(UsageError):
    __doc__: str
    cmd: Any
    ctx: Any
    message: Any
    def __init__(self, message, ctx = ...) -> None: ...

class BadOptionUsage(UsageError):
    __doc__: str
    cmd: Any
    ctx: Any
    message: Any
    option_name: Any
    def __init__(self, option_name, message, ctx = ...) -> None: ...

class BadParameter(UsageError):
    __doc__: str
    cmd: Any
    ctx: Any
    message: Any
    param: Any
    param_hint: Any
    def __init__(self, message, ctx = ..., param = ..., param_hint = ...) -> None: ...
    def format_message(self) -> str: ...

class ClickException(Exception):
    __doc__: str
    exit_code: int
    message: Any
    def __init__(self, message) -> None: ...
    def __str__(self) -> Any: ...
    def __unicode__(self) -> Any: ...
    def format_message(self) -> Any: ...
    def show(self, file = ...) -> None: ...

class Exit(RuntimeError):
    __slots__ = ["exit_code"]
    __doc__: str
    exit_code: Any
    def __init__(self, code = ...) -> None: ...

class FileError(ClickException):
    __doc__: str
    filename: Any
    message: Any
    ui_filename: Any
    def __init__(self, filename, hint = ...) -> None: ...
    def format_message(self) -> str: ...

class MissingParameter(BadParameter):
    __doc__: str
    cmd: Any
    ctx: Any
    message: Any
    param: Any
    param_hint: Any
    param_type: Any
    def __init__(self, message = ..., ctx = ..., param = ..., param_hint = ..., param_type = ...) -> None: ...
    def __str__(self) -> Any: ...
    def __unicode__(self) -> Any: ...
    def format_message(self) -> str: ...

class NoSuchOption(UsageError):
    __doc__: str
    cmd: Any
    ctx: Any
    message: Any
    option_name: Any
    possibilities: Any
    def __init__(self, option_name, message = ..., possibilities = ..., ctx = ...) -> None: ...
    def format_message(self) -> str: ...

class UsageError(ClickException):
    __doc__: str
    cmd: Any
    ctx: Any
    exit_code: int
    message: Any
    def __init__(self, message, ctx = ...) -> None: ...
    def show(self, file = ...) -> None: ...

def _join_param_hints(param_hint: _T0) -> Union[str, _T0]: ...
def echo(message = ..., file = ..., nl = ..., err = ..., color = ...) -> None: ...
def filename_to_ui(value) -> Any: ...
def get_text_stderr(encoding = ..., errors = ...) -> Any: ...
