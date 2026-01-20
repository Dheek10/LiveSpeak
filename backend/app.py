from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import threading
import time

from backend.audio import get_audio_stream
from backend.asr import recognize_speech
from backend.simplifier import simplify_text
from backend.translator import translate_text

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

stream = get_audio_stream()

def start_asr():
    recognize_speech(stream)

# start speech recognition in background
threading.Thread(target=start_asr, daemon=True).start()

@app.get("/caption")
def get_caption():
    try:
        with open("backend/latest.txt", "r", encoding="utf-8") as f:
            text = f.read().strip()
    except:
        text = ""

    if not text:
        return {"status": "Listening"}

    return {
        "original": text,
        "translated": translate_text(text, "de")
    }