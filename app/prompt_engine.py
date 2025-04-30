def build_prompt(filename, content):
    return f"""
You are a world-class technical documentation specialist.

Your task is to read and analyze the contents of the provided file and generate structured, professional documentation.

---
### 📄 File Information
- **File Name:** {filename}
- **File Content:** 
{content}

---

### 📜 Please generate the documentation in the following format:

1. **Overall Summary:**
   - Provide a high-level overview of what this file contains and its purpose.

2. **Detailed Sections:**
   - For source code files (.py, .js, .java, etc.):
     - List and explain each function or class.
     - For each function:
       - Name
       - Purpose (short summary)
       - Parameters (name + description)
       - Return value (if any)
   - For configuration/data files (.json, .yaml):
     - Describe the schema/structure.
     - Explain key fields and their possible values.
   - For datasets (.csv, .xlsx):
     - List all columns and provide a short description of each.
     - Highlight any missing or suspicious values if noticed.
   - For text/markdown files (.txt, .md):
     - Summarize key topics or points.
     - Identify any action items if applicable.

3. **Quality Evaluation (Optional):**
   - Is the code or data well-organized?
   - Are there any improvements or best practices that should be applied?

4. **Professional Tips (Optional):**
   - Suggest how the file can be improved for better readability, efficiency, or maintainability.
   - Recommend documentation or formatting improvements if needed.

---

### 📋 Important Instructions:
- Use clear, concise, and professional language.
- Format the output cleanly using headings, bullet points, and sub-sections.
- Ensure technical accuracy and do not hallucinate missing information.
- If a section is not applicable, clearly state "Not applicable for this file."

---
Generate the documentation now.
"""
