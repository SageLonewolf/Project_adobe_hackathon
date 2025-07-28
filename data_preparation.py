import os, json
import fitz  
from features import extract_features

def load_ground_truth(json_path):
    with open(json_path) as f:
        return json.load(f)

def extract_spans(pdf_path):
    doc = fitz.open(pdf_path)
    all_spans = []
    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    all_spans.append({
                        "text": span["text"].strip(),
                        "size": span["size"],
                        "flags": span["flags"],
                        "page": page_num,
                        "x": span["bbox"][0],
                        "y": span["bbox"][1],
                    })
    return all_spans

def match_and_label(spans, gt_outline, gt_title):
    labeled = []
    for span in spans:
        label = "Other"
        if span["text"].strip() == gt_title.strip():
            label = "Title"
        for item in gt_outline:
            if span["text"].strip() == item["text"].strip() and span["page"] == item["page"]:
                label = item["level"]
                break
        labeled.append((extract_features(span), label))
    return labeled
