from fastapi import FastAPI
from backend.audio import get_audio_stream
from backend.asr import recognize_speech
from backend.simplifier import simplify_text
from backend.translator import translate_text

app = FastAPI()

stream = get_audio_stream()

@app.get("/caption")
def get_caption():
    try:
        with open("backend/latest.txt") as f:
            text = f.read().strip()
    except:
        text = ""

    if not text:
        return {"status": "Listening"}

    return {"text": text}