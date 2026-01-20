import json
import time
from vosk import Model, KaldiRecognizer

# Load model ONCE
model = Model("backend/models/vosk-en")

def recognize_speech(stream, timeout=10):
    recognizer = KaldiRecognizer(model, 16000)

    start_time = time.time()

    while True:
        if time.time() - start_time > timeout:
            return None

        data = stream.read(4000, exception_on_overflow=False)

        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            return result.get("text")