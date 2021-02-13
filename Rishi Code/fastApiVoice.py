from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import File,UploadFile
import speech_recognition as sr
from mlModels import voiceTtext

app = FastAPI()

@app.post("/voice")
async def voice_Data(fileVoice : UploadFile = File(...)):
    text = voiceTtext(fileVoice.file)