# (generated with --quick)

import jose.backends.base
import jose.constants
import jose.exceptions
import pyasn1.error
import rsa.key
from typing import Any, Dict, Optional, Tuple, Type, TypeVar, Union

ALGORITHMS: jose.constants.Algorithms
ASN1_SEQUENCE_ID: bytes
JWKError: Type[jose.exceptions.JWKError]
Key: Type[jose.backends.base.Key]
LEGACY_INVALID_PKCS8_RSA_HEADER: bytes
PyAsn1Error: Type[pyasn1.error.PyAsn1Error]
RSA_ENCRYPTION_ASN1_OID: str
_MAX_RECOVERY_ATTEMPTS: int
binascii: module
pyrsa: module
pyrsa_pem: module
six: module
warnings: module

_T0 = TypeVar('_T0')
_TRSAKey = TypeVar('_TRSAKey', bound=RSAKey)

class RSAKey(jose.backends.base.Key):
    SHA256: str
    SHA384: str
    SHA512: str
    _algorithm: Any
    _prepared_key: Any
    hash_alg: Optional[str]
    def __init__(self, key, algorithm) -> None: ...
    def _process_jwk(self, jwk_dict) -> Union[rsa.key.PrivateKey, rsa.key.PublicKey]: ...
    def is_public(self) -> bool: ...
    def public_key(self: _TRSAKey) -> _TRSAKey: ...
    def sign(self, msg) -> bytes: ...
    def to_dict(self) -> Dict[str, Any]: ...
    def to_pem(self, pem_format = ...) -> bytes: ...
    def verify(self, msg, sig) -> bool: ...

def _gcd(a: _T0, b) -> _T0: ...
def _legacy_private_key_pkcs8_to_pkcs1(pkcs8_key) -> Any: ...
def _rsa_recover_prime_factors(n, e, d) -> Tuple[Any, Any]: ...
def base64_to_long(data) -> Any: ...
def long_to_base64(data, size = ...) -> bytes: ...
def pem_to_spki(pem, fmt = ...) -> Any: ...
def rsa_private_key_pkcs1_to_pkcs8(pkcs1_key) -> Any: ...
def rsa_private_key_pkcs8_to_pkcs1(pkcs8_key) -> Any: ...
def rsa_public_key_pkcs1_to_pkcs8(pkcs1_key) -> Any: ...
