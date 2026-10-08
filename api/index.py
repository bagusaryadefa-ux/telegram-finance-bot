from fastapi import FastAPI, Request
from bot.handlers import process_update
from bot.config import TELEGRAM_TOKEN

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Bot is running"}

@app.post("/")
@app.post("/webhook")
@app.post("/{full_path:path}")
async def handle_telegram_update(request: Request, full_path: str = ""):
    try:
        update = await request.json()
        print(f"Received update: {update}")
        await process_update(update)
    except Exception as e:
        print(f"Error processing update: {e}")
    return {"ok": True}
