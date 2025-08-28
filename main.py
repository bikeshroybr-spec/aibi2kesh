from fastapi import FastAPI
from gtts import gTTS
import uvicorn
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI App is working!"}

@app.get("/text-to-speech/")
def text_to_speech(text: str):
    tts = gTTS(text)
    file_path = "output.mp3"
    tts.save(file_path)
    return {"message": f"Audio saved at {file_path}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
