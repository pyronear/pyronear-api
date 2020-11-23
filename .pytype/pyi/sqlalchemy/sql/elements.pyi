# (generated with --quick)

import __builtin__
import __future__
import sqlalchemy.sql.annotation
import sqlalchemy.sql.base
import sqlalchemy.sql.operators
import sqlalchemy.sql.visitors
import typing
from typing import Any, Dict, Generator, List, NoReturn, Pattern, Set, Type, TypeVar, Union

_generated_label = _truncated_label

Annotated: Type[sqlalchemy.sql.annotation.Annotated]
Executable: Type[sqlalchemy.sql.base.Executable]
Immutable: Type[sqlalchemy.sql.base.Immutable]
NO_ARG: Any
PARSE_AUTOCOMMIT: Any
RANGE_CURRENT: Any
RANGE_UNBOUNDED: Any
Visitable: Type[sqlalchemy.sql.visitors.Visitable]
_NONE_NAME: Any
_generative: Any
_guess_straight_column: Pattern[str]
_labeled: Any
exc: module
inspection: module
itertools: module
numbers: module
operator: module
operators: module
re: module
type_api: module
unicode_literals: __future__._Feature
util: module

_T0 = TypeVar('_T0')
_TAsBoolean = TypeVar('_TAsBoolean', bound=AsBoolean)
_TClauseElement = TypeVar('_TClauseElement', bound=ClauseElement)
_TCollectionAggregate = TypeVar('_TCollectionAggregate', bound=CollectionAggregate)
_TFalse_ = TypeVar('_TFalse_', bound=False_)
_TFunctionFilter = TypeVar('_TFunctionFilter', bound=FunctionFilter)
_TGrouping = TypeVar('_TGrouping', bound=Grouping)
_TLabel = TypeVar('_TLabel', bound=Label)
_TNull = TypeVar('_TNull', bound=Null)
_TSlice = TypeVar('_TSlice', bound=Slice)
_TTrue_ = TypeVar('_TTrue_', bound=True_)
_TTypeCoerce = TypeVar('_TTypeCoerce', bound=TypeCoerce)
_TUnaryExpression = TypeVar('_TUnaryExpression', bound=UnaryExpression)
_T_truncated_label = TypeVar('_T_truncated_label', bound=_truncated_label)

class AnnotatedColumnElement(sqlalchemy.sql.annotation.Annotated):
    anon_label: Any
    info: Any
    key: Any
    name: Any
    table: Any
    def __init__(self, element, values) -> None: ...
    def _with_annotations(self, values) -> Any: ...

class AsBoolean(UnaryExpression):
    _is_implicitly_boolean: Any
    element: Any
    modifier: None
    negate: Any
    operator: Any
    type: Any
    wraps_column_expression: bool
    def __init__(self, element, operator, negate) -> None: ...
    def _negate(self) -> Any: ...
    def self_group(self: _TAsBoolean, against = ...) -> _TAsBoolean: ...

class BinaryExpression(ColumnElement):
    __doc__: str
    __visit_name__: str
    _from_objects: Any
    _is_implicitly_boolean: Any
    _orig: typing.Tuple[Any, Any]
    is_comparison: Any
    left: Any
    modifiers: Any
    negate: Any
    operator: Any
    right: Any
    type: Any
    def __bool__(self) -> Any: ...
    def __init__(self, left, right, operator, type_ = ..., negate = ..., modifiers = ...) -> None: ...
    def __nonzero__(self) -> Any: ...
    def _copy_internals(self, clone = ..., **kw) -> None: ...
    def _negate(self) -> Any: ...
    def compare(self, other, **kw) -> Any: ...
    def get_children(self, **kwargs) -> typing.Tuple[Any, Any]: ...
    def self_group(self, against = ...) -> Union[BinaryExpression, Grouping]: ...

class BindParameter(ColumnElement):
    __doc__: str
    __visit_name__: str
    _expanding_in_types: typing.Tuple[()]
    _identifying_key: Any
    _is_crud: bool
    _orig_key: Any
    callable: Any
    effective_value: Any
    expanding: Any
    isoutparam: Any
    key: Any
    required: Any
    type: Any
    unique: Any
    value: Any
    def __getstate__(self) -> Any: ...
    def __init__(self, key, value = ..., type_ = ..., unique = ..., required = ..., quote = ..., callable_ = ..., expanding = ..., isoutparam = ..., _compared_to_operator = ..., _compared_to_type = ...) -> None: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state) -> None: ...
    def _clone(self) -> Any: ...
    def _convert_to_unique(self) -> None: ...
    def _with_expanding_in_types(self, types) -> Any: ...
    def _with_value(self, value) -> Any: ...
    def compare(self, other, **kw) -> Any: ...

class BooleanClauseList(ClauseList, ColumnElement):
    __visit_name__: str
    _select_iterable: typing.Tuple[Any]
    _tuple_values: bool
    def __init__(self, *arg, **kw) -> NoReturn: ...
    @classmethod
    def _construct(cls, operator, continue_on, skip_on, *clauses, **kw) -> Any: ...
    def _negate(self) -> Any: ...
    @classmethod
    def and_(cls, *clauses) -> Any: ...
    @classmethod
    def or_(cls, *clauses) -> Any: ...
    def self_group(self, against = ...) -> Any: ...

class Case(ColumnElement):
    __doc__: str
    __visit_name__: str
    _from_objects: List[nothing]
    else_: Any
    type: Any
    value: Any
    whens: Any
    def __init__(self, whens, value = ..., else_ = ...) -> None: ...
    def _copy_internals(self, clone = ..., **kw) -> None: ...
    def get_children(self, **kwargs) -> Generator[Any, Any, None]: ...

class Cast(ColumnElement):
    __doc__: str
    __visit_name__: str
    _from_objects: Any
    clause: Any
    type: Any
    typeclause: Any
    def __init__(self, expression, type_) -> None: ...
    def _copy_internals(self, clone = ..., **kw) -> None: ...
    def get_children(self, **kwargs) -> typing.Tuple[Any, Any]: ...

class ClauseElement(sqlalchemy.sql.visitors.Visitable):
    __and__: Any
    __doc__: str
    __or__: Any
    __visit_name__: str
    _annotations: Dict[nothing, nothing]
    _cloned_set: Any
    _constructor: Any
    _from_objects: List[nothing]
    _is_clone_of: None
    _is_from_container: bool
    _order_by_label_element: None
    bind: None
    compile: Any
    description: None
    is_clause_element: bool
    is_selectable: bool
    supports_execution: bool
    def __bool__(self) -> NoReturn: ...
    def __getstate__(self) -> Any: ...
    def __invert__(self) -> Any: ...
    def __nonzero__(self) -> NoReturn: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> Any: ...
    def _annotate(self, values) -> Any: ...
    def _clone(self) -> Any: ...
    def _compiler(self, dialect, **kw) -> Any: ...
    def _copy_internals(self, clone = ..., **kw) -> None: ...
    def _deannotate(self, values = ..., clone = ...) -> Any: ...
    def _execute_on_connection(self, connection, multiparams, params) -> NoReturn: ...
    def _negate(self) -> UnaryExpression: ...
    def _params(self, unique, optionaldict, kwargs) -> Any: ...
    def _with_annotations(self, values) -> Any: ...
    def compare(self, other, **kw) -> bool: ...
    def get_children(self, **kwargs) -> List[nothing]: ...
    def params(self, *optionaldict, **kwargs) -> Any: ...
    def self_group(self: _TClauseElement, against = ...) -> _TClauseElement: ...
    def unique_params(self, *optionaldict, **kwargs) -> Any: ...

class ClauseList(ClauseElement):
    __doc__: str
    __visit_name__: str
    _from_objects: List[nothing]
    _is_implicitly_boolean: Any
    _select_iterable: Any
    _tuple_values: Any
    clauses: Any
    group: Any
    group_contents: Any
    operator: Any
    def __init__(self, *clauses, **kwargs) -> None: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
    def _copy_internals(self, clone = ..., **kw) -> None: ...
    def append(self, clause) -> None: ...
    def compare(self, other, **kw) -> Any: ...
    def get_children(self, **kwargs) -> Any: ...
    def self_group(self, against = ...) -> Union[ClauseList, Grouping]: ...

class CollationClause(ColumnElement):
    __visit_name__: str
    collation: Any
    def __init__(self, collation) -> None: ...

class CollectionAggregate(UnaryExpression):
    __doc__: str
    element: Any
    modifier: Any
    negate: Any
    operator: Any
    type: Any
    wraps_column_expression: Any
    @classmethod
    def _create_all(cls: __builtin__.type[_TCollectionAggregate], expr) -> _TCollectionAggregate: ...
    @classmethod
    def _create_any(cls: __builtin__.type[_TCollectionAggregate], expr) -> _TCollectionAggregate: ...
    def operate(self, op, *other, **kwargs) -> Any: ...
    def reverse_operate(self, op, other, **kwargs) -> NoReturn: ...

class ColumnClause(sqlalchemy.sql.base.Immutable, ColumnElement):
    __doc__: str
    __visit_name__: str
    _ddl_label: Any
    _from_objects: Any
    _is_clone_of: Any
    _is_multiparam_column: bool
    _key_label: Any
    _label: Any
    _memoized_property: Any
    _proxies: List[ColumnElement]
    _render_label_in_columns_clause: Any
    default: None
    description: Any
    is_literal: Any
    key: Any
    name: Any
    onupdate: None
    server_default: None
    server_onupdate: None
    table: Any
    type: Any
    def __init__(self, text, type_ = ..., is_literal = ..., _selectable = ...) -> None: ...
    def _bind_param(self, operator, obj, type_ = ...) -> BindParameter: ...
    def _compare_name_for_result(self, other) -> Any: ...
    def _gen_label(self, name, dedupe_on_key = ...) -> Any: ...
    def _get_table(self) -> Any: ...
    def _make_proxy(self, selectable, name = ..., attach = ..., name_is_truncatable = ..., disallow_is_literal = ..., **kw) -> Any: ...
    def _set_table(self, table) -> None: ...

class ColumnElement(sqlalchemy.sql.operators.ColumnOperators, ClauseElement):
    __doc__: str
    __visit_name__: str
    _allow_label_resolve: bool
    _alt_names: typing.Tuple[()]
    _is_implicitly_boolean: bool
    _key_label: None
    _label: None
    _proxies: typing.Tuple[()]
    _render_label_in_columns_clause: bool
    _resolve_label: None
    _select_iterable: typing.Tuple[Any]
    anon_label: Any
    base_columns: Any
    comparator: Any
    expression: Any
    foreign_keys: List[nothing]
    key: None
    primary_key: bool
    proxy_set: Any
    type: Any
    def __getattr__(self, key) -> Any: ...
    def _bind_param(self, operator, obj, type_ = ...) -> BindParameter: ...
    def _compare_name_for_result(self, other) -> Any: ...
    def _make_proxy(self, selectable, name = ..., name_is_truncatable = ..., **kw) -> ColumnClause: ...
    def _negate(self) -> Any: ...
    def _uncached_proxy_set(self) -> set: ...
    def cast(self, type_) -> Cast: ...
    def compare(self, other, use_proxies = ..., equivalents = ..., **kw) -> bool: ...
    def label(self, name) -> Label: ...
    def operate(self, op, *other, **kwargs) -> Any: ...
    def reverse_operate(self, op, other, **kwargs) -> Any: ...
    def self_group(self, against = ...) -> ColumnElement: ...
    def shares_lineage(self, othercolumn) -> bool: ...

class Extract(ColumnElement):
    __doc__: str
    __visit_name__: str
    _from_objects: Any
    expr: Any
    field: Any
    type: Any
    def __init__(self, field, expr, **kwargs) -> None: ...
    def _copy_internals(self, clone = ..., **kw) -> None: ...
    def get_children(self, **kwargs) -> typing.Tuple[Any]: ...

class False_(ColumnElement):
    __doc__: str
    __visit_name__: str
    type: Any
    @classmethod
    def _instance(cls: __builtin__.type[_TFalse_]) -> _TFalse_: ...
    def _negate(self) -> True_: ...
    def compare(self, other) -> bool: ...

class FunctionFilter(ColumnElement):
    __doc__: str
    __visit_name__: str
    _from_objects: List[nothing]
    criterion: Any
    func: Any
    type: Any
    def __init__(self, func, *criterion) -> None: ...
    def _copy_internals(self, clone = ..., **kw) -> None: ...
    def filter(self: _TFunctionFilter, *criterion) -> _TFunctionFilter: ...
    def get_children(self, **kwargs) -> Any: ...
    def over(self, partition_by = ..., order_by = ..., range_ = ..., rows = ...) -> Over: ...
    def self_group(self, against = ...) -> Union[FunctionFilter, Grouping]: ...

class Grouping(ColumnElement):
    __doc__: str
    __visit_name__: str
    _from_objects: Any
    _is_implicitly_boolean: Any
    _key_label: Any
    _label: Any
    _proxies: list
    element: Any
    type: Any
    def __getattr__(self, attr) -> Any: ...
    def __getstate__(self) -> Dict[str, Any]: ...
    def __init__(self, element) -> None: ...
    def __setstate__(self, state) -> None: ...
    def _copy_internals(self, clone = ..., **kw) -> None: ...
    def compare(self, other, **kw) -> Any: ...
    def get_children(self, **kwargs) -> typing.Tuple[Any]: ...
    def self_group(self: _TGrouping, against = ...) -> _TGrouping: ...

class IndexExpression(BinaryExpression):
    __doc__: str
    _is_implicitly_boolean: Any
    _orig: typing.Tuple[Any, Any]
    left: Any
    modifiers: Any
    negate: Any
    operator: Any
    right: Any
    type: Any

class Label(ColumnElement):
    __doc__: str
    __visit_name__: str
    _allow_label_resolve: Any
    _element: Any
    _from_objects: Any
    _is_implicitly_boolean: Any
    _key_label: Any
    _label: Any
    _order_by_label_element: Any
    _proxies: list
    _resolve_label: Any
    _type: Any
    element: Any
    foreign_keys: Any
    key: Any
    name: Any
    primary_key: Any
    type: Any
    def __init__(self, name, element, type_ = ...) -> None: ...
    def __reduce__(self) -> typing.Tuple[__builtin__.type[Label], typing.Tuple[Any, Any, Any]]: ...
    def _apply_to_inner(self: _TLabel, fn, *arg, **kw) -> _TLabel: ...
    def _copy_internals(self, clone = ..., anonymize_labels = ..., **kw) -> None: ...
    def _make_proxy(self, selectable, name = ..., **kw) -> Any: ...
    def _negate(self) -> Any: ...
    def get_children(self, **kwargs) -> typing.Tuple[Any]: ...
    def self_group(self, against = ...) -> Any: ...

class Null(ColumnElement):
    __doc__: str
    __visit_name__: str
    type: Any
    @classmethod
    def _instance(cls: __builtin__.type[_TNull]) -> _TNull: ...
    def compare(self, other) -> bool: ...

class Over(ColumnElement):
    __doc__: str
    __visit_name__: str
    _from_objects: List[nothing]
    element: Any
    func: Any
    order_by: Any
    partition_by: Any
    range_: Any
    rows: Any
    type: Any
    def __init__(self, element, partition_by = ..., order_by = ..., range_ = ..., rows = ...) -> None: ...
    def _copy_internals(self, clone = ..., **kw) -> None: ...
    def _interpret_range(self, range_) -> typing.Tuple[Any, Any]: ...
    def get_children(self, **kwargs) -> Any: ...

class ReleaseSavepointClause(_IdentifiedClause):
    __visit_name__: str
    ident: Any

class RollbackToSavepointClause(_IdentifiedClause):
    __visit_name__: str
    ident: Any

class SavepointClause(_IdentifiedClause):
    __visit_name__: str
    ident: Any

class Slice(ColumnElement):
    __doc__: str
    __visit_name__: str
    start: Any
    step: Any
    stop: Any
    type: Any
    def __init__(self, start, stop, step) -> None: ...
    def self_group(self: _TSlice, against = ...) -> _TSlice: ...

class TextClause(sqlalchemy.sql.base.Executable, ClauseElement):
    __doc__: str
    __visit_name__: str
    _allow_label_resolve: bool
    _bind: Any
    _bind_params_regex: Pattern[str]
    _bindparams: dict
    _create_text: Any
    _execution_options: Any
    _hide_froms: List[nothing]
    _is_implicitly_boolean: bool
    _label: None
    _resolve_label: None
    _select_iterable: typing.Tuple[Any]
    bindparams: Any
    columns: Any
    comparator: Any
    key: None
    selectable: Any
    text: str
    type: Any
    def __and__(self, other) -> Any: ...
    def __init__(self, text, bind = ...) -> None: ...
    def _copy_internals(self, clone = ..., **kw) -> None: ...
    def compare(self, other) -> Any: ...
    def get_children(self, **kwargs) -> list: ...
    def self_group(self, against = ...) -> Union[Grouping, TextClause]: ...

class True_(ColumnElement):
    __doc__: str
    __visit_name__: str
    type: Any
    @classmethod
    def _ifnone(cls: __builtin__.type[True_], other) -> Any: ...
    @classmethod
    def _instance(cls: __builtin__.type[_TTrue_]) -> _TTrue_: ...
    def _negate(self) -> False_: ...
    def compare(self, other) -> bool: ...

class Tuple(ClauseList, ColumnElement):
    __doc__: str
    _is_implicitly_boolean: Any
    _select_iterable: typing.Tuple[Any]
    _tuple_values: Any
    _type_tuple: Any
    clauses: Any
    group: Any
    group_contents: Any
    operator: Any
    type: Any
    def __init__(self, *clauses, **kw) -> None: ...
    def _bind_param(self, operator, obj, type_ = ...) -> Any: ...

class TypeClause(ClauseElement):
    __doc__: str
    __visit_name__: str
    type: Any
    def __init__(self, type_) -> None: ...

class TypeCoerce(ColumnElement):
    __doc__: str
    __visit_name__: str
    _from_objects: Any
    clause: Any
    type: Any
    typed_expression: Any
    def __init__(self, expression, type_) -> None: ...
    def _copy_internals(self, clone = ..., **kw) -> None: ...
    def get_children(self, **kwargs) -> typing.Tuple[Any]: ...
    def self_group(self: _TTypeCoerce, against = ...) -> _TTypeCoerce: ...

class UnaryExpression(ColumnElement):
    __doc__: str
    __visit_name__: str
    _from_objects: Any
    _order_by_label_element: Any
    element: Any
    modifier: Any
    negate: Any
    operator: Any
    type: Any
    wraps_column_expression: Any
    def __init__(self, element, operator = ..., modifier = ..., type_ = ..., negate = ..., wraps_column_expression = ...) -> None: ...
    def _copy_internals(self, clone = ..., **kw) -> None: ...
    @classmethod
    def _create_asc(cls: __builtin__.type[_TUnaryExpression], column) -> _TUnaryExpression: ...
    @classmethod
    def _create_desc(cls: __builtin__.type[_TUnaryExpression], column) -> _TUnaryExpression: ...
    @classmethod
    def _create_distinct(cls: __builtin__.type[_TUnaryExpression], expr) -> _TUnaryExpression: ...
    @classmethod
    def _create_nullsfirst(cls: __builtin__.type[_TUnaryExpression], column) -> _TUnaryExpression: ...
    @classmethod
    def _create_nullslast(cls: __builtin__.type[_TUnaryExpression], column) -> _TUnaryExpression: ...
    def _negate(self) -> Any: ...
    def compare(self, other, **kw) -> Any: ...
    def get_children(self, **kwargs) -> typing.Tuple[Any]: ...
    def self_group(self, against = ...) -> Union[Grouping, UnaryExpression]: ...

class WithinGroup(ColumnElement):
    __doc__: str
    __visit_name__: str
    _from_objects: List[nothing]
    element: Any
    order_by: Any
    type: Any
    def __init__(self, element, *order_by) -> None: ...
    def _copy_internals(self, clone = ..., **kw) -> None: ...
    def get_children(self, **kwargs) -> Any: ...
    def over(self, partition_by = ..., order_by = ..., range_ = ..., rows = ...) -> Over: ...

class _IdentifiedClause(sqlalchemy.sql.base.Executable, ClauseElement):
    __visit_name__: str
    _execution_options: Any
    ident: Any
    def __init__(self, ident) -> None: ...

class _anonymous_label(_truncated_label):
    __slots__ = []
    __doc__: str
    def __add__(self, other) -> Any: ...
    def __radd__(self, other) -> Any: ...
    def apply_map(self, map_) -> Any: ...

class _defer_name(_truncated_label):
    __slots__ = []
    __doc__: str
    def __new__(cls, value) -> Any: ...
    def __reduce__(self) -> typing.Tuple[Type[_defer_name], typing.Tuple[str]]: ...

class _defer_none_name(_defer_name):
    __slots__ = []
    __doc__: str

class _label_reference(ColumnElement):
    __doc__: str
    __visit_name__: str
    _from_objects: typing.Tuple[()]
    element: Any
    def __init__(self, element) -> None: ...
    def _copy_internals(self, clone = ..., **kw) -> None: ...

class _textual_label_reference(ColumnElement):
    __visit_name__: str
    _text_clause: Any
    element: Any
    def __init__(self, element) -> None: ...

class _truncated_label(quoted_name):
    __slots__ = []
    __doc__: str
    def __new__(cls, value, quote = ...) -> Any: ...
    def __reduce__(self) -> typing.Tuple[Type[_truncated_label], typing.Tuple[str, Any]]: ...
    def apply_map(self: _T_truncated_label, map_) -> _T_truncated_label: ...

class conv(_truncated_label):
    __slots__ = []
    __doc__: str

class quoted_name(Any, str):
    __slots__ = ["lower", "quote", "upper"]
    __doc__: str
    def __new__(cls, value, quote) -> Any: ...
    def __reduce__(self) -> typing.Tuple[Type[quoted_name], typing.Tuple[str, Any]]: ...
    def __repr__(self) -> str: ...
    def _memoized_method_lower(self) -> str: ...
    def _memoized_method_upper(self) -> str: ...

def _as_truncated(value) -> Any: ...
def _clause_element_as_expr(element) -> Any: ...
def _clone(element, **kw) -> Any: ...
def _cloned_difference(a, b) -> set: ...
def _cloned_intersection(a, b) -> set: ...
def _column_as_key(element) -> Any: ...
def _const_expr(element: _T0) -> Union[False_, Null, True_, _T0]: ...
def _corresponding_column_or_error(fromclause, column, require_embedded = ...) -> Any: ...
def _document_text_coercion(paramname, meth_rst, param_rst) -> Any: ...
def _expand_cloned(elements) -> itertools.chain[nothing]: ...
def _expression_literal_as_text(element) -> Any: ...
def _find_columns(clause) -> Set[nothing]: ...
def _interpret_as_column_or_from(element) -> Any: ...
def _is_column(col) -> bool: ...
def _is_literal(element) -> bool: ...
def _literal_and_labels_as_label_reference(element) -> Any: ...
def _literal_as(element, text_fallback) -> Any: ...
def _literal_as_binds(element, name = ..., type_ = ...) -> Any: ...
def _literal_as_column(element) -> Any: ...
def _literal_as_label_reference(element) -> Any: ...
def _literal_as_text(element, allow_coercion_to_text = ...) -> Any: ...
def _no_column_coercion(element) -> NoReturn: ...
def _no_literals(element) -> Any: ...
def _no_text_coercion(element, exc_cls = ..., extra = ..., err = ...) -> NoReturn: ...
def _only_column_elements(element, name) -> Any: ...
def _only_column_elements_or_none(element, name) -> Any: ...
def _select_iterables(elements) -> itertools.chain[nothing]: ...
def _string_or_unprintable(element: _T0) -> Union[str, _T0]: ...
def _type_from_args(args) -> Any: ...
def and_(*clauses) -> Any: ...
def between(expr, lower_bound, upper_bound, symmetric = ...) -> Any: ...
def cloned_traverse(obj, opts, visitors) -> Any: ...
def collate(expression, collation) -> BinaryExpression: ...
def literal(value, type_ = ...) -> BindParameter: ...
def literal_column(text, type_ = ...) -> ColumnClause: ...
def not_(clause) -> Any: ...
def or_(*clauses) -> Any: ...
def outparam(key, type_ = ...) -> BindParameter: ...
def traverse(obj, opts, visitors) -> Any: ...
