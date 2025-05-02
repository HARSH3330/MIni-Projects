from fastapi import FastAPI, UploadFile, File
from app.file_handler import parse_file
from app.prompt_engine import build_prompt
from app.llm_interface import generate_documentation
from app.doc_generator import save_markdown

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    parsed = parse_file(file.filename, content)
    prompt = build_prompt(file.filename, parsed)
    doc = generate_documentation(prompt)
    path = save_markdown(file.filename, doc)
    return {"message": "Documentation generated", "path": path}
