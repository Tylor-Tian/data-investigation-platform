import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from app.models import Investigation
from uuid import uuid4


def test_model_defaults():
    inv = Investigation(title='x', created_by=uuid4())
    assert inv.status == 'active'
    assert inv.id
