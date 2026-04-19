import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Path fix
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "TESLA.csv")

# Load data
df = pd.read_csv(csv_path)
df = df.dropna()

# Features (Option 2)
X = df[['Open', 'High', 'Low', 'Volume']]
y = df['Close']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Evaluation
print("MSE:", mean_squared_error(y_test, predictions))
print("R2 Score:", r2_score(y_test, predictions))

print(f"Coefficient: {model.coef_}")
print(f"Intercept: {model.intercept_}")

# Save model
model_path = os.path.join(BASE_DIR, "stock_model.pkl")
joblib.dump(model, model_path)

print("✅ Model saved successfully!")