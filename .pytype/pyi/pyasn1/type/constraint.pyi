# (generated with --quick)

from typing import Any, Dict, List, NoReturn, Set, Tuple, TypeVar

__all__: List[str]
error: module
sys: module

_TAbstractConstraintSet = TypeVar('_TAbstractConstraintSet', bound=AbstractConstraintSet)
_TSingleValueConstraint = TypeVar('_TSingleValueConstraint', bound=SingleValueConstraint)

class AbstractConstraint:
    _AbstractConstraint__hash: int
    _valueMap: Set[nothing]
    _values: Any
    def __bool__(self) -> bool: ...
    def __call__(self, value, idx = ...) -> None: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> int: ...
    def __init__(self, *values) -> None: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __repr__(self) -> str: ...
    def _setValues(self, values) -> None: ...
    def _testValue(self, value, idx) -> NoReturn: ...
    def getValueMap(self) -> Set[nothing]: ...
    def isSubTypeOf(self, otherConstraint) -> Any: ...
    def isSuperTypeOf(self, otherConstraint) -> Any: ...

class AbstractConstraintSet(AbstractConstraint):
    _AbstractConstraint__hash: int
    _valueMap: set
    _values: Any
    def __add__(self: _TAbstractConstraintSet, value) -> _TAbstractConstraintSet: ...
    def __getitem__(self, idx) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
    def __radd__(self: _TAbstractConstraintSet, value) -> _TAbstractConstraintSet: ...
    def _setValues(self, values) -> None: ...

class ComponentAbsentConstraint(AbstractConstraint):
    _AbstractConstraint__hash: int
    __doc__: str
    _valueMap: Set[nothing]
    _values: Tuple[str]
    def _setValues(self, values) -> None: ...
    def _testValue(self, value, idx) -> None: ...

class ComponentPresentConstraint(AbstractConstraint):
    _AbstractConstraint__hash: int
    __doc__: str
    _valueMap: Set[nothing]
    _values: Tuple[str]
    def _setValues(self, values) -> None: ...
    def _testValue(self, value, idx) -> None: ...

class ConstraintsExclusion(AbstractConstraint):
    _AbstractConstraint__hash: int
    __doc__: str
    _valueMap: Set[nothing]
    def _setValues(self, values) -> None: ...
    def _testValue(self, value, idx) -> None: ...

class ConstraintsIntersection(AbstractConstraintSet):
    _AbstractConstraint__hash: int
    __doc__: str
    _valueMap: Set[nothing]
    def _testValue(self, value, idx) -> None: ...

class ConstraintsUnion(AbstractConstraintSet):
    _AbstractConstraint__hash: int
    __doc__: str
    _valueMap: Set[nothing]
    def _testValue(self, value, idx) -> None: ...

class ContainedSubtypeConstraint(AbstractConstraint):
    _AbstractConstraint__hash: int
    __doc__: str
    _valueMap: Set[nothing]
    def _testValue(self, value, idx) -> None: ...

class InnerTypeConstraint(AbstractConstraint):
    _AbstractConstraint__hash: int
    _InnerTypeConstraint__multipleTypeConstraint: Dict[Any, Tuple[Any, Any]]
    _InnerTypeConstraint__singleTypeConstraint: Any
    __doc__: str
    _valueMap: Set[nothing]
    def _setValues(self, values) -> None: ...
    def _testValue(self, value, idx) -> None: ...

class PermittedAlphabetConstraint(SingleValueConstraint):
    _AbstractConstraint__hash: int
    __doc__: str
    _set: set
    _valueMap: Set[nothing]
    _values: Any
    def _setValues(self, values) -> None: ...
    def _testValue(self, value, idx) -> None: ...

class SingleValueConstraint(AbstractConstraint):
    _AbstractConstraint__hash: int
    __doc__: str
    _set: set
    _valueMap: Set[nothing]
    _values: Any
    def __add__(self: _TSingleValueConstraint, constraint) -> _TSingleValueConstraint: ...
    def __contains__(self, item) -> bool: ...
    def __iter__(self) -> Any: ...
    def __sub__(self: _TSingleValueConstraint, constraint) -> _TSingleValueConstraint: ...
    def _setValues(self, values) -> None: ...
    def _testValue(self, value, idx) -> None: ...

class ValueRangeConstraint(AbstractConstraint):
    _AbstractConstraint__hash: int
    __doc__: str
    _valueMap: Set[nothing]
    start: Any
    stop: Any
    def _setValues(self, values) -> None: ...
    def _testValue(self, value, idx) -> None: ...

class ValueSizeConstraint(ValueRangeConstraint):
    _AbstractConstraint__hash: int
    __doc__: str
    _valueMap: Set[nothing]
    def _testValue(self, value, idx) -> None: ...

class WithComponentsConstraint(AbstractConstraint):
    _AbstractConstraint__hash: int
    __doc__: str
    _valueMap: Set[nothing]
    def _setValues(self, values) -> None: ...
    def _testValue(self, value, idx) -> None: ...
