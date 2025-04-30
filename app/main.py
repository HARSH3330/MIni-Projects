from fastapi import FastAPI, UploadFile, File
import shutil
import os
from app.file_handler import parse_file
from app.llm_interface import generate_documentation

app = FastAPI()

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    content = parse_file(file_location)
    documentation = generate_documentation(file.filename, content)

    output_file_path = os.path.join(OUTPUT_FOLDER, file.filename + "_documentation.md")
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(documentation)

    return {"message": "Documentation generated", "output_file": output_file_path}
