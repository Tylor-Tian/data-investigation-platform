import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import uuid
import pytest
from app.models import Investigation
from app.services.store import InvestigationStore
from app.services.auth import User
from app.services.permissions import register_permission_system
from app.services.watermark import add_watermark

class DenyAll:
    def has_access(self, user, resource, action):
        return False


def test_permission_denied():
    store = InvestigationStore()
    user = User(id=uuid.uuid4(), role="Analyst")
    register_permission_system(DenyAll())
    with pytest.raises(PermissionError):
        store.create(Investigation(title="t", created_by=user.id), user)


def test_watermark_added():
    user = User(id=uuid.uuid4(), role="Admin")
    data = add_watermark({"foo": "bar"}, user)
    assert "_watermark" in data
