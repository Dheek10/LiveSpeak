from audio import get_audio_stream
from vosk import Model, KaldiRecognizer
import json

model = Model("models/vosk-en")
stream = get_audio_stream()
recognizer = KaldiRecognizer(model, 16000)

while True:
    data = stream.read(4000, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        text = result.get("text", "")
        if text:
            with open("latest.txt", "w") as f:
                f.write(text)