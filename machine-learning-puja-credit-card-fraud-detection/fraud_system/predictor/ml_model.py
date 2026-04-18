import joblib

artifacts = joblib.load("fraud_model.pkl")

model = artifacts["model"]
scaler = artifacts["scaler"]
feature_names = artifacts["feature_names"]