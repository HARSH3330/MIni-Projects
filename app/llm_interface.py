import subprocess

def generate_documentation(prompt: str):
    result = subprocess.run(
        ["ollama", "run", "gemma:2b", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()
