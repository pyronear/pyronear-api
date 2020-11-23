# (generated with --quick)

import pyasn1.type.base
import pyasn1.type.constraint
import pyasn1.type.namedtype
import pyasn1.type.namedval
import pyasn1.type.tag
import typing
from typing import Generator, Iterator, List, Optional, Tuple, Type, TypeVar, Union

NoValue: Type[pyasn1.type.base.NoValue]
SizedIntegerBase: Type[int]
__all__: List[str]
base: module
binary: module
constraint: module
eoo: module
error: module
intTypes: Tuple[Type[int]]
integer: module
math: module
namedtype: module
namedval: module
noValue: pyasn1.type.base.NoValue
numericTypes: Tuple[Type[Union[float, int]], ...]
octets: module
sys: module
tag: module
tagmap: module

_T0 = TypeVar('_T0')
_TBitString = TypeVar('_TBitString', bound=BitString)
_TChoice = TypeVar('_TChoice', bound=Choice)
_TInteger = TypeVar('_TInteger', bound=Integer)
_TObjectIdentifier = TypeVar('_TObjectIdentifier', bound=ObjectIdentifier)
_TOctetString = TypeVar('_TOctetString', bound=OctetString)
_TReal = TypeVar('_TReal', bound=Real)
_TSequenceAndSetBase = TypeVar('_TSequenceAndSetBase', bound=SequenceAndSetBase)
_TSequenceOfAndSetOfBase = TypeVar('_TSequenceOfAndSetOfBase', bound=SequenceOfAndSetOfBase)
_TSet = TypeVar('_TSet', bound=Set)
_TSizedInteger = TypeVar('_TSizedInteger', bound=SizedInteger)

class Any(OctetString):
    __doc__: str
    subtypeSpec: pyasn1.type.constraint.ConstraintsIntersection
    tagMap: typing.Any
    tagSet: pyasn1.type.tag.TagSet
    typeId: typing.Any

class BitString(pyasn1.type.base.SimpleAsn1Type):
    __doc__: str
    defaultBinValue: pyasn1.type.base.NoValue
    defaultHexValue: pyasn1.type.base.NoValue
    namedValues: pyasn1.type.namedval.NamedValues
    subtypeSpec: pyasn1.type.constraint.ConstraintsIntersection
    tagSet: pyasn1.type.tag.TagSet
    typeId: typing.Any
    def __add__(self: _TBitString, value: typing.Any) -> _TBitString: ...
    def __eq__(self, other: typing.Any) -> typing.Any: ...
    def __float__(self) -> float: ...
    def __ge__(self, other: typing.Any) -> typing.Any: ...
    def __getitem__(self, i: typing.Any) -> typing.Any: ...
    def __gt__(self, other: typing.Any) -> typing.Any: ...
    def __init__(self, value: typing.Any = ..., **kwargs) -> None: ...
    def __int__(self) -> typing.Any: ...
    def __iter__(self) -> Generator[typing.Any, typing.Any, None]: ...
    def __le__(self, other: typing.Any) -> typing.Any: ...
    def __len__(self) -> int: ...
    def __lshift__(self: _TBitString, count: typing.Any) -> _TBitString: ...
    def __lt__(self, other: typing.Any) -> typing.Any: ...
    def __mul__(self: _TBitString, value: typing.Any) -> _TBitString: ...
    def __ne__(self, other: typing.Any) -> typing.Any: ...
    def __radd__(self: _TBitString, value: typing.Any) -> _TBitString: ...
    def __reversed__(self) -> reversed: ...
    def __rmul__(self, value: typing.Any) -> typing.Any: ...
    def __rshift__(self: _TBitString, count: typing.Any) -> _TBitString: ...
    def __str__(self) -> typing.Any: ...
    def asBinary(self) -> str: ...
    def asInteger(self) -> typing.Any: ...
    def asNumbers(self) -> tuple: ...
    def asOctets(self) -> typing.Any: ...
    @classmethod
    def fromBinaryString(cls, value: typing.Any, internalFormat: typing.Any = ..., prepend: typing.Any = ...) -> typing.Any: ...
    @classmethod
    def fromHexString(cls, value: typing.Any, internalFormat: typing.Any = ..., prepend: typing.Any = ...) -> typing.Any: ...
    @classmethod
    def fromOctetString(cls, value: typing.Any, internalFormat: typing.Any = ..., prepend: typing.Any = ..., padding: typing.Any = ...) -> typing.Any: ...
    def prettyIn(self, value: typing.Any) -> typing.Any: ...

class Boolean(Integer):
    __doc__: str
    namedValues: pyasn1.type.namedval.NamedValues
    subtypeSpec: pyasn1.type.constraint.ConstraintsIntersection
    tagSet: pyasn1.type.tag.TagSet
    typeId: typing.Any

class Choice(Set):
    __doc__: str
    _componentTypeLen: int
    _componentValues: Union[list, pyasn1.type.base.NoValue]
    _currentIdx: typing.Any
    _dynamicNames: typing.Any
    componentType: pyasn1.type.namedtype.NamedTypes
    effectiveTagSet: typing.Any
    isValue: typing.Any
    subtypeSpec: pyasn1.type.constraint.ConstraintsIntersection
    tagMap: typing.Any
    tagSet: pyasn1.type.tag.TagSet
    typeId: typing.Any
    def __bool__(self) -> bool: ...
    def __contains__(self, key: typing.Any) -> typing.Any: ...
    def __eq__(self, other: typing.Any) -> typing.Any: ...
    def __ge__(self, other: typing.Any) -> typing.Any: ...
    def __gt__(self, other: typing.Any) -> typing.Any: ...
    def __iter__(self) -> Generator[typing.Any, typing.Any, None]: ...
    def __le__(self, other: typing.Any) -> typing.Any: ...
    def __len__(self) -> int: ...
    def __lt__(self, other: typing.Any) -> typing.Any: ...
    def __ne__(self, other: typing.Any) -> typing.Any: ...
    def _cloneComponentValues(self, myClone: typing.Any, cloneValueFlag: typing.Any) -> None: ...
    def checkConsistency(self) -> None: ...
    def clear(self) -> typing.Any: ...
    def getComponent(self, innerFlag: typing.Any = ...) -> typing.Any: ...
    def getComponentByPosition(self, idx: typing.Any, default: typing.Any = ..., instantiate: typing.Any = ...) -> typing.Any: ...
    def getMinTagSet(self) -> typing.Any: ...
    def getName(self, innerFlag: typing.Any = ...) -> typing.Any: ...
    def items(self) -> Generator[Tuple[typing.Any, typing.Any], typing.Any, None]: ...
    def keys(self) -> Generator[typing.Any, typing.Any, None]: ...
    def setComponentByPosition(self: _TChoice, idx: typing.Any, value: typing.Any = ..., verifyConstraints: typing.Any = ..., matchTags: typing.Any = ..., matchConstraints: typing.Any = ...) -> _TChoice: ...
    def values(self) -> Generator[typing.Any, typing.Any, None]: ...

class Enumerated(Integer):
    __doc__: str
    namedValues: pyasn1.type.namedval.NamedValues
    subtypeSpec: pyasn1.type.constraint.ConstraintsIntersection
    tagSet: pyasn1.type.tag.TagSet
    typeId: typing.Any

class Integer(pyasn1.type.base.SimpleAsn1Type):
    __doc__: str
    namedValues: pyasn1.type.namedval.NamedValues
    subtypeSpec: pyasn1.type.constraint.ConstraintsIntersection
    tagSet: pyasn1.type.tag.TagSet
    typeId: typing.Any
    def __abs__(self: _TInteger) -> _TInteger: ...
    def __add__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def __and__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def __ceil__(self) -> int: ...
    def __divmod__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def __eq__(self, value: typing.Any) -> typing.Any: ...
    def __float__(self) -> float: ...
    def __floor__(self) -> int: ...
    def __floordiv__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def __ge__(self, value: typing.Any) -> typing.Any: ...
    def __gt__(self, value: typing.Any) -> typing.Any: ...
    def __hash__(self: pyasn1.type.base.SimpleAsn1Type) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: typing.Any = ..., **kwargs) -> None: ...
    def __int__(self) -> int: ...
    def __invert__(self: _TInteger) -> _TInteger: ...
    def __le__(self, value: typing.Any) -> typing.Any: ...
    def __lshift__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def __lt__(self, value: typing.Any) -> typing.Any: ...
    def __mod__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def __mul__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def __ne__(self, value: typing.Any) -> typing.Any: ...
    def __neg__(self: _TInteger) -> _TInteger: ...
    def __or__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def __pos__(self: _TInteger) -> _TInteger: ...
    def __pow__(self: _TInteger, value: typing.Any, modulo: typing.Any = ...) -> _TInteger: ...
    def __radd__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def __rand__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def __rdivmod__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def __rfloordiv__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def __rmod__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def __rmul__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def __ror__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def __round__(self, n: typing.Any = ...) -> Union[Integer, float]: ...
    def __rpow__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def __rshift__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def __rsub__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def __rtruediv__(self, value: typing.Any) -> Real: ...
    def __rxor__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def __sub__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def __truediv__(self, value: typing.Any) -> Real: ...
    def __trunc__(self: _TInteger) -> _TInteger: ...
    def __xor__(self: _TInteger, value: typing.Any) -> _TInteger: ...
    def getNamedValues(self) -> pyasn1.type.namedval.NamedValues: ...
    def prettyIn(self, value: typing.Any) -> typing.Any: ...
    def prettyOut(self, value: typing.Any) -> str: ...

class Null(OctetString):
    __doc__: str
    subtypeSpec: pyasn1.type.constraint.ConstraintsIntersection
    tagSet: pyasn1.type.tag.TagSet
    typeId: typing.Any
    def prettyIn(self, value: typing.Any) -> typing.Any: ...

class ObjectIdentifier(pyasn1.type.base.SimpleAsn1Type):
    __doc__: str
    subtypeSpec: pyasn1.type.constraint.ConstraintsIntersection
    tagSet: pyasn1.type.tag.TagSet
    typeId: typing.Any
    def __add__(self: _TObjectIdentifier, other: typing.Any) -> _TObjectIdentifier: ...
    def __contains__(self, value: typing.Any) -> bool: ...
    def __getitem__(self, i: typing.Any) -> typing.Any: ...
    def __iter__(self) -> typing.Any: ...
    def __len__(self) -> int: ...
    def __radd__(self: _TObjectIdentifier, other: typing.Any) -> _TObjectIdentifier: ...
    def asTuple(self) -> typing.Any: ...
    def index(self, suboid: typing.Any) -> typing.Any: ...
    def isPrefixOf(self, other: typing.Any) -> bool: ...
    def prettyIn(self, value: typing.Any) -> tuple: ...
    def prettyOut(self, value: typing.Any) -> str: ...

class OctetString(pyasn1.type.base.SimpleAsn1Type):
    __doc__: str
    defaultBinValue: pyasn1.type.base.NoValue
    defaultHexValue: pyasn1.type.base.NoValue
    encoding: str
    subtypeSpec: pyasn1.type.constraint.ConstraintsIntersection
    tagSet: pyasn1.type.tag.TagSet
    typeId: typing.Any
    def __add__(self: _TOctetString, value: typing.Any) -> _TOctetString: ...
    def __bytes__(self) -> bytes: ...
    def __contains__(self, value: typing.Any) -> bool: ...
    def __float__(self) -> float: ...
    def __getitem__(self, i: typing.Any) -> typing.Any: ...
    def __init__(self, value: typing.Any = ..., **kwargs) -> None: ...
    def __int__(self) -> int: ...
    def __iter__(self) -> typing.Any: ...
    def __len__(self) -> int: ...
    def __mul__(self: _TOctetString, value: typing.Any) -> _TOctetString: ...
    def __radd__(self: _TOctetString, value: typing.Any) -> _TOctetString: ...
    def __reversed__(self) -> reversed: ...
    def __rmul__(self, value: typing.Any) -> typing.Any: ...
    def __str__(self) -> typing.Any: ...
    def asNumbers(self) -> tuple: ...
    def asOctets(self) -> bytes: ...
    @staticmethod
    def fromBinaryString(value: typing.Any) -> bytes: ...
    @staticmethod
    def fromHexString(value: typing.Any) -> bytes: ...
    def prettyIn(self, value: typing.Any) -> typing.Any: ...
    def prettyOut(self, value: _T0) -> _T0: ...
    def prettyPrint(self, scope: typing.Any = ...) -> typing.Any: ...

class Real(pyasn1.type.base.SimpleAsn1Type):
    __doc__: str
    _inf: Tuple[float, ...]
    _minusInf: Optional[float]
    _plusInf: Optional[float]
    binEncBase: None
    isInf: bool
    isMinusInf: typing.Any
    isPlusInf: typing.Any
    subtypeSpec: pyasn1.type.constraint.ConstraintsIntersection
    tagSet: pyasn1.type.tag.TagSet
    typeId: typing.Any
    @staticmethod
    def _Real__normalizeBase10(value: typing.Any) -> Tuple[typing.Any, typing.Any, typing.Any]: ...
    def __abs__(self: _TReal) -> _TReal: ...
    def __add__(self: _TReal, value: typing.Any) -> _TReal: ...
    def __bool__(self) -> bool: ...
    def __ceil__(self: _TReal) -> _TReal: ...
    def __divmod__(self: _TReal, value: typing.Any) -> _TReal: ...
    def __eq__(self, value: typing.Any) -> bool: ...
    def __float__(self) -> typing.Any: ...
    def __floor__(self: _TReal) -> _TReal: ...
    def __ge__(self, value: typing.Any) -> bool: ...
    def __getitem__(self, idx: typing.Any) -> typing.Any: ...
    def __gt__(self, value: typing.Any) -> bool: ...
    def __hash__(self: pyasn1.type.base.SimpleAsn1Type) -> int: ...
    def __int__(self) -> int: ...
    def __le__(self, value: typing.Any) -> bool: ...
    def __lt__(self, value: typing.Any) -> bool: ...
    def __mod__(self: _TReal, value: typing.Any) -> _TReal: ...
    def __mul__(self: _TReal, value: typing.Any) -> _TReal: ...
    def __ne__(self, value: typing.Any) -> bool: ...
    def __neg__(self: _TReal) -> _TReal: ...
    def __pos__(self: _TReal) -> _TReal: ...
    def __pow__(self: _TReal, value: typing.Any, modulo: typing.Any = ...) -> _TReal: ...
    def __radd__(self, value: typing.Any) -> typing.Any: ...
    def __rdivmod__(self: _TReal, value: typing.Any) -> _TReal: ...
    def __rmod__(self: _TReal, value: typing.Any) -> _TReal: ...
    def __rmul__(self, value: typing.Any) -> typing.Any: ...
    def __round__(self, n: typing.Any = ...) -> Union[Real, float]: ...
    def __rpow__(self: _TReal, value: typing.Any) -> _TReal: ...
    def __rsub__(self: _TReal, value: typing.Any) -> _TReal: ...
    def __rtruediv__(self: _TReal, value: typing.Any) -> _TReal: ...
    def __sub__(self: _TReal, value: typing.Any) -> _TReal: ...
    def __truediv__(self: _TReal, value: typing.Any) -> _TReal: ...
    def __trunc__(self: _TReal) -> _TReal: ...
    def isInfinity(self) -> typing.Any: ...
    def isMinusInfinity(self) -> typing.Any: ...
    def isPlusInfinity(self) -> typing.Any: ...
    def prettyIn(self, value: typing.Any) -> typing.Any: ...
    def prettyPrint(self, scope: typing.Any = ...) -> str: ...

class Sequence(SequenceAndSetBase):
    __doc__: str
    _componentTypeLen: int
    _componentValues: Union[pyasn1.type.base.NoValue, List[nothing]]
    _dynamicNames: typing.Any
    componentType: pyasn1.type.namedtype.NamedTypes
    subtypeSpec: pyasn1.type.constraint.ConstraintsIntersection
    tagSet: pyasn1.type.tag.TagSet
    typeId: typing.Any
    def getComponentPositionNearType(self, tagSet: typing.Any, idx: typing.Any) -> typing.Any: ...
    def getComponentTagMapNearPosition(self, idx: typing.Any) -> typing.Any: ...

class SequenceAndSetBase(pyasn1.type.base.ConstructedAsn1Type):
    DynamicNames: type
    __doc__: str
    _componentTypeLen: int
    _componentValues: Union[list, pyasn1.type.base.NoValue]
    _dynamicNames: typing.Any
    componentType: pyasn1.type.namedtype.NamedTypes
    components: typing.Any
    isInconsistent: Optional[Union[BaseException, bool]]
    isValue: bool
    def __contains__(self, key: typing.Any) -> bool: ...
    def __getitem__(self, idx: typing.Any) -> typing.Any: ...
    def __init__(self, **kwargs) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def __setitem__(self, idx: typing.Any, value: typing.Any) -> None: ...
    def _cloneComponentValues(self, myClone: typing.Any, cloneValueFlag: typing.Any) -> None: ...
    def clear(self: _TSequenceAndSetBase) -> _TSequenceAndSetBase: ...
    def getComponentByName(self, name: typing.Any, default: typing.Any = ..., instantiate: typing.Any = ...) -> typing.Any: ...
    def getComponentByPosition(self, idx: typing.Any, default: typing.Any = ..., instantiate: typing.Any = ...) -> typing.Any: ...
    def getComponentType(self) -> Optional[pyasn1.type.namedtype.NamedTypes]: ...
    def getNameByPosition(self, idx: typing.Any) -> typing.Any: ...
    def items(self) -> Generator[Tuple[typing.Any, typing.Any], typing.Any, None]: ...
    def keys(self) -> Iterator: ...
    def prettyPrint(self, scope: typing.Any = ...) -> str: ...
    def prettyPrintType(self, scope: typing.Any = ...) -> str: ...
    def reset(self: _TSequenceAndSetBase) -> _TSequenceAndSetBase: ...
    def setComponentByName(self, name: typing.Any, value: typing.Any = ..., verifyConstraints: typing.Any = ..., matchTags: typing.Any = ..., matchConstraints: typing.Any = ...) -> typing.Any: ...
    def setComponentByPosition(self: _TSequenceAndSetBase, idx: typing.Any, value: typing.Any = ..., verifyConstraints: typing.Any = ..., matchTags: typing.Any = ..., matchConstraints: typing.Any = ...) -> _TSequenceAndSetBase: ...
    def setDefaultComponents(self: _TSequenceAndSetBase) -> _TSequenceAndSetBase: ...
    def update(self, *iterValue, **mappingValue) -> None: ...
    def values(self) -> Generator[typing.Any, typing.Any, None]: ...

class SequenceOf(SequenceOfAndSetOfBase):
    __doc__: str
    _componentValues: pyasn1.type.base.NoValue
    componentType: None
    subtypeSpec: pyasn1.type.constraint.ConstraintsIntersection
    tagSet: pyasn1.type.tag.TagSet
    typeId: typing.Any

class SequenceOfAndSetOfBase(pyasn1.type.base.ConstructedAsn1Type):
    __doc__: str
    _componentValues: Union[dict, pyasn1.type.base.NoValue]
    componentTagMap: typing.Any
    components: typing.Any
    isInconsistent: Optional[Union[BaseException, bool]]
    isValue: bool
    def __getitem__(self, idx: typing.Any) -> typing.Any: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __iter__(self) -> Generator[typing.Any, typing.Any, None]: ...
    def __len__(self) -> typing.Any: ...
    def __setitem__(self, idx: typing.Any, value: typing.Any) -> None: ...
    def _cloneComponentValues(self, myClone: typing.Any, cloneValueFlag: typing.Any) -> None: ...
    def append(self, value: typing.Any) -> None: ...
    def clear(self: _TSequenceOfAndSetOfBase) -> _TSequenceOfAndSetOfBase: ...
    def count(self, value: typing.Any) -> int: ...
    def extend(self, values: typing.Any) -> None: ...
    def getComponentByPosition(self, idx: typing.Any, default: typing.Any = ..., instantiate: typing.Any = ...) -> typing.Any: ...
    def index(self, value: typing.Any, start: typing.Any = ..., stop: typing.Any = ...) -> typing.Any: ...
    def prettyPrint(self, scope: typing.Any = ...) -> str: ...
    def prettyPrintType(self, scope: typing.Any = ...) -> str: ...
    def reset(self: _TSequenceOfAndSetOfBase) -> _TSequenceOfAndSetOfBase: ...
    def reverse(self) -> None: ...
    def setComponentByPosition(self: _TSequenceOfAndSetOfBase, idx: typing.Any, value: typing.Any = ..., verifyConstraints: typing.Any = ..., matchTags: typing.Any = ..., matchConstraints: typing.Any = ...) -> _TSequenceOfAndSetOfBase: ...
    def sort(self, key: typing.Any = ..., reverse: typing.Any = ...) -> None: ...

class Set(SequenceAndSetBase):
    __doc__: str
    _componentTypeLen: int
    _componentValues: Union[pyasn1.type.base.NoValue, List[nothing]]
    _dynamicNames: typing.Any
    componentTagMap: typing.Any
    componentType: pyasn1.type.namedtype.NamedTypes
    subtypeSpec: pyasn1.type.constraint.ConstraintsIntersection
    tagSet: pyasn1.type.tag.TagSet
    typeId: typing.Any
    def getComponent(self: _TSet, innerFlag: typing.Any = ...) -> _TSet: ...
    def getComponentByType(self, tagSet: typing.Any, default: typing.Any = ..., instantiate: typing.Any = ..., innerFlag: typing.Any = ...) -> typing.Any: ...
    def setComponentByType(self, tagSet: typing.Any, value: typing.Any = ..., verifyConstraints: typing.Any = ..., matchTags: typing.Any = ..., matchConstraints: typing.Any = ..., innerFlag: typing.Any = ...) -> typing.Any: ...

class SetOf(SequenceOfAndSetOfBase):
    __doc__: str
    _componentValues: pyasn1.type.base.NoValue
    componentType: None
    subtypeSpec: pyasn1.type.constraint.ConstraintsIntersection
    tagSet: pyasn1.type.tag.TagSet
    typeId: typing.Any

class SizedInteger(int):
    bitLength: typing.Any
    leadingZeroBits: typing.Any
    def __len__(self) -> typing.Any: ...
    def setBitLength(self: _TSizedInteger, bitLength: typing.Any) -> _TSizedInteger: ...

def all(iterable: typing.Any) -> bool: ...
