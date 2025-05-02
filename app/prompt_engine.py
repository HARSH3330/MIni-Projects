def build_prompt(filename, content):
    return f"""
You are an AI that generates software documentation.

File Name: {filename}

Content:
{content}

Create:
- A summary of what this file does
- Function/Class Descriptions (if applicable)
- Data Dictionary (for datasets)
- Suggestions for improvements
"""
