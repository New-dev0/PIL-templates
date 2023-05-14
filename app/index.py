import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()

@app.get("/")
async def Index():
    return {}

PORT = int(os.getenv("PORT", 8000))
uvicorn.run(app, port=PORT)