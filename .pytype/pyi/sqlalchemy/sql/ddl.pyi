# (generated with --quick)

import sqlalchemy.sql.base
from typing import Any, Dict, Type

ClauseElement: Any
Executable: Type[sqlalchemy.sql.base.Executable]
SchemaVisitor: Type[sqlalchemy.sql.base.SchemaVisitor]
_generative: Any
event: module
exc: module
topological: module
util: module

class AddConstraint(_CreateDropBase):
    __doc__: str
    __visit_name__: str
    bind: None
    element: Any
    on: Any
    def __init__(self, element, *args, **kw) -> None: ...

class CreateColumn(_DDLCompiles):
    __doc__: str
    __visit_name__: str
    element: Any
    def __init__(self, element) -> None: ...

class CreateIndex(_CreateDropBase):
    __doc__: str
    __visit_name__: str
    bind: Any
    element: Any
    on: Any

class CreateSchema(_CreateDropBase):
    __doc__: str
    __visit_name__: str
    bind: None
    element: Any
    on: None
    quote: Any
    def __init__(self, name, quote = ..., **kw) -> None: ...

class CreateSequence(_CreateDropBase):
    __doc__: str
    __visit_name__: str
    bind: Any
    element: Any
    on: Any

class CreateTable(_CreateDropBase):
    __doc__: str
    __visit_name__: str
    bind: Any
    columns: Any
    element: Any
    include_foreign_key_constraints: Any
    on: Any
    def __init__(self, element, on = ..., bind = ..., include_foreign_key_constraints = ...) -> None: ...

class DDL(DDLElement):
    __doc__: str
    __init__: Any
    __visit_name__: str
    def __repr__(self) -> str: ...

class DDLBase(sqlalchemy.sql.base.SchemaVisitor):
    connection: Any
    def __init__(self, connection) -> None: ...

class DDLElement(sqlalchemy.sql.base.Executable, _DDLCompiles):
    __doc__: str
    _bind: Any
    _execution_options: Any
    against: Any
    bind: Any
    callable_: None
    dialect: None
    execute_at: Any
    execute_if: Any
    on: None
    target: None
    def __call__(self, target, bind, **kw) -> Any: ...
    def _check_ddl_on(self, on) -> None: ...
    def _execute_on_connection(self, connection, multiparams, params) -> Any: ...
    def _generate(self) -> Any: ...
    def _set_bind(self, bind) -> None: ...
    def _should_execute(self, target, bind, **kw) -> bool: ...
    def _should_execute_deprecated(self, event, target, bind, **kw) -> Any: ...
    def execute(self, bind = ..., target = ...) -> Any: ...

class DropColumnComment(_CreateDropBase):
    __doc__: str
    __visit_name__: str
    bind: Any
    element: Any
    on: Any

class DropConstraint(_CreateDropBase):
    __doc__: str
    __visit_name__: str
    bind: None
    cascade: Any
    element: Any
    on: None
    def __init__(self, element, cascade = ..., **kw) -> None: ...

class DropIndex(_CreateDropBase):
    __doc__: str
    __visit_name__: str
    bind: Any
    element: Any
    on: Any

class DropSchema(_CreateDropBase):
    __doc__: str
    __visit_name__: str
    bind: None
    cascade: Any
    element: Any
    on: None
    quote: Any
    def __init__(self, name, quote = ..., cascade = ..., **kw) -> None: ...

class DropSequence(_CreateDropBase):
    __doc__: str
    __visit_name__: str
    bind: Any
    element: Any
    on: Any

class DropTable(_CreateDropBase):
    __doc__: str
    __visit_name__: str
    bind: Any
    element: Any
    on: Any

class DropTableComment(_CreateDropBase):
    __doc__: str
    __visit_name__: str
    bind: Any
    element: Any
    on: Any

class SchemaDropper(DDLBase):
    checkfirst: Any
    connection: Any
    dialect: Any
    memo: Dict[nothing, nothing]
    preparer: Any
    tables: Any
    def __init__(self, dialect, connection, checkfirst = ..., tables = ..., **kwargs) -> None: ...
    def _can_drop_sequence(self, sequence) -> Any: ...
    def _can_drop_table(self, table) -> Any: ...
    def visit_foreign_key_constraint(self, constraint) -> None: ...
    def visit_index(self, index) -> None: ...
    def visit_metadata(self, metadata) -> None: ...
    def visit_sequence(self, sequence, drop_ok = ...) -> None: ...
    def visit_table(self, table, drop_ok = ..., _is_metadata_operation = ...) -> None: ...

class SchemaGenerator(DDLBase):
    checkfirst: Any
    connection: Any
    dialect: Any
    memo: Dict[nothing, nothing]
    preparer: Any
    tables: Any
    def __init__(self, dialect, connection, checkfirst = ..., tables = ..., **kwargs) -> None: ...
    def _can_create_sequence(self, sequence) -> Any: ...
    def _can_create_table(self, table) -> bool: ...
    def visit_foreign_key_constraint(self, constraint) -> None: ...
    def visit_index(self, index) -> None: ...
    def visit_metadata(self, metadata) -> None: ...
    def visit_sequence(self, sequence, create_ok = ...) -> None: ...
    def visit_table(self, table, create_ok = ..., include_foreign_key_constraints = ..., _is_metadata_operation = ...) -> None: ...

class SetColumnComment(_CreateDropBase):
    __doc__: str
    __visit_name__: str
    bind: Any
    element: Any
    on: Any

class SetTableComment(_CreateDropBase):
    __doc__: str
    __visit_name__: str
    bind: Any
    element: Any
    on: Any

class _CreateDropBase(DDLElement):
    __doc__: str
    bind: Any
    element: Any
    on: Any
    def __init__(self, element, on = ..., bind = ...) -> None: ...
    def _create_rule_disable(self, compiler) -> bool: ...

class _DDLCompiles(Any):
    def _compiler(self, dialect, **kw) -> Any: ...

class _DropView(_CreateDropBase):
    __doc__: str
    __visit_name__: str
    bind: Any
    element: Any
    on: Any

def _bind_or_error(schemaitem, msg = ...) -> Any: ...
def sort_tables(tables, skip_fn = ..., extra_dependencies = ...) -> Any: ...
def sort_tables_and_constraints(tables, filter_fn = ..., extra_dependencies = ..., _warn_for_cycles = ...) -> Any: ...
