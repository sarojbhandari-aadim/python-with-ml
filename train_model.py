import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

def train():
    if not os.path.exists("yield_df.csv"):
        print("Error: yield_df.csv not found!")
        return
        
    df = pd.read_csv("yield_df.csv")
    
    # 1. Manual Encoding: Convert Text (Area/Item) into Numbers
    # We use get_dummies because it's the standard way to handle categorical data
    df_encoded = pd.get_dummies(df, columns=['Area', 'Item'])
    
    # 2. Define Features (X) and Target (y)
    X = df_encoded.drop('hg/ha_yield', axis=1)
    y = df_encoded['hg/ha_yield']

    # 3. Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Manual Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 5. Train Model
    print("Training Random Forest... this might take a minute.")
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # 6. Get Accuracy Score
    score = model.score(X_test_scaled, y_test)
    print(f"📊 Model Accuracy (R2 Score): {round(score * 100, 2)}%")
    
    # 7. Save BOTH the model and the scaler
    # Since we scaled manually, we need to save the scaler to use it in the website!
    os.makedirs("predictor/ml", exist_ok=True)
    joblib.dump(model, "predictor/ml/crop_yield_model.pkl")
    joblib.dump(scaler, "predictor/ml/scaler.pkl")
    joblib.dump(X.columns.tolist(), "predictor/ml/model_columns.pkl") # Save column names
    
    print("Success! Files saved in predictor/ml/")

if __name__ == "__main__":
    train()