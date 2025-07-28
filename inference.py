import fitz
import json
import joblib
from features import extract_features
from data_preparation import extract_spans

def process_pdf(pdf_path):
    clf = joblib.load("model/classifier.pkl")
    scaler = joblib.load("model/scaler.pkl")
    spans = extract_spans(pdf_path)

    results = []
    title = ""
    for span in spans:
        feats = extract_features(span)
        X = scaler.transform([list(feats.values())])
        pred = clf.predict(X)[0]

        if pred == "Title" and not title:
            title = span["text"]
        elif pred in {"H1", "H2", "H3", "H4"}:
            results.append({
                "level": pred,
                "text": span["text"],
                "page": span["page"]
            })

    return {
        "title": title,
        "outline": results
    }
