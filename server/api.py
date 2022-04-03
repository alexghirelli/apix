from fastapi import FastAPI
from .slack.routes import router as SlackRouter

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {
        "message": "Welcome apix!"
    }

app.include_router(SlackRouter, prefix="/api/slack") 