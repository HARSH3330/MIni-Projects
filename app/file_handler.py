import pandas as pd
import json

def parse_file(filename, content):
    if filename.endswith(".py"):
        return content.decode()
    elif filename.endswith(".json"):
        return json.dumps(json.loads(content), indent=2)
    elif filename.endswith(".csv"):
        df = pd.read_csv(pd.compat.StringIO(content.decode()))
        return df.head().to_markdown()
    elif filename.endswith(".txt") or filename.endswith(".md"):
        return content.decode()
    else:
        return "Unsupported file type."

