from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from chat.api.router import router as chat_router

app = FastAPI(
    title="CHAT",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)
app.include_router(chat_router)
