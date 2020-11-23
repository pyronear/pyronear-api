# (generated with --quick)

import decimal
import enum
import pathlib
from typing import Any, Callable, Dict, Iterable, List, Optional, Pattern, Set, Type, TypeVar, Union
import uuid

ModelOrDc = type

BYTE_SIZES: Dict[str, int]
BaseConfig: Any
BaseModel: Any
CallableGenerator: Any
DataclassType: Any
Decimal: Type[decimal.Decimal]
Enum: Type[enum.Enum]
ModelField: Any
NoneBytes: Type[Optional[bytes]]
NoneStr: Type[Optional[str]]
NoneStrBytes: Type[Optional[Union[bytes, str]]]
OptionalInt: Type[Optional[int]]
OptionalIntFloat: Type[Optional[Union[float, int]]]
OptionalIntFloatDecimal: Type[Optional[Union[float, int, decimal.Decimal]]]
Path: Type[pathlib.Path]
StrBytes: Type[Union[bytes, str]]
StrIntFloat: Type[Union[float, int, str]]
StrictBool: Type[bool]
UUID: Type[uuid.UUID]
__all__: List[str]
byte_string_re: Pattern[str]
errors: module
math: module
re: module
warnings: module

T = TypeVar('T')

class ByteSize(int):
    @classmethod
    def __get_validators__(cls) -> Any: ...
    def human_readable(self, decimal: bool = ...) -> str: ...
    def to(self, unit: str) -> float: ...
    @classmethod
    def validate(cls, v: Union[float, str]) -> ByteSize: ...

class ConstrainedBytes(bytes):
    max_length: Optional[int]
    min_length: Optional[int]
    strip_whitespace: bool
    @classmethod
    def __get_validators__(cls) -> Any: ...
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...

class ConstrainedDecimal(decimal.Decimal, metaclass=ConstrainedNumberMeta):
    decimal_places: Optional[int]
    ge: Optional[Union[float, int, decimal.Decimal]]
    gt: Optional[Union[float, int, decimal.Decimal]]
    le: Optional[Union[float, int, decimal.Decimal]]
    lt: Optional[Union[float, int, decimal.Decimal]]
    max_digits: Optional[int]
    multiple_of: Optional[Union[float, int, decimal.Decimal]]
    @classmethod
    def __get_validators__(cls) -> Any: ...
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def validate(cls, value: decimal.Decimal) -> decimal.Decimal: ...

class ConstrainedFloat(float, metaclass=ConstrainedNumberMeta):
    ge: Optional[Union[float, int]]
    gt: Optional[Union[float, int]]
    le: Optional[Union[float, int]]
    lt: Optional[Union[float, int]]
    multiple_of: Optional[Union[float, int]]
    strict: bool
    @classmethod
    def __get_validators__(cls) -> Any: ...
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...

class ConstrainedInt(int, metaclass=ConstrainedNumberMeta):
    ge: Optional[int]
    gt: Optional[int]
    le: Optional[int]
    lt: Optional[int]
    multiple_of: Optional[int]
    strict: bool
    @classmethod
    def __get_validators__(cls) -> Any: ...
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...

class ConstrainedList(list):
    __args__: Any
    __origin__: Type[list]
    item_type: Any
    max_items: Optional[int]
    min_items: Optional[int]
    @classmethod
    def __get_validators__(cls) -> Any: ...
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def list_length_validator(cls, v: Optional[List[T]], field) -> Optional[List[T]]: ...

class ConstrainedNumberMeta(type):
    def __new__(cls, name: str, bases, dct: Dict[str, Any]) -> ConstrainedInt: ...

class ConstrainedSet(set):
    __args__: Any
    __origin__: Type[set]
    item_type: Any
    max_items: Optional[int]
    min_items: Optional[int]
    @classmethod
    def __get_validators__(cls) -> Any: ...
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def set_length_validator(cls, v: Optional[Set[T]], field) -> Optional[Set[T]]: ...

class ConstrainedStr(str):
    curtail_length: Optional[int]
    max_length: Optional[int]
    min_length: Optional[int]
    regex: Optional[Pattern[str]]
    strict: bool
    strip_whitespace: bool
    @classmethod
    def __get_validators__(cls) -> Any: ...
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def validate(cls, value: str) -> str: ...

class DirectoryPath(pathlib.Path):
    @classmethod
    def __get_validators__(cls) -> Any: ...
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def validate(cls, value: pathlib.Path) -> pathlib.Path: ...

class FilePath(pathlib.Path):
    @classmethod
    def __get_validators__(cls) -> Any: ...
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def validate(cls, value: pathlib.Path) -> pathlib.Path: ...

class Json(metaclass=JsonMeta):
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...

class JsonMeta(type):
    def __getitem__(self, t: type) -> Type[JsonWrapper]: ...

class JsonWrapper: ...

class NegativeFloat(ConstrainedFloat):
    lt: int

class NegativeInt(ConstrainedInt):
    lt: int

class PaymentCardBrand(str, enum.Enum):
    amex: str
    mastercard: str
    other: str
    visa: str
    def __str__(self) -> str: ...

class PaymentCardNumber(str):
    __doc__: str
    bin: str
    brand: Any
    last4: str
    masked: str
    max_length: int
    min_length: int
    strip_whitespace: bool
    @classmethod
    def __get_validators__(cls) -> Any: ...
    def __init__(self, card_number: str) -> None: ...
    @staticmethod
    def _get_brand(card_number: str) -> PaymentCardBrand: ...
    @classmethod
    def validate_digits(cls, card_number: str) -> str: ...
    @classmethod
    def validate_length_for_brand(cls, card_number: PaymentCardNumber) -> PaymentCardNumber: ...
    @classmethod
    def validate_luhn_check_digit(cls, card_number: str) -> str: ...

class PositiveFloat(ConstrainedFloat):
    gt: int

class PositiveInt(ConstrainedInt):
    gt: int

class PyObject:
    validate_always: bool
    @classmethod
    def __get_validators__(cls) -> Any: ...
    @classmethod
    def validate(cls, value) -> Any: ...

class SecretBytes:
    _secret_value: bytes
    def __eq__(self, other) -> bool: ...
    @classmethod
    def __get_validators__(cls) -> Any: ...
    def __init__(self, value: bytes) -> None: ...
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def display(self) -> str: ...
    def get_secret_value(self) -> bytes: ...
    @classmethod
    def validate(cls, value) -> SecretBytes: ...

class SecretStr:
    _secret_value: str
    def __eq__(self, other) -> bool: ...
    @classmethod
    def __get_validators__(cls) -> Any: ...
    def __init__(self, value: str) -> None: ...
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def display(self) -> str: ...
    def get_secret_value(self) -> str: ...
    @classmethod
    def validate(cls, value) -> SecretStr: ...

class StrictFloat(ConstrainedFloat):
    strict: bool

class StrictInt(ConstrainedInt):
    strict: bool

class StrictStr(ConstrainedStr):
    strict: bool

class UUID1(uuid.UUID):
    _required_version: int
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...

class UUID3(UUID1):
    _required_version: int

class UUID4(UUID1):
    _required_version: int

class UUID5(UUID1):
    _required_version: int

def bytes_validator(v) -> bytes: ...
def conbytes(*, strip_whitespace: bool = ..., min_length: int = ..., max_length: int = ...) -> Type[bytes]: ...
def condecimal(*, gt: decimal.Decimal = ..., ge: decimal.Decimal = ..., lt: decimal.Decimal = ..., le: decimal.Decimal = ..., max_digits: int = ..., decimal_places: int = ..., multiple_of: decimal.Decimal = ...) -> Type[decimal.Decimal]: ...
def confloat(*, strict: bool = ..., gt: float = ..., ge: float = ..., lt: float = ..., le: float = ..., multiple_of: float = ...) -> Type[float]: ...
def conint(*, strict: bool = ..., gt: int = ..., ge: int = ..., lt: int = ..., le: int = ..., multiple_of: int = ...) -> Type[int]: ...
def conlist(item_type: Type[T], *, min_items: int = ..., max_items: int = ...) -> Type[List[T]]: ...
def conset(item_type: Type[T], *, min_items: int = ..., max_items: int = ...) -> Type[Set[T]]: ...
def constr(*, strip_whitespace: bool = ..., strict: bool = ..., min_length: int = ..., max_length: int = ..., curtail_length: int = ..., regex: str = ...) -> Type[str]: ...
def constr_length_validator(v: Union[bytes, str], field, config) -> Union[bytes, str]: ...
def constr_strip_whitespace(v: Union[bytes, str], field, config) -> Union[bytes, str]: ...
def decimal_validator(v) -> decimal.Decimal: ...
def float_validator(v) -> float: ...
def import_string(dotted_path: str) -> Any: ...
def int_validator(v) -> int: ...
def list_validator(v) -> list: ...
def new_class(name: str, bases: Iterable[object] = ..., kwds: Dict[str, Any] = ..., exec_body: Callable[[Dict[str, Any]], None] = ...) -> type: ...
def number_multiple_validator(v: Union[float, decimal.Decimal], field) -> Union[float, int, decimal.Decimal]: ...
def number_size_validator(v: Union[float, decimal.Decimal], field) -> Union[float, int, decimal.Decimal]: ...
def path_exists_validator(v) -> pathlib.Path: ...
def path_validator(v) -> pathlib.Path: ...
def set_validator(v) -> set: ...
def str_validator(v) -> str: ...
def strict_float_validator(v) -> float: ...
def strict_int_validator(v) -> int: ...
def strict_str_validator(v) -> str: ...
def update_not_none(mapping: dict, **update) -> None: ...
