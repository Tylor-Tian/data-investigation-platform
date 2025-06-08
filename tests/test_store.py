import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import uuid
from app.models import Investigation
from app.services.store import InvestigationStore
from app.services.auth import User


def test_create_and_get():
    store = InvestigationStore()
    user = User(id=uuid.uuid4(), role='Admin')
    inv = store.create(Investigation(title='t', created_by=user.id), user)
    fetched = store.get(inv.id, user)
    assert fetched.id == inv.id
