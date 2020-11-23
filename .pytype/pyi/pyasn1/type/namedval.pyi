# (generated with --quick)

from typing import Any, Generator, Iterator, List, Tuple, TypeVar

__all__: List[str]
error: module

_TNamedValues = TypeVar('_TNamedValues', bound=NamedValues)

class NamedValues:
    _NamedValues__names: dict
    _NamedValues__numbers: dict
    __doc__: str
    def __add__(self: _TNamedValues, namedValues) -> _TNamedValues: ...
    def __contains__(self, key) -> bool: ...
    def __eq__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __getitem__(self, key) -> Any: ...
    def __gt__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __le__(self, other) -> bool: ...
    def __len__(self) -> int: ...
    def __lt__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __repr__(self) -> str: ...
    def clone(self, *args, **kwargs) -> Any: ...
    def getName(self, value) -> Any: ...
    def getValue(self, name) -> Any: ...
    def getValues(self, *names) -> Any: ...
    def items(self) -> Generator[Tuple[Any, Any], Any, None]: ...
    def keys(self) -> Iterator: ...
    def values(self) -> Iterator: ...
