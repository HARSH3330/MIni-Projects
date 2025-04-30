import os

def save_markdown(filename, content):
    doc_name = filename.replace('.', '_') + "_doc.md"
    output_path = os.path.join("outputs", doc_name)
    with open(output_path, "w") as f:
        f.write(content)
    return output_path
