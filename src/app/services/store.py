from typing import Dict, List
from uuid import UUID
from .auth import User
from ..models import Investigation
from .permissions import get_permission_system
from .encryption import encrypt, decrypt

class InvestigationStore:
    def __init__(self):
        self._store: Dict[UUID, bytes] = {}

    def create(self, inv: Investigation, user: User) -> Investigation:
        if not get_permission_system().has_access(user, "investigation", "create"):
            raise PermissionError("access denied")
        self._store[inv.id] = encrypt(inv.json().encode())
        return inv

    def get(self, inv_id: UUID, user: User) -> Investigation | None:
        if inv_id not in self._store:
            return None
        if not get_permission_system().has_access(user, "investigation", "read"):
            raise PermissionError("access denied")
        data = decrypt(self._store[inv_id])
        return Investigation.parse_raw(data)

    def list(self, user: User) -> List[Investigation]:
        if not get_permission_system().has_access(user, "investigation", "read"):
            raise PermissionError("access denied")
        return [Investigation.parse_raw(decrypt(item)) for item in self._store.values()]
