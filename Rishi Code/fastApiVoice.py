from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import File,UploadFile
from fastapi.responses import HTMLResponse
import speech_recognition as sr
from mlModels import voiceTtext, classifier
from typing import List
import uvicorn
from sklearn.feature_extraction.text import CountVectorizer
import pymongo

client = pymongo.MongoClient("mongodb+srv://RiXiRx:tAf1t7vjsGbRsPMN@cluster0.rrhdn.mongodb.net/")
db = client['MakeHarvard']
resList = db['resList']

app = FastAPI()

@app.post("/voice/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    text=[]
    cls = []
    for File in files:
        text.append(voiceTtext(File.file))
        cls.append(classifier(text))
    try:
        resList.insert_one({"text":text[0],"cls":cls})
        print("data uploaded")
    except:
        print("Error")
    dct = {"text":text[0],"cls":cls[0]}
    jsonData = jsonable_encoder(dct)
    return JSONResponse(content = jsonData)


@app.get("/file")
async def file():
    content = """
<body>
<form action="/voice/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

@app.get("/")
async def slash():
    return "Hello world"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)