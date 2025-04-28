# 🍽️ RAG System for Restaurant Dataset

A Retrieval-Augmented Generation (RAG) chatbot designed to answer restaurant-related queries by leveraging a structured restaurant dataset and the power of modern Large Language Models (LLMs).

---

## 🎯 Objective

The goal is to build a chatbot that can provide accurate, context-grounded answers by retrieving relevant information from a restaurant dataset and generating human-like responses using an LLM.

---

## 🛠️ Tech Stack

- **Backend Framework:** Python
- **Retrieval Engine:** LangChain + ChromaDB
- **Language Model:** Gemma 3 via Ollama
- **Data Source:** Structured restaurant CSV/Excel files
- **Evaluation:** Custom LLM evaluation system for output quality analysis

---

## 📚 Key Features

- 🔎 Intelligent retrieval from structured restaurant information
- 💬 Context-grounded, natural language responses via Gemma 3
- 🧠 Integrated evaluation module to log:
  - Expected output
  - Actual model output
  - Scoring
  - Explanation of discrepancies
- 🗂️ Modular code for easy dataset swapping and LLM fine-tuning

---



---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/restaurant-rag-bot.git
cd restaurant-rag-bot
```

### 2.Start Ollama and Load Gemma 3
```
ollama run gemma:3b
```

### 3.Run the Bot
```
python main.py
```

Evaluation Example
After each query, the system automatically evaluates the LLM's answer:
```
✅ Evaluation Completed
Expected Answer: "The best-rated Italian restaurant is Pasta Palace."
Actual Answer: "Pasta Palace is known for top Italian cuisine."
Score: 4.7 / 5.0
Explanation: The response matches the expected restaurant but adds slight elaboration.
```





