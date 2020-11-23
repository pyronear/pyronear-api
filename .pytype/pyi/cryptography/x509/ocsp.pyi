# (generated with --quick)

import __future__
import enum
from typing import Any, Dict, Tuple, Type, TypeVar

Enum: Type[enum.Enum]
_ALLOWED_HASHES: Tuple[Any, Any, Any, Any, Any]
_CERT_STATUS_TO_ENUM: Dict[Any, OCSPCertStatus]
_EARLIEST_UTC_TIME: datetime.datetime
_OIDS_TO_HASH: Dict[str, Any]
_RESPONSE_STATUS_TO_ENUM: Dict[Any, OCSPResponseStatus]
abc: module
absolute_import: __future__._Feature
datetime: module
division: __future__._Feature
hashes: module
print_function: __future__._Feature
six: module
x509: module

_TOCSPRequestBuilder = TypeVar('_TOCSPRequestBuilder', bound=OCSPRequestBuilder)
_TOCSPResponseBuilder = TypeVar('_TOCSPResponseBuilder', bound=OCSPResponseBuilder)

class OCSPCertStatus(enum.Enum):
    GOOD: int
    REVOKED: int
    UNKNOWN: int

class OCSPRequest(metaclass=abc.ABCMeta):
    extensions: Any
    hash_algorithm: Any
    issuer_key_hash: Any
    issuer_name_hash: Any
    serial_number: Any
    @abstractmethod
    def public_bytes(self, encoding) -> Any: ...

class OCSPRequestBuilder:
    _extensions: Any
    _request: Any
    def __init__(self, request = ..., extensions = ...) -> None: ...
    def add_certificate(self: _TOCSPRequestBuilder, cert, issuer, algorithm) -> _TOCSPRequestBuilder: ...
    def add_extension(self: _TOCSPRequestBuilder, extension, critical) -> _TOCSPRequestBuilder: ...
    def build(self) -> Any: ...

class OCSPResponderEncoding(enum.Enum):
    HASH: str
    NAME: str

class OCSPResponse(metaclass=abc.ABCMeta):
    certificate_status: Any
    certificates: Any
    extensions: Any
    hash_algorithm: Any
    issuer_key_hash: Any
    issuer_name_hash: Any
    next_update: Any
    produced_at: Any
    responder_key_hash: Any
    responder_name: Any
    response_status: Any
    revocation_reason: Any
    revocation_time: Any
    serial_number: Any
    signature: Any
    signature_algorithm_oid: Any
    signature_hash_algorithm: Any
    single_extensions: Any
    tbs_response_bytes: Any
    this_update: Any

class OCSPResponseBuilder:
    _certs: Any
    _extensions: Any
    _responder_id: Any
    _response: Any
    def __init__(self, response = ..., responder_id = ..., certs = ..., extensions = ...) -> None: ...
    def add_extension(self: _TOCSPResponseBuilder, extension, critical) -> _TOCSPResponseBuilder: ...
    def add_response(self: _TOCSPResponseBuilder, cert, issuer, algorithm, cert_status, this_update, next_update, revocation_time, revocation_reason) -> _TOCSPResponseBuilder: ...
    @classmethod
    def build_unsuccessful(cls, response_status) -> Any: ...
    def certificates(self: _TOCSPResponseBuilder, certs) -> _TOCSPResponseBuilder: ...
    def responder_id(self: _TOCSPResponseBuilder, encoding, responder_cert) -> _TOCSPResponseBuilder: ...
    def sign(self, private_key, algorithm) -> Any: ...

class OCSPResponseStatus(enum.Enum):
    INTERNAL_ERROR: int
    MALFORMED_REQUEST: int
    SIG_REQUIRED: int
    SUCCESSFUL: int
    TRY_LATER: int
    UNAUTHORIZED: int

class _SingleResponse:
    _algorithm: Any
    _cert: Any
    _cert_status: Any
    _issuer: Any
    _next_update: Any
    _revocation_reason: Any
    _revocation_time: Any
    _this_update: Any
    def __init__(self, cert, issuer, algorithm, cert_status, this_update, next_update, revocation_time, revocation_reason) -> None: ...

def _convert_to_naive_utc_time(time) -> Any: ...
def _reject_duplicate_extension(extension, extensions) -> None: ...
def _verify_algorithm(algorithm) -> None: ...
def load_der_ocsp_request(data) -> Any: ...
def load_der_ocsp_response(data) -> Any: ...
