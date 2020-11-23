# (generated with --quick)

from typing import Any, Callable, List, NoReturn, Tuple, Type, TypeVar

Final: _FinalForm
GenericMeta: Type[type]
HAVE_ANNOTATED: bool
HAVE_PROTOCOLS: bool
OLD_GENERICS: bool
PEP_560: bool
SUBS_TREE: bool
TypeAlias: _TypeAliasForm
TypingMeta: Type[type]
_GenericAlias: Any
_PROTO_WHITELIST: List[str]
_TypingEllipsis: Any
_TypingEmpty: Any
__all__: list
_check_methods_in_mro: Any
_collections_abc: module
_geqv: None
_geqv_defined: bool
_next_in_mro: Any
_subs_tree: Any
_tp_cache: Any
_type_check: Any
_type_vars: Any
abc: module
collections: module
collections_abc: module
contextlib: module
operator: module
sys: module
typing: module

KT = TypeVar('KT')
T = TypeVar('T')
T_co = TypeVar('T_co')
T_contra = TypeVar('T_contra')
VT = TypeVar('VT')
VT_co = TypeVar('VT_co')
V_co = TypeVar('V_co')
_T = TypeVar('_T')
_T0 = TypeVar('_T0')
_T_AnnotatedAlias = TypeVar('_T_AnnotatedAlias', bound=_AnnotatedAlias)

class Annotated:
    __slots__ = []
    __class_getitem__: Any
    __doc__: str
    def __init_subclass__(cls: Annotated, *args, **kwargs) -> NoReturn: ...
    def __new__(cls, *args, **kwargs) -> NoReturn: ...

class TypedDict(dict, metaclass=_TypedDictMeta):
    __doc__: str
    __optional_keys__: frozenset
    __required_keys__: frozenset
    __total__: bool
    def __new__(*args, total = ..., **kwargs) -> Any: ...

class _AnnotatedAlias(Any):
    __doc__: str
    __metadata__: Any
    def __eq__(self, other) -> Any: ...
    def __hash__(self) -> int: ...
    def __init__(self, origin, metadata) -> None: ...
    def __reduce__(self) -> Tuple[Callable, Tuple[Type[Annotated], tuple]]: ...
    def __repr__(self) -> str: ...
    def copy_with(self: _T_AnnotatedAlias, params) -> _T_AnnotatedAlias: ...

class _ExtensionsGenericMeta(type):
    def __subclasscheck__(self, subclass) -> Any: ...

class _FinalForm(Any):
    def __getitem__(self, parameters) -> Any: ...
    def __repr__(self) -> str: ...

class _TypeAliasForm(Any):
    def __repr__(self) -> str: ...

class _TypedDictMeta(type):
    def __instancecheck__(cls: _TypedDictMeta, other) -> bool: ...
    def __new__(cls, name, bases, ns, total = ...) -> Any: ...
    def __subclasscheck__(cls: _TypedDictMeta, other) -> bool: ...

def IntVar(name) -> Any: ...
def _check_fails(cls: _TypedDictMeta, other) -> bool: ...
def _check_generic(cls, parameters) -> None: ...
def _define_guard(type_name) -> bool: ...
def _dict_new(*args, **kwargs) -> dict: ...
def _generic_new(base_cls, cls, *args, **kwargs) -> Any: ...
def _get_protocol_attrs(cls) -> set: ...
def _gorg(cls) -> Any: ...
def _is_callable_members_only(cls) -> bool: ...
def _no_slots_copy(dct) -> dict: ...
def _overload_dummy(*args, **kwds) -> NoReturn: ...
def _strip_annotations(t) -> Any: ...
def _typeddict_new(*args, total = ..., **kwargs) -> Any: ...
def final(f: _T0) -> _T0: ...
def get_args(tp) -> Any: ...
def get_origin(tp) -> Any: ...
def get_type_hints(obj, globalns = ..., localns = ..., include_extras = ...) -> Any: ...
def overload(func) -> Callable: ...
def runtime(cls: _T) -> _T: ...
