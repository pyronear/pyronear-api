# (generated with --quick)

from typing import Iterable, Tuple

doctest: module
typing: module

class NotRelativePrimeError(ValueError):
    a: int
    b: int
    d: int
    def __init__(self, a: int, b: int, d: int, msg: str = ...) -> None: ...

def bit_size(num: int) -> int: ...
def byte_size(number: int) -> int: ...
def ceil_div(num: int, div: int) -> int: ...
def crt(a_values: Iterable[int], modulo_values: Iterable[int]) -> int: ...
def extended_gcd(a: int, b: int) -> Tuple[int, int, int]: ...
def inverse(x: int, n: int) -> int: ...
