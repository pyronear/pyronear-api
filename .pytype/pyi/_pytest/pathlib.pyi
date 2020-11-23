# (generated with --quick)

import _pytest.outcomes
import _pytest.warning_types
import enum
import functools
import pathlib
from typing import Any, Callable, Iterable, Iterator, List, NoReturn, Optional, Set, Type, TypeVar, Union

Enum: Type[enum.Enum]
LOCK_TIMEOUT: int
ModuleType: Type[module]
Path: Type[pathlib.Path]
PurePath: Type[pathlib.PurePath]
PytestWarning: Type[_pytest.warning_types.PytestWarning]
__all__: List[str]
atexit: module
contextlib: module
fnmatch: module
importlib: module
itertools: module
os: module
partial: Type[functools.partial]
posix_sep: str
py: module
sep: str
shutil: module
skip: _pytest.outcomes._WithException[Callable, Type[_pytest.outcomes.Skipped]]
sys: module
uuid: module
warnings: module

AnyStr = TypeVar('AnyStr', str, bytes)
_AnyPurePath = TypeVar('_AnyPurePath', bound=pathlib.PurePath)

class ImportMode(enum.Enum):
    __doc__: str
    append: str
    importlib: str
    prepend: str

class ImportPathMismatchError(ImportError):
    __doc__: str

def _force_symlink(root: pathlib.Path, target: Union[str, pathlib.PurePath], link_to: Union[str, pathlib.Path]) -> None: ...
def absolutepath(path: Union[str, pathlib.Path]) -> pathlib.Path: ...
def assert_never(value) -> NoReturn: ...
def bestrelpath(directory: pathlib.Path, dest: pathlib.Path) -> str: ...
def cleanup_candidates(root: pathlib.Path, prefix: str, keep: int) -> Iterator[pathlib.Path]: ...
def cleanup_numbered_dir(root: pathlib.Path, prefix: str, keep: int, consider_lock_dead_if_created_before: float) -> None: ...
def commonpath(path1: pathlib.Path, path2: pathlib.Path) -> Optional[pathlib.Path]: ...
def create_cleanup_lock(p: pathlib.Path) -> pathlib.Path: ...
def ensure_deletable(path: pathlib.Path, consider_lock_dead_if_created_before: float) -> bool: ...
def ensure_extended_length_path(path: pathlib.Path) -> pathlib.Path: ...
def ensure_reset_dir(path: pathlib.Path) -> None: ...
def expanduser(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def expandvars(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def extract_suffixes(iter: Iterable[pathlib.PurePath], prefix: str) -> Iterator[str]: ...
def find_prefixed(root: pathlib.Path, prefix: str) -> Iterator[pathlib.Path]: ...
def find_suffixes(root: pathlib.Path, prefix: str) -> Iterator[str]: ...
def fnmatch_ex(pattern: str, path) -> bool: ...
def get_extended_length_path_str(path: str) -> str: ...
def get_lock_path(path: _AnyPurePath) -> _AnyPurePath: ...
def import_path(p, *, mode: Union[ImportMode, str] = ...) -> module: ...
def isabs(s: Union[_PathLike, bytes, str]) -> bool: ...
def make_numbered_dir(root: pathlib.Path, prefix: str) -> pathlib.Path: ...
def make_numbered_dir_with_cleanup(root: pathlib.Path, prefix: str, keep: int, lock_timeout: float) -> pathlib.Path: ...
def maybe_delete_a_numbered_dir(path: pathlib.Path) -> None: ...
def on_rm_rf_error(func, path: str, exc, *, start_path: pathlib.Path) -> bool: ...
def parse_num(maybe_num) -> int: ...
def parts(s: str) -> Set[str]: ...
def register_cleanup_lock_removal(lock_path: pathlib.Path, register = ...) -> Any: ...
def resolve_from_str(input: str, rootpath: pathlib.Path) -> pathlib.Path: ...
def resolve_package_path(path: pathlib.Path) -> Optional[pathlib.Path]: ...
def rm_rf(path: pathlib.Path) -> None: ...
def symlink_or_skip(src, dst, **kwargs) -> None: ...
def try_cleanup(path: pathlib.Path, consider_lock_dead_if_created_before: float) -> None: ...
def visit(path: str, recurse: Callable[[os.DirEntry[str]], bool]) -> Iterator[os.DirEntry[str]]: ...
