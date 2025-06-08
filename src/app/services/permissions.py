from __future__ import annotations
from typing import Protocol
from .auth import User

class PermissionSystem(Protocol):
    def has_access(self, user: User, resource: str, action: str) -> bool:
        ...

default_roles = {
    "Admin": {"*": ["create", "read", "update", "delete"]},
    "Analyst": {"investigation": ["read"]},
}

class BasicPermissionSystem:
    def has_access(self, user: User, resource: str, action: str) -> bool:
        perms = default_roles.get(user.role, {})
        allowed = perms.get(resource, []) + perms.get("*", [])
        return action in allowed

_permission_provider: PermissionSystem = BasicPermissionSystem()

def register_permission_system(provider: PermissionSystem) -> None:
    global _permission_provider
    _permission_provider = provider


def get_permission_system() -> PermissionSystem:
    return _permission_provider
