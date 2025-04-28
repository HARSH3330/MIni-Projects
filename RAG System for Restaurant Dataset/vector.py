from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
import os
import pandas as pd

# Load your CSV
df = pd.read_csv(r"C:\Users\670336314\OneDrive - Signify\Desktop\Local AI agent\realistic_restaurant_reviews.csv")

# Initialize embedding model
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Directory to store FAISS index
db_location = "faiss_index"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    for i, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + " " + row["Review"],
            metadata={"rating": row["Rating"], "date": row["Date"]}
        )
        documents.append(document)

    # Create FAISS vector store and save it
    vector_store = FAISS.from_documents(documents, embedding=embeddings)
    vector_store.save_local(db_location)
else:
    # Load existing FAISS index
    vector_store = FAISS.load_local(db_location, embeddings, allow_dangerous_deserialization=True)


# Get retriever from the vector store
retriever = vector_store.as_retriever(search_kwargs={"k": 5})
