# (generated with --quick)

import __builtin__
import __future__
import cryptography.exceptions
import cryptography.hazmat.backends.interfaces
import cryptography.hazmat.backends.openssl.cmac
import cryptography.hazmat.backends.openssl.decode_asn1
import cryptography.hazmat.backends.openssl.poly1305
import cryptography.hazmat.primitives.asymmetric.padding
from typing import Any, Callable, Dict, Iterable, Iterator, Sized, Tuple, Type, TypeVar

_MemoryBIO = `namedtuple-_MemoryBIO-bio-char_ptr`

AES: Any
ARC4: Any
Backend: Any
Blowfish: Any
CAST5: Any
CBC: Any
CFB: Any
CFB8: Any
CMACBackend: Type[cryptography.hazmat.backends.interfaces.CMACBackend]
CTR: Any
Camellia: Any
ChaCha20: Any
CipherBackend: Type[cryptography.hazmat.backends.interfaces.CipherBackend]
DERSerializationBackend: Type[cryptography.hazmat.backends.interfaces.DERSerializationBackend]
DHBackend: Type[cryptography.hazmat.backends.interfaces.DHBackend]
DSABackend: Type[cryptography.hazmat.backends.interfaces.DSABackend]
ECB: Any
EllipticCurveBackend: Type[cryptography.hazmat.backends.interfaces.EllipticCurveBackend]
GCM: Any
HMACBackend: Type[cryptography.hazmat.backends.interfaces.HMACBackend]
HashBackend: Type[cryptography.hazmat.backends.interfaces.HashBackend]
IDEA: Any
INTEGER: int
MGF1: Type[cryptography.hazmat.primitives.asymmetric.padding.MGF1]
NULL: int
OAEP: Any
OFB: Any
PBKDF2HMACBackend: Type[cryptography.hazmat.backends.interfaces.PBKDF2HMACBackend]
PEMSerializationBackend: Type[cryptography.hazmat.backends.interfaces.PEMSerializationBackend]
PKCS1v15: Any
PSS: Any
RSABackend: Type[cryptography.hazmat.backends.interfaces.RSABackend]
SEED: Any
SEQUENCE: int
ScryptBackend: Type[cryptography.hazmat.backends.interfaces.ScryptBackend]
TripleDES: Any
UnsupportedAlgorithm: Type[cryptography.exceptions.UnsupportedAlgorithm]
X509Backend: Type[cryptography.hazmat.backends.interfaces.X509Backend]
XTS: Any
_CMACContext: Type[cryptography.hazmat.backends.openssl.cmac._CMACContext]
_CRL_ENTRY_EXTENSION_ENCODE_HANDLERS: Dict[Any, Callable[[Any, Any], Any]]
_CRL_ENTRY_REASON_ENUM_TO_CODE: Dict[Any, int]
_CRL_EXTENSION_ENCODE_HANDLERS: Dict[Any, Callable[[Any, Any], Any]]
_CRL_EXTENSION_HANDLERS: Dict[Any, Callable[[Any, Any], Any]]
_Certificate: Any
_CertificateRevocationList: Any
_CertificateSigningRequest: Any
_CipherContext: Any
_DHParameters: Any
_DHPrivateKey: Any
_DHPublicKey: Any
_DSAParameters: Any
_DSAPrivateKey: Any
_DSAPublicKey: Any
_ED448_KEY_SIZE: int
_EXTENSION_ENCODE_HANDLERS: Dict[Any, Callable[[Any, Any], Any]]
_EXTENSION_HANDLERS_BASE: Dict[Any, Callable[[Any, Any], Any]]
_EXTENSION_HANDLERS_SCT: Dict[Any, Callable[[Any, Any], Any]]
_Ed25519PrivateKey: Any
_Ed25519PublicKey: Any
_Ed448PrivateKey: Any
_Ed448PublicKey: Any
_EllipticCurvePrivateKey: Any
_EllipticCurvePublicKey: Any
_HMACContext: Any
_HashContext: Any
_OCSPRequest: Any
_OCSPResponse: Any
_OCSP_BASICRESP_EXTENSION_ENCODE_HANDLERS: Dict[Any, Callable[[Any, Any], Any]]
_OCSP_BASICRESP_EXTENSION_HANDLERS: Dict[Any, Callable[[Any, Any], Any]]
_OCSP_REQUEST_EXTENSION_ENCODE_HANDLERS: Dict[Any, Callable[[Any, Any], Any]]
_OCSP_REQ_EXTENSION_HANDLERS: Dict[Any, Callable[[Any, Any], Any]]
_OCSP_SINGLERESP_EXTENSION_HANDLERS_SCT: Dict[Any, Callable[[Any, Any], Any]]
_POLY1305_KEY_SIZE: int
_Poly1305Context: Type[cryptography.hazmat.backends.openssl.poly1305._Poly1305Context]
_REVOKED_EXTENSION_HANDLERS: Dict[Any, Callable[[Any, Any], Any]]
_RSAPrivateKey: Any
_RSAPublicKey: Any
_Reasons: Type[cryptography.exceptions._Reasons]
_RevokedCertificate: Any
_X25519PrivateKey: Any
_X25519PublicKey: Any
_X448PrivateKey: Any
_X448PublicKey: Any
_X509ExtensionParser: Type[cryptography.hazmat.backends.openssl.decode_asn1._X509ExtensionParser]
absolute_import: __future__._Feature
aead: module
backend: Any
binding: module
collections: module
contextlib: module
division: __future__._Feature
dsa: module
ec: module
ed25519: module
ed448: module
hashes: module
itertools: module
ocsp: module
print_function: __future__._Feature
range: Type[__builtin__.range]
rsa: module
scrypt: module
serialization: module
six: module
ssh: module
utils: module
warnings: module
x509: module

_T = TypeVar('_T')
_Tnamedtuple-_MemoryBIO-bio-char_ptr = TypeVar('_Tnamedtuple-_MemoryBIO-bio-char_ptr', bound=`namedtuple-_MemoryBIO-bio-char_ptr`)

class GetCipherByName:
    _fmt: Any
    def __call__(self, backend, cipher, mode) -> Any: ...
    def __init__(self, fmt) -> None: ...

class _RC2: ...

class `namedtuple-_MemoryBIO-bio-char_ptr`(tuple):
    __slots__ = ["bio", "char_ptr"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str]
    bio: Any
    char_ptr: Any
    def __getnewargs__(self) -> Tuple[Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-_MemoryBIO-bio-char_ptr`], bio, char_ptr) -> `_Tnamedtuple-_MemoryBIO-bio-char_ptr`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-_MemoryBIO-bio-char_ptr`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-_MemoryBIO-bio-char_ptr`: ...
    def _replace(self: `_Tnamedtuple-_MemoryBIO-bio-char_ptr`, **kwds) -> `_Tnamedtuple-_MemoryBIO-bio-char_ptr`: ...

def _dh_params_dup(dh_cdata, backend) -> Any: ...
def _encode_asn1_int_gc(backend, x) -> Any: ...
def _encode_asn1_str_gc(backend, data) -> Any: ...
def _encode_name_gc(backend, attributes) -> Any: ...
def _get_xts_cipher(backend, cipher, mode) -> Any: ...
def _txt2obj_gc(backend, name) -> Any: ...
def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., contextlib._GeneratorContextManager[_T]]: ...
def encode_der(tag, *children) -> bytes: ...
def encode_der_integer(x) -> Any: ...
