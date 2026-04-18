import os
import joblib
import pandas as pd
from django.conf import settings

ARTIFACT_PATH = os.path.join(settings.BASE_DIR, "predictor", "ml", "medical_cost_artifacts.pkl")

if not os.path.exists(ARTIFACT_PATH):
    raise FileNotFoundError(
        "Model artifact not found. Run 'python train_model.py' first."
    )

artifacts = joblib.load(ARTIFACT_PATH)
model = artifacts["model"]
scaler = artifacts["scaler"]
feature_names = artifacts["feature_names"]
numeric_cols = artifacts["numeric_cols"]
label_encoders = artifacts["label_encoders"]


def preprocess_input(input_data: dict) -> pd.DataFrame:
    row = input_data.copy()

    # Apply label encoders for categorical fields
    for col, le in label_encoders.items():
        if col in row:
            val = str(row[col]).strip()
            if val in le.classes_:
                row[col] = le.transform([val])[0]
            else:
                row[col] = 0  # fallback

    df = pd.DataFrame([row], columns=feature_names)
    df[numeric_cols] = scaler.transform(df[numeric_cols])
    return df


def predict_medical_cost(input_data: dict) -> dict:
    processed = preprocess_input(input_data)
    predicted_cost = float(model.predict(processed)[0])

    return {
        "predicted_cost": round(predicted_cost, 2),
        "predicted_cost_formatted": f"${predicted_cost:,.2f}",
    }
