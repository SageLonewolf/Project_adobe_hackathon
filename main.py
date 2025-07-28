import json
import os
from PyPDF2 import PdfReader 
import tkinter as tk
from tkinter import filedialog

def select_pdf_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    file_path = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if file_path:
        print("Selected file:", file_path)
    else:
        print("No file selected.")

def pdf_to_json(pdf_path, json_path):
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    reader = PdfReader(pdf_path)
    pdf_data = {}

    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            pdf_data[f"page_{page_num + 1}"] = text.strip()
        else:
            pdf_data[f"page_{page_num + 1}"] = ""

    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(pdf_data, json_file, indent=4, ensure_ascii=False)

pdf_file = select_pdf_file()
output_json = select_pdf_file()
pdf_to_json(pdf_file, output_json)
