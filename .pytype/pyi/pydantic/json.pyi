# (generated with --quick)

import decimal
import enum
import ipaddress
import pathlib
import pydantic.color
import pydantic.types
import types
from typing import Any, Callable, Dict, Tuple, Type, Union
import uuid

Color: Type[pydantic.color.Color]
Decimal: Type[decimal.Decimal]
ENCODERS_BY_TYPE: Dict[type, Callable[[Any], Any]]
Enum: Type[enum.Enum]
GeneratorType: Type[types.GeneratorType]
IPv4Address: Type[ipaddress.IPv4Address]
IPv4Interface: Type[ipaddress.IPv4Interface]
IPv4Network: Type[ipaddress.IPv4Network]
IPv6Address: Type[ipaddress.IPv6Address]
IPv6Interface: Type[ipaddress.IPv6Interface]
IPv6Network: Type[ipaddress.IPv6Network]
Path: Type[pathlib.Path]
SecretBytes: Type[pydantic.types.SecretBytes]
SecretStr: Type[pydantic.types.SecretStr]
UUID: Type[uuid.UUID]
__all__: Tuple[str, str, str]
datetime: module

def custom_pydantic_encoder(type_encoders: Dict[Any, Callable[[type], Any]], obj) -> Any: ...
def isoformat(o: Union[datetime.date, datetime.time]) -> str: ...
def pydantic_encoder(obj) -> Any: ...
def timedelta_isoformat(td: datetime.timedelta) -> str: ...
