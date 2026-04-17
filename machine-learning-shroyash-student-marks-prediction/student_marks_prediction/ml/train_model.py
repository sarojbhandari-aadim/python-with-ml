

import os
import pickle
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "Student_Performance.csv")
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")

CHARTS_DIR = os.path.join(BASE_DIR, "..", "predictor", "static", "predictor", "charts")
os.makedirs(CHARTS_DIR, exist_ok=True)


df = pd.read_csv(DATA_PATH)

print(f"Shape: {df.shape}")
print(df.head())

df.columns = [col.strip().replace(" ", "_") for col in df.columns]

print("Missing values:\n", df.isnull().sum())
df.dropna(inplace=True)

# Encode categorical column
if "Extracurricular_Activities" in df.columns:
    df["Extracurricular_Activities"] = df["Extracurricular_Activities"].map({"Yes": 1, "No": 0})

print(df.dtypes)


# Chart 1: Hours Studied vs Performance
fig, ax = plt.subplots()
ax.scatter(df["Hours_Studied"], df["Performance_Index"], alpha=0.5)

m, b = np.polyfit(df["Hours_Studied"], df["Performance_Index"], 1)
x = np.linspace(df["Hours_Studied"].min(), df["Hours_Studied"].max(), 100)
ax.plot(x, m*x + b, color="red")

ax.set_title("Hours Studied vs Performance")
ax.set_xlabel("Hours Studied")
ax.set_ylabel("Performance Index")

plt.savefig(os.path.join(CHARTS_DIR, "hours_vs_performance.png"))
plt.close()

# Chart 2: Previous Scores vs Performance (FIXED instead of Attendance)
fig, ax = plt.subplots()
ax.scatter(df["Previous_Scores"], df["Performance_Index"], alpha=0.5)

m, b = np.polyfit(df["Previous_Scores"], df["Performance_Index"], 1)
x = np.linspace(df["Previous_Scores"].min(), df["Previous_Scores"].max(), 100)
ax.plot(x, m*x + b, color="green")

ax.set_title("Previous Scores vs Performance")
ax.set_xlabel("Previous Scores")
ax.set_ylabel("Performance Index")

plt.savefig(os.path.join(CHARTS_DIR, "scores_vs_performance.png"))
plt.close()

FEATURES = [
    "Hours_Studied",
    "Previous_Scores",
    "Sleep_Hours",
    "Sample_Question_Papers_Practiced",
    "Extracurricular_Activities"
]

TARGET = "Performance_Index"

df_model = df[FEATURES + [TARGET]].dropna()

X = df_model[FEATURES].values
y = df_model[TARGET].values

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

print(f"\nTraining: {len(X_train)} | Testing: {len(X_test)}")

models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        max_depth=10,
        random_state=42
    )
}

results = {}

print("\n🤖 Training models...")

for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    r2 = r2_score(y_test, preds)
    mae = mean_absolute_error(y_test, preds)

    results[name] = {"model": model, "r2": r2, "mae": mae}

    print(f"\n{name}")
    print(f"R2: {r2:.4f}")
    print(f"MAE: {mae:.4f}")


best_name = max(results, key=lambda k: results[k]["r2"])
best_model = results[best_name]["model"]

print(f"\n🏆 Best Model: {best_name}")

with open(MODEL_PATH, "wb") as f:
    pickle.dump(best_model, f)

with open(SCALER_PATH, "wb") as f:
    pickle.dump(scaler, f)

p