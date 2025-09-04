from fastapi import APIRouter, WebSocket

router = APIRouter()

CLIENTS: list[WebSocket] = []

@router.websocket("/ws")
async def ws_chat(websocket: WebSocket):
    await websocket.accept()
    CLIENTS.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for client in CLIENTS:
                await client.send_text(f"{data}")
    except:
        CLIENTS.remove(websocket)