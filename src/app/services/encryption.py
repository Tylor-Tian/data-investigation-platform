from __future__ import annotations
from cryptography.fernet import Fernet

_key = Fernet.generate_key()
_cipher = Fernet(_key)


def encrypt(data: bytes) -> bytes:
    return _cipher.encrypt(data)


def decrypt(data: bytes) -> bytes:
    return _cipher.decrypt(data)
