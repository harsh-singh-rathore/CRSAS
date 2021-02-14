from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import File,UploadFile
from fastapi.responses import HTMLResponse
import speech_recognition as sr
from mlModels import voiceTtext
from typing import List
import uvicorn

app = FastAPI()

@app.post("/voice/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    text=[]
    for File in files:
        text.append(voiceTtext(File.file))
    dct = {"output":text}
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