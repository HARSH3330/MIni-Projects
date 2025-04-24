from langchain_community.vectorstores import FAISS
from config import FAISS_INDEX_PATH
from loader import load_policy_documents
from embedder import get_embedding_function

def create_vectorstore():
    docs = load_policy_documents()
    embedding = get_embedding_function()
    vectordb = FAISS.from_documents(docs, embedding)
    vectordb.save_local(FAISS_INDEX_PATH)
    print(f"✅ FAISS index saved to: {FAISS_INDEX_PATH}")

if __name__ == "__main__":
    create_vectorstore()
