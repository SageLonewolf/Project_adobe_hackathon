import os, json
import joblib
from data_preparation import extract_spans, load_ground_truth, match_and_label
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

def train_model(pdf_dir, json_dir):
    X, y = [], []
    for file in os.listdir(pdf_dir):
        if not file.endswith(".pdf"):
            continue
        pdf_path = os.path.join(pdf_dir, file)
        json_path = os.path.join(json_dir, file.replace(".pdf", ".json"))
        gt = load_ground_truth(json_path)
        spans = extract_spans(pdf_path)
        labeled = match_and_label(spans, gt["outline"], gt["title"])
        for feats, label in labeled:
            X.append(list(feats.values()))
            y.append(label)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_scaled, y)

    os.makedirs("model", exist_ok=True)
    joblib.dump(clf, "model/classifier.pkl")
    joblib.dump(scaler, "model/scaler.pkl")
    print("✅ Model trained and saved to model/")

if __name__ == "__main__":
    train_model("training_pdfs", "training_labels")
