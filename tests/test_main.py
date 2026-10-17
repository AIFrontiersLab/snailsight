"""Tests for Galaxy Events MVP."""
from fastapi.testclient import TestClient
from main import app, get_events

client = TestClient(app)

def test_startup():
    """Verify app starts."""
    assert app.title == "Galaxy Events"

def test_get_events_happy_path():
    """Verify 200 response with data."""
    resp = client.get("/events?region=default&intensity=1")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 1
    assert data[0]["status"] == "detected"

def test_get_events_no_results():
    """Verify 404 when no events found."""
    resp = client.get("/events?region=unknown")
    assert resp.status_code == 404

def test_get_events_invalid_region():
    """Verify 404 for invalid region."""
    resp = client.get("/events?region=void")
    assert resp.status_code == 404

def test_demo_runs():
    """Verify demo function works."""
    from main import demo
    demo()  # Should not raise