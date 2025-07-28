# 📘 PDF Outline & Title Extractor (Adobe Hackathon 2025)

This project uses a Machine Learning pipeline to extract a structured outline (`H1`, `H2`, etc.) and document title from PDF files. It is designed to handle a wide range of documents — from highly structured reports to simple flyers and forms.

---

## 🚀 Features

-  ML-based heading classification (`Title`, `H1`, `H2`, `H3`, `H4`)
-  JSON output schema as per challenge requirement
-  Dockerized for easy reproducibility and submission
-  Works on real-world noisy PDFs

---

## 🧾 JSON Output Schema

{
  "title": "Document Title",
  "outline": [
    {
      "level": "H1",
      "text": "Section Heading",
      "page": 1
    }
  ]
}


Project Structure

.
├── input/             # Put your PDFs here for inference
├── output/            # JSON output appears here
├── training_pdfs/     # Labeled PDFs for training
├── training_labels/   # JSONs with title + outline for training
├── model/             # Trained model files (.pkl)
├── train.py           # Train model on labeled data
├── app.py             # Run inference on input/
├── inference.py       # Inference logic (ML + fallback)
├── data_preparation.py# Preprocessing and labeling
├── features.py        # Feature engineering
├── Dockerfile         # Container for full pipeline
└── README.md          # This file

Requirements:
Python 3.10+

Acknowledgements:
Built for Adobe India Hackathon 2025
Model trained on real and synthetic documents using RandomForestClassifier.