from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_websocket_endpoint():
    # test websocket endpoint
    pass