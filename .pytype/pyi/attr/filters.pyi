# (generated with --quick)

import __future__
import attr._make
from typing import Any, Callable, Tuple, Type

Attribute: Type[attr._make.Attribute]
absolute_import: __future__._Feature
division: __future__._Feature
print_function: __future__._Feature

def _split_what(what) -> Tuple[frozenset, frozenset]: ...
def exclude(*what) -> Callable[[Any, Any], Any]: ...
def include(*what) -> Callable[[Any, Any], Any]: ...
def isclass(klass) -> bool: ...
