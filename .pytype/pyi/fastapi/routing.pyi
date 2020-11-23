# (generated with --quick)

import fastapi.dependencies.models
import fastapi.exceptions
import fastapi.params
import pydantic.class_validators
import pydantic.error_wrappers
import pydantic.fields
import starlette.background
import starlette.convertors
import starlette.datastructures
import starlette.exceptions
import starlette.requests
import starlette.responses
import starlette.routing
import starlette.websockets
from typing import Any, Awaitable, Callable, Coroutine, Dict, List, MutableMapping, Optional, Pattern, Sequence, Set, Tuple, Type, TypeVar, Union

ASGIApp = Callable[[MutableMapping[str, Any], Callable[[], Awaitable[MutableMapping[str, Any]]], Callable[[MutableMapping[str, Any]], Awaitable[None]]], Awaitable[None]]
DictIntStrAny = Dict[Union[int, str], Any]
SetIntStr = Set[Union[int, str]]

BaseModel: Any
Dependant: Type[fastapi.dependencies.models.Dependant]
ErrorWrapper: Type[pydantic.error_wrappers.ErrorWrapper]
HTTPException: Type[starlette.exceptions.HTTPException]
JSONResponse: Type[starlette.responses.JSONResponse]
ModelField: Type[pydantic.fields.ModelField]
Mount: Type[starlette.routing.Mount]
Request: Type[starlette.requests.Request]
RequestValidationError: Type[fastapi.exceptions.RequestValidationError]
Response: Type[starlette.responses.Response]
STATUS_CODES_WITH_NO_BODY: Set[int]
ValidationError: Type[pydantic.error_wrappers.ValidationError]
WS_1008_POLICY_VIOLATION: int
WebSocket: Type[starlette.websockets.WebSocket]
WebSocketRequestValidationError: Type[fastapi.exceptions.WebSocketRequestValidationError]
asyncio: module
enum: module
inspect: module
json: module
params: Any
routing: module

T = TypeVar('T')

class APIRoute(starlette.routing.Route):
    app: Callable[[MutableMapping[str, Any], Callable[[], Awaitable[MutableMapping[str, Any]]], Callable[[MutableMapping[str, Any]], Awaitable[None]]], Awaitable[None]]
    body_field: Optional[pydantic.fields.ModelField]
    callbacks: Optional[List[APIRoute]]
    dependant: fastapi.dependencies.models.Dependant
    dependencies: list
    dependency_overrides_provider: Any
    deprecated: Optional[bool]
    description: Any
    endpoint: Callable
    include_in_schema: bool
    methods: set
    name: str
    operation_id: Optional[str]
    param_convertors: Dict[str, starlette.convertors.Convertor]
    path: str
    path_format: str
    path_regex: Pattern[Union[bytes, str]]
    response_class: Optional[Type[starlette.responses.Response]]
    response_description: str
    response_field: Optional[pydantic.fields.ModelField]
    response_fields: Dict[Any, pydantic.fields.ModelField]
    response_model: Any
    response_model_by_alias: bool
    response_model_exclude: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]]
    response_model_exclude_defaults: bool
    response_model_exclude_none: bool
    response_model_exclude_unset: bool
    response_model_include: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]]
    responses: Dict[Union[int, str], Dict[str, Any]]
    secure_cloned_response_field: Optional[pydantic.fields.ModelField]
    status_code: int
    summary: Optional[str]
    tags: List[str]
    unique_id: str
    def __init__(self, path: str, endpoint: Callable, *, response_model: Optional[type] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: bool = ..., name: Optional[str] = ..., methods: Optional[Union[List[str], Set[str]]] = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_exclude: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[starlette.responses.Response]] = ..., dependency_overrides_provider = ..., callbacks: Optional[List[APIRoute]] = ...) -> None: ...
    def get_route_handler(self) -> Callable: ...

class APIRouter(starlette.routing.Router):
    default_response_class: Optional[Type[starlette.responses.Response]]
    dependency_overrides_provider: Any
    route_class: Type[APIRoute]
    def __init__(self, routes: Optional[List[starlette.routing.BaseRoute]] = ..., redirect_slashes: bool = ..., default: Optional[Callable[[MutableMapping[str, Any], Callable[[], Awaitable[MutableMapping[str, Any]]], Callable[[MutableMapping[str, Any]], Awaitable[None]]], Awaitable[None]]] = ..., dependency_overrides_provider = ..., route_class: Type[APIRoute] = ..., default_response_class: Optional[Type[starlette.responses.Response]] = ..., on_startup: Optional[Sequence[Callable]] = ..., on_shutdown: Optional[Sequence[Callable]] = ...) -> None: ...
    def add_api_route(self, path: str, endpoint: Callable, *, response_model: Optional[type] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: bool = ..., methods: Optional[Union[List[str], Set[str]]] = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_exclude: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[starlette.responses.Response]] = ..., name: Optional[str] = ..., route_class_override: Optional[Type[APIRoute]] = ..., callbacks: Optional[List[APIRoute]] = ...) -> None: ...
    def add_api_websocket_route(self, path: str, endpoint: Callable, name: Optional[str] = ...) -> None: ...
    def api_route(self, path: str, *, response_model: Optional[type] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: bool = ..., methods: Optional[List[str]] = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_exclude: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[starlette.responses.Response]] = ..., name: Optional[str] = ..., callbacks: Optional[List[APIRoute]] = ...) -> Callable: ...
    def delete(self, path: str, *, response_model: Optional[type] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: bool = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_exclude: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[starlette.responses.Response]] = ..., name: Optional[str] = ..., callbacks: Optional[List[APIRoute]] = ...) -> Callable: ...
    def get(self, path: str, *, response_model: Optional[type] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: bool = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_exclude: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[starlette.responses.Response]] = ..., name: Optional[str] = ..., callbacks: Optional[List[APIRoute]] = ...) -> Callable: ...
    def head(self, path: str, *, response_model: Optional[type] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: bool = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_exclude: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[starlette.responses.Response]] = ..., name: Optional[str] = ..., callbacks: Optional[List[APIRoute]] = ...) -> Callable: ...
    def include_router(self, router: APIRouter, *, prefix: str = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence] = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., default_response_class: Optional[Type[starlette.responses.Response]] = ...) -> None: ...
    def options(self, path: str, *, response_model: Optional[type] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: bool = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_exclude: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[starlette.responses.Response]] = ..., name: Optional[str] = ..., callbacks: Optional[List[APIRoute]] = ...) -> Callable: ...
    def patch(self, path: str, *, response_model: Optional[type] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: bool = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_exclude: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[starlette.responses.Response]] = ..., name: Optional[str] = ..., callbacks: Optional[List[APIRoute]] = ...) -> Callable: ...
    def post(self, path: str, *, response_model: Optional[type] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: bool = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_exclude: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[starlette.responses.Response]] = ..., name: Optional[str] = ..., callbacks: Optional[List[APIRoute]] = ...) -> Callable: ...
    def put(self, path: str, *, response_model: Optional[type] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: bool = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_exclude: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[starlette.responses.Response]] = ..., name: Optional[str] = ..., callbacks: Optional[List[APIRoute]] = ...) -> Callable: ...
    def trace(self, path: str, *, response_model: Optional[type] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: bool = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_exclude: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[starlette.responses.Response]] = ..., name: Optional[str] = ..., callbacks: Optional[List[APIRoute]] = ...) -> Callable: ...
    def websocket(self, path: str, name: Optional[str] = ...) -> Callable: ...

class APIWebSocketRoute(starlette.routing.WebSocketRoute):
    app: Callable[[MutableMapping[str, Any], Callable[[], Awaitable[MutableMapping[str, Any]]], Callable[[MutableMapping[str, Any]], Awaitable[None]]], Awaitable[None]]
    dependant: fastapi.dependencies.models.Dependant
    endpoint: Callable
    name: str
    param_convertors: Dict[str, starlette.convertors.Convertor]
    path: str
    path_format: str
    path_regex: Pattern[Union[bytes, str]]
    def __init__(self, path: str, endpoint: Callable, *, name: Optional[str] = ..., dependency_overrides_provider = ...) -> None: ...

def _prepare_response_content(res, *, exclude_unset: bool, exclude_defaults: bool = ..., exclude_none: bool = ...) -> Any: ...
def compile_path(path: str) -> Tuple[Pattern, str, Dict[str, starlette.convertors.Convertor]]: ...
def create_cloned_field(field: pydantic.fields.ModelField, *, cloned_types: Optional[Dict[type, type]] = ...) -> pydantic.fields.ModelField: ...
def create_response_field(name: str, type_: type, class_validators: Optional[Dict[str, pydantic.class_validators.Validator]] = ..., default = ..., required: Union[bool, pydantic.fields.UndefinedType] = ..., model_config: type = ..., field_info: Optional[pydantic.fields.FieldInfo] = ..., alias: Optional[str] = ...) -> pydantic.fields.ModelField: ...
def generate_operation_id_for_path(*, name: str, path: str, method: str) -> str: ...
def get_body_field(*, dependant: fastapi.dependencies.models.Dependant, name: str) -> Optional[pydantic.fields.ModelField]: ...
def get_dependant(*, path: str, call: Callable, name: Optional[str] = ..., security_scopes: Optional[List[str]] = ..., use_cache: bool = ...) -> fastapi.dependencies.models.Dependant: ...
def get_name(endpoint: Callable) -> str: ...
def get_parameterless_sub_dependant(*, depends: fastapi.params.Depends, path: str) -> fastapi.dependencies.models.Dependant: ...
def get_request_handler(dependant: fastapi.dependencies.models.Dependant, body_field: Optional[pydantic.fields.ModelField] = ..., status_code: int = ..., response_class: Type[starlette.responses.Response] = ..., response_field: Optional[pydantic.fields.ModelField] = ..., response_model_include: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_exclude: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., dependency_overrides_provider = ...) -> Callable: ...
def get_websocket_app(dependant: fastapi.dependencies.models.Dependant, dependency_overrides_provider = ...) -> Callable: ...
def jsonable_encoder(obj, include: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., exclude: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., by_alias: bool = ..., exclude_unset: bool = ..., exclude_defaults: bool = ..., exclude_none: bool = ..., custom_encoder: dict = ..., sqlalchemy_safe: bool = ...) -> Any: ...
def request_response(func: Callable) -> Callable[[MutableMapping[str, Any], Callable[[], Awaitable[MutableMapping[str, Any]]], Callable[[MutableMapping[str, Any]], Awaitable[None]]], Awaitable[None]]: ...
def run_endpoint_function(*, dependant: fastapi.dependencies.models.Dependant, values: Dict[str, Any], is_coroutine: bool) -> coroutine: ...
def run_in_threadpool(func: Callable[..., T], *args, **kwargs) -> coroutine: ...
def serialize_response(*, field: Optional[pydantic.fields.ModelField] = ..., response_content, include: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., exclude: Optional[Union[Dict[Union[int, str], Any], Set[Union[int, str]]]] = ..., by_alias: bool = ..., exclude_unset: bool = ..., exclude_defaults: bool = ..., exclude_none: bool = ..., is_coroutine: bool = ...) -> coroutine: ...
def solve_dependencies(*, request: Union[starlette.requests.Request, starlette.websockets.WebSocket], dependant: fastapi.dependencies.models.Dependant, body: Optional[Union[starlette.datastructures.FormData, Dict[str, Any]]] = ..., background_tasks: Optional[starlette.background.BackgroundTasks] = ..., response: Optional[starlette.responses.Response] = ..., dependency_overrides_provider = ..., dependency_cache: Optional[Dict[Tuple[Callable, Tuple[str]], Any]] = ...) -> Coroutine[Any, Any, Tuple[Dict[str, Any], List[pydantic.error_wrappers.ErrorWrapper], Optional[starlette.background.BackgroundTasks], starlette.responses.Response, Dict[Tuple[Callable, Tuple[str]], Any]]]: ...
def websocket_session(func: Callable) -> Callable[[MutableMapping[str, Any], Callable[[], Awaitable[MutableMapping[str, Any]]], Callable[[MutableMapping[str, Any]], Awaitable[None]]], Awaitable[None]]: ...
