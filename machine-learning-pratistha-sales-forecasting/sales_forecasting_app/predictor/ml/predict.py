import os
import joblib
import pandas as pd
from django.conf import settings

MODEL_PATH = os.path.join(
    settings.BASE_DIR,
    "sales_forecasting_app",
    "predictor",
    "ml",
    "model.pkl"
)

artifacts = joblib.load(MODEL_PATH)

model = artifacts["model"]
feature_names = artifacts["feature_names"]

def predict_sales(data: dict):
    df = pd.DataFrame([data])


    for col in feature_names:
        if col not in df.columns:
            df[col] = 0

    df = df[feature_names]

    prediction = model.predict(df)[0]

    return round(float(prediction), 2)