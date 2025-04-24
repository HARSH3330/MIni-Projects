from langchain_ollama import OllamaEmbeddings
from config import EMBED_MODEL

def get_embedding_function():
    return OllamaEmbeddings(model=EMBED_MODEL)
