import pandas as pd
from langchain_community.llms import Ollama
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

Seasonality & Events: Binary flags for holidays (e.g., Prime Day, Black Friday), seasonal spikes (e.g., Christmas), and promotional periods

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
For each channel with associated spend (e.g., search, display, social, offline), calculate ROI using:
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
def evaluate_response_gemma(prompt, response):
    eval_template = """
You are an expert evaluator tasked with analyzing the LLM's response.

Prompt:
{prompt}

LLM Response:
{response}

Evaluation Criteria:
Clarity & Structure – Is the output logically organized and easy to follow?

Accuracy – Are the insights grounded in the dataset and supported by quantitative analysis?

Channel Contribution – Are % contributions and baseline breakdowns accurate and clearly presented?

ROI Calculation – Are the ROI metrics correctly computed and meaningfully interpreted?

Strategic Insights – Are the recommendations actionable, relevant, and supported by the data?

Seasonality & External Factors – Is there a meaningful assessment of events, inflation, or promotions?

Executive Readability – Could this report be used in a CMO-level meeting?

Provide a score from 1 to 10 for each of these criteria, followed by a detailed explanation of your reasoning for each score.
"""
    
    return eval_template.format(prompt=prompt, response=response)

# Main Function
def main():
    file_path = r"C:\Users\670336314\Downloads\Final_Model_Input_File_corrected 3 - Copy.xlsx"  # Change to your Excel file path
    llm = Ollama(model="gemma3:1b")

    # Step 1: Load Data
    df = load_excel(file_path)

    # Step 2: Generate Prompt & Get LLM Analysis
    analysis_prompt = create_analysis_prompt(df)
    analysis_result = llm.invoke(analysis_prompt)

    print("📊 Analysis Result:")
    print(analysis_result)

    # Step 3: Evaluate the Response
    evaluation_prompt = evaluate_response_gemma(analysis_prompt, analysis_result)
    evaluation_result = llm.invoke(evaluation_prompt)

    print("\n🧠 Evaluation Result:")
    print(evaluation_result)

    # Step 4: Save Results
    with open(f"results/eval_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt", "w") as f:
        f.write("=== Analysis Prompt ===\n")
        f.write(analysis_prompt + "\n\n")
        f.write("=== LLM Response ===\n")
        f.write(analysis_result + "\n\n")
        f.write("=== Evaluation Result ===\n")
        f.write(evaluation_result)

if __name__ == "__main__":
    main()
