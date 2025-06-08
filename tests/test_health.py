import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from app.main import app

client = app.test_client()


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}
