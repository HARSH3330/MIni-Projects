# 📊 Excel LLM Evaluator

A lightweight evaluation system that uses **G-Eval** with **Gemma 3 (via Ollama)** to assess how accurately a Large Language Model interprets and analyzes uploaded Excel files.

---

## 🎯 Objective

This tool helps validate the **interpretability and reliability** of LLM-generated insights or responses based on structured data, specifically **Excel spreadsheets**. It compares expected vs. actual outputs and scores the model's performance on various metrics.

---

## 🧠 Key Features

- ✅ Upload and process `.xlsx` or `.csv` files
- ✅ Prompt LLM (via **Ollama**) with custom tasks (e.g., "Summarize this sales data")
- ✅ Automatically evaluate:
  - ✅ Relevance
  - ✅ Accuracy
  - ✅ Completeness
  - ✅ Fluency (Optional)
- ✅ Uses **G-Eval** scoring logic with explanation
- ✅ Logs results in a structured format with traceability

---

## 🛠️ Tech Stack

- **Language:** Python
- **LLM:** Gemma 3 via Ollama
- **Framework:** G-Eval
- **File Types:** Excel (.xlsx), CSV (.csv)
- **Libraries:** Pandas, Openpyxl, LangChain, Ollama, G-Eval modules

---

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/excel-llm-evaluator.git
cd excel-llm-evaluator
```

###2. Start Ollama and load Gemma 3
```
ollama run gemma:3b
```

###3.Run the evaluation
```
python main.py --file "path/to/your/excel_file.xlsx"
```

Customization
Modify prompts/ to define your own instructions for the LLM

Tune evaluation weights in evaluation.py for custom scoring logic

🧪 Ideal Use Cases
Testing LLMs in enterprise analytics workflows

Benchmarking Excel understanding in closed-domain assistants

Verifying model-generated dashboards or reports

📬 Feedback & Contributions
We welcome suggestions and pull requests!
Let’s improve the way we evaluate LLMs on structured data — together. 🚀
