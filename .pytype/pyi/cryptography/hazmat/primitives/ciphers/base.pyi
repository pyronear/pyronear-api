# (generated with --quick)

import __future__
import cryptography.exceptions
import cryptography.hazmat.backends.interfaces
from typing import Any, Type

AlreadyFinalized: Type[cryptography.exceptions.AlreadyFinalized]
AlreadyUpdated: Type[cryptography.exceptions.AlreadyUpdated]
CipherBackend: Type[cryptography.hazmat.backends.interfaces.CipherBackend]
NotYetFinalized: Type[cryptography.exceptions.NotYetFinalized]
UnsupportedAlgorithm: Type[cryptography.exceptions.UnsupportedAlgorithm]
_AEADCipherContext: Any
_AEADEncryptionContext: Any
_CipherContext: Any
_Reasons: Type[cryptography.exceptions._Reasons]
abc: module
absolute_import: __future__._Feature
division: __future__._Feature
modes: Any
print_function: __future__._Feature
six: module
utils: module

class AEADCipherContext(metaclass=abc.ABCMeta):
    @abstractmethod
    def authenticate_additional_data(self, data) -> Any: ...

class AEADDecryptionContext(metaclass=abc.ABCMeta):
    @abstractmethod
    def finalize_with_tag(self, tag) -> Any: ...

class AEADEncryptionContext(metaclass=abc.ABCMeta):
    tag: Any

class BlockCipherAlgorithm(metaclass=abc.ABCMeta):
    block_size: Any

class Cipher:
    _backend: Any
    algorithm: Any
    mode: Any
    def __init__(self, algorithm, mode, backend = ...) -> None: ...
    def _wrap_ctx(self, ctx, encrypt) -> Any: ...
    def decryptor(self) -> Any: ...
    def encryptor(self) -> Any: ...

class CipherAlgorithm(metaclass=abc.ABCMeta):
    key_size: Any
    name: Any

class CipherContext(metaclass=abc.ABCMeta):
    @abstractmethod
    def finalize(self) -> Any: ...
    @abstractmethod
    def update(self, data) -> Any: ...
    @abstractmethod
    def update_into(self, data, buf) -> Any: ...

def _get_backend(backend) -> Any: ...
