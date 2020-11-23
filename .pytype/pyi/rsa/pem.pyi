# (generated with --quick)

from typing import Iterator, Tuple, Type, Union

FlexiText: Type[Union[bytes, str]]
base64: module
typing: module

def _markers(pem_marker: Union[bytes, str]) -> Tuple[bytes, bytes]: ...
def _pem_lines(contents: bytes, pem_start: bytes, pem_end: bytes) -> Iterator[bytes]: ...
def load_pem(contents: Union[bytes, str], pem_marker: Union[bytes, str]) -> bytes: ...
def save_pem(contents: bytes, pem_marker: Union[bytes, str]) -> bytes: ...
