import os

# Base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(BASE_DIR, "Signify_pol")  # Folder with category-wise JSON policies
FAISS_INDEX_PATH = os.path.join(BASE_DIR, "faiss_index")  # Where to save the FAISS index

# Models
EMBED_MODEL = "nomic-embed-text"  # Or "gemma:2b" or anything available in your Ollama
LLM_MODEL = "gemma3:1b"
