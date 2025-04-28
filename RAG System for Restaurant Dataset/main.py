import os
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever  # Ensure vector.py defines and exports 'retriever'
from evaluation import evaluate_response, save_result  # Make sure both functions are in evaluation.py

# Load model
model = OllamaLLM(model="gemma3:1b")  # or "gemma:3b" if you're using Gemma

# Prompt template
template = """
You are an expert in answering questions about a pizza restaurant.

Here are some relevant reviews:
{reviews}

Here is the question to answer:
{question}
"""

# Setup prompt chain
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Ensure results directory exists
os.makedirs("results", exist_ok=True)

# Start interactive Q&A loop
while True:
    print("\n\n-------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question.lower() == "q":
        break

    # 1. Retrieve context from vector DB
    documents = retriever.invoke(question)
    reviews_text = "\n".join([doc.page_content for doc in documents])

    # 2. Run LLM with context
    llm_response = chain.invoke({"reviews": reviews_text, "question": question})
    print(f"LLM Response:\n{llm_response}\n")

    # 3. Ask for expected output
    expected_output = input("Enter the expected answer for evaluation: ")

    # 4. Evaluate the response
    eval_result = evaluate_response(question, expected_output, llm_response)
    print("Evaluation Result:\n", eval_result)

    # 5. Save result
    save_result(
        inputs={
            "statement": question,
            "expected": expected_output,
            "actual": llm_response
        },
        response=eval_result
    )
    print("✅ Evaluation saved to results folder.")
