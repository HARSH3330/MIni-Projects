import pandas as pd
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from datetime import datetime

# Load Excel File
def load_excel(file_path):
    df = pd.read_excel(file_path)
    return df

# Generate Prompt for Marketing Mix Modeling (MMM)
def create_analysis_prompt(df):
    preview = df.head(5).to_string()  # Showing 5 rows to give a better context for analysis
    return f"""
You are a data scientist specializing in advanced Marketing Mix Modeling (MMM).
You have been provided with a structured Excel dataset containing weekly-level data with the following types of variables:

Dependent Variable: Weekly sales (e.g., HUE_SALES)

Marketing Channels: Spend, impressions, clicks across search, social, display, promotions, and traditional media

Seasonality & Events: Binary flags for holidays (e.g., Prime Day, Black Friday), seasonal spikes (e.g., Christmas), and promotional periods dont just stick to these but check for others also from the dataset

External Variables: Inflation rates, pricing indices, discount levels

Time Identifiers: Year, week number, date
{preview}
 
Your Tasks:
📈 1. Identify Key Sales Drivers
Determine which variables most strongly influence weekly sales.

Differentiate between incremental marketing impact and baseline sales (sales that would occur without marketing).

📊 2. Calculate Channel Contribution (%)
Break down the sales into:

Baseline Sales

Incremental Sales from each Marketing Channel

Report this as a percentage contribution to total sales for each.

💸 3. Compute ROI (Return on Investment)
For each channel with associated spend and calculate ROI using:
ROI = Incremental Sales / Spend

Highlight any underperforming or inefficient channels.

📅 4. Detect Seasonality & External Effects
Highlight any time-based patterns or events that consistently lead to sales spikes or drops.

Discuss how inflation or discounts affect overall sales behavior.

🧠 5. Provide Strategic Insights
What are the top 3 most effective marketing levers to focus on?

Which areas should be reduced, paused, or reallocated based on diminishing returns or poor ROI?

📌 6. Deliver an Executive Summary
Present your insights in a structured, bullet-point summary.

Focus on action-oriented recommendations that a CMO or VP of Marketing could use for media planning and strategy.


"""

# Generate Evaluation Prompt (G-Eval Style) for MMM Analysis
def evaluate_response_gemma(full_chat_history):
    return f"""You are an expert evaluator tasked with analyzing the LLM's response.

Complete Conversation:
{full_chat_history}

Evaluation Criteria:
- Clarity & Structure
- Accuracy
- Channel Contribution
- ROI Calculation
- Strategic Insights
- Seasonality & External Factors
- Executive Readability

Score each from 1–10 with detailed reasoning.
"""

# Main Function
def main():
    file_path = r"C:\Users\670336314\Downloads\Final_Model_Input_File_corrected 3 - Copy.xlsx"  # Change to your Excel file path
    llm = OllamaLLM(model="gemma3:1b")

    # Step 1: Load Data
    df = load_excel(file_path)

    # Step 2: Generate Prompt & Get LLM Analysis
    analysis_prompt = create_analysis_prompt(df)
    full_chat_history = f"User: {analysis_prompt.strip()}\n"
    analysis_response = llm.invoke(analysis_prompt)
    full_chat_history += f"Gemma: {analysis_response.strip()}\n"

    print("\n📊 Initial Analysis:\n")
    print(analysis_response)

    # Interactive follow-up
    while True:
        user_input = input("\n💬 Ask a follow-up question or type 'EVALUATE' to score the full conversation:\n")

        if user_input.strip().upper() == "EVALUATE":
            evaluation_prompt = evaluate_response_gemma(full_chat_history)
            evaluation_result = llm.invoke(evaluation_prompt)
            print("\n🧠 Evaluation Result:\n")
            print(evaluation_result)
            break

        # Otherwise, continue chat
        full_chat_history += f"User: {user_input.strip()}\n"
        followup_response = llm.invoke(user_input)
        full_chat_history += f"Gemma: {followup_response.strip()}\n"
        print("\n🔁 Gemma's Answer:\n")
        print(followup_response)

if __name__ == "__main__":
    main()

  
