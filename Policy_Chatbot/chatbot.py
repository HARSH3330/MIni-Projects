from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_ollama import OllamaLLM  # Updated Ollama import
from embedder import get_embedding_function
from config import FAISS_INDEX_PATH, LLM_MODEL

def run_chatbot():
    try:
        # Load embedding function and vector store
        embedding = get_embedding_function()
        vectordb = FAISS.load_local(FAISS_INDEX_PATH, embeddings=embedding, allow_dangerous_deserialization=True)
        retriever = vectordb.as_retriever(search_type="similarity", k=5 )

        # Load LLM
        llm = OllamaLLM(model=LLM_MODEL)

        # Build RetrievalQA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True
        )

        print("💬 Company Policy Chatbot (type 'exit' to quit)")

        while True:
            query = input("You: ")
            if query.lower() in ["exit", "quit"]:
                print("👋 Goodbye!")
                break

            response = qa_chain({"query": query})
            print("\n🤖 Answer:", response["result"])
            print("📄 Source(s):", [doc.metadata.get("source", "Unknown") for doc in response["source_documents"]])
            print("-" * 50)

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    run_chatbot()
