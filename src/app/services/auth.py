from uuid import UUID, uuid4
from flask import abort
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: UUID
    role: str

# Dummy user store
_users = {
    uuid4(): User(id=uuid4(), role="Admin")
}

def get_current_user() -> User:
    # In real scenario, decode token etc.
    # Here we return a static admin user for simplicity
    user = next(iter(_users.values()))
    if not user:
        abort(401)
    return user
