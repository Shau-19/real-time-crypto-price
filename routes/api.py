from fastapi import APIRouter, WebSocket
from pydantic import BaseModel
from models import CryptoPrice

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.websocket("/ws")
def websocket_endpoint(websocket: WebSocket):
    while True:
        data = websocket.receive_text()
        req: ChatRequest = ChatRequest.parse_raw(data)
        # handle message
        websocket.send_text(f"Message: {req.message}")