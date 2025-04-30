from app.prompt_engine import build_prompt
import subprocess

def query_ollama(prompt):
    result = subprocess.run(
        ["ollama", "run", "gemma3:1b", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout

def generate_documentation(filename, content):
    prompt = build_prompt(filename, content)
    documentation = query_ollama(prompt)
    return documentation
