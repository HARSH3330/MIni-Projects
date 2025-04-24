# 🧠 Internal Knowledge Base Q&A Bot

A smart chatbot powered by **Gemma 3 via Ollama** that helps employees navigate company policy documents with ease. This Retrieval-Augmented Generation (RAG) system enables natural language Q&A over categorized internal policies and documents.

---

## 🎯 Goal

To create an internal, secure, and intelligent chatbot that:
- Understands natural questions from employees
- Retrieves accurate information from internal policy files
- Enhances productivity and reduces manual HR queries

---

## 🚀 Current Status

🔄 **In Progress**  
- ✅ Document ingestion and vectorization module completed  
- 🛠️ Retrieval and response generation pipeline under development  
- 🧩 Integration with company policy JSON files in progress  

---

## 🛠️ Tech Stack

- **LLM:** Gemma 3 (via Ollama)
- **Framework:** LangChain
- **Vector Store:** Chroma DB
- **Language:** Python
- **File Format:** Structured JSON policy documents

---


---

## 🔍 How It Works

1. **Document Loader:** Parses and categorizes structured policy files  
2. **Vectorization:** Embeds content using Ollama-powered Gemma 3 LLM  
3. **Retrieval:** Uses semantic search to find relevant chunks  
4. **Answering:** Responds to user queries using RAG pipeline

---

## 🧪 Example Use Cases

- _“How many days of paid leave are allowed per year?”_  
- _“What is the company policy on remote work?”_  
- _“Who should I contact for IT equipment reimbursement?”_

---

## 📦 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/your-username/knowledge-bot.git
cd knowledge-bot

# Install dependencies
pip install -r requirements.txt

# Run the chatbot
python main.py


