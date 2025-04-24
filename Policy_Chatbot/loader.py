import os
import json
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import DATA_FOLDER

def load_policy_documents():
    docs = []
    for root, dirs, files in os.walk(DATA_FOLDER):
        for file in files:
            if file.endswith(".json"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list):  # List of policy entries
                        for entry in data:
                            content = entry.get("content", "")
                            if content:
                                docs.append(Document(page_content=content, metadata={"source": file}))
                    elif isinstance(data, dict):  # Single policy dict
                        content = data.get("content", "")
                        if content:
                            docs.append(Document(page_content=content, metadata={"source": file}))

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_docs = splitter.split_documents(docs)

    print(f"✅ Loaded {len(docs)} documents and split into {len(split_docs)} chunks from '{DATA_FOLDER}'")
    return split_docs

if __name__ == "__main__":
    load_policy_documents()
