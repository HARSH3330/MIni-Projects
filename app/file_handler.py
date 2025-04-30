import pandas as pd
import json
import os

def parse_file(file_path):
    ext = os.path.splitext(file_path)[1]
    
    if ext == ".csv":
        df = pd.read_csv(file_path)
        return df.head().to_string()
    elif ext == ".xlsx":
        df = pd.read_excel(file_path)
        return df.head().to_string()
    elif ext == ".json":
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return json.dumps(data, indent=2)
    elif ext in [".txt", ".md", ".py"]:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        return "Unsupported file type."
