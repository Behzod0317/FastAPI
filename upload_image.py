from fastapi import FastAPI, File, UploadFile
import os

app = FastAPI()
UPLOAD_FOLDER = "uploads"



@app.post("/upload")
async def upload_file(file: UploadFile):
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    file.filename = file.filename.replace("/", "")

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as f:

        f.write(await file.read())
    return {"filename": file.filename}



@app.get("/{filename}")
async def get_file(filename: str):
    return {"file_url": "/" + UPLOAD_FOLDER + "/" + filename}
