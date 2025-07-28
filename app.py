import os, json
from inference import process_pdf

INPUT_DIR = "input"
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

for file in os.listdir(INPUT_DIR):
    if not file.endswith(".pdf"):
        continue
    pdf_path = os.path.join(INPUT_DIR, file)
    output_path = os.path.join(OUTPUT_DIR, file.replace(".pdf", ".json"))
    result = process_pdf(pdf_path)
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"✅ Processed: {file} -> {output_path}")
