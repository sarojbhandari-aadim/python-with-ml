import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

DATA_FILE = "medical_cost_prediction_dataset.csv"
ARTIFACT_DIR = os.path.join("predictor", "ml")
ARTIFACT_PATH = os.path.join(ARTIFACT_DIR, "medical_cost_artifacts.pkl")


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()

    # Encode categorical columns
    label_encoders = {}

    cat_cols = ["gender", "smoker", "physical_activity_level", "insurance_type", "city_type"]
    for col in cat_cols:
        if col in df.columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str).str.strip())
            label_encoders[col] = le

    return df, label_encoders


def main():
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"Dataset not found: {DATA_FILE}")

    df = pd.read_csv(DATA_FILE)
    df, label_encoders = clean_dataframe(df)
    df = df.dropna().drop_duplicates()

    TARGET = "annual_medical_cost"
    X = df.drop(columns=[TARGET])
    y = df[TARGET]

    numeric_cols = [col for col in X.columns if col not in ["gender", "smoker", "physical_activity_level", "insurance_type", "city_type"]]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train_scaled = X_train.copy()
    X_test_scaled = X_test.copy()
    X_train_scaled[numeric_cols] = scaler.fit_transform(X_train[numeric_cols])
    X_test_scaled[numeric_cols] = scaler.transform(X_test[numeric_cols])

    model = RandomForestRegressor(n_estimators=300, random_state=42)
    model.fit(X_train_scaled, y_train)

    preds = model.predict(X_test_scaled)
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    print(f"MAE:  ${mae:.2f}")
    print(f"R2 Score: {r2:.4f}")

    os.makedirs(ARTIFACT_DIR, exist_ok=True)
    artifacts = {
        "model": model,
        "scaler": scaler,
        "feature_names": list(X.columns),
        "numeric_cols": numeric_cols,
        "label_encoders": label_encoders,
    }
    joblib.dump(artifacts, ARTIFACT_PATH)
    print(f"Artifacts saved to: {ARTIFACT_PATH}")


if __name__ == "__main__":
    main()
