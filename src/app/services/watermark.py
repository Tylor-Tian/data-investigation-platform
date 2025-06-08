from __future__ import annotations
from hashlib import sha1
from .auth import User


def add_watermark(data: dict, user: User) -> dict:
    mark = sha1(str(user.id).encode()).hexdigest()
    data = dict(data)
    data["_watermark"] = mark
    return data
