import pandas as pd          
import numpy as np           
import pickle                
import os

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split #yesle dataset lai 2 part ma splits garxa 
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "data", "House_Rent_Dataset.csv")

df = pd.read_csv(file_path)
print("Dataset loaded successfully!")
print("Shape:", df.shape) # tdf.shape le row ra column ko number ra row dekhauxa

print(df.head())
print(df.info())

df.dropna(inplace=True) # inplace=True le naya copy nabai df lai directly modify garxa
print("\nShape after dropping NaN rows:", df.shape)

df['Posted On'] = pd.to_datetime(df['Posted On'])


df['Posted Year'] = df['Posted On'].dt.year


df['Posted Month'] = df['Posted On'].dt.month


categorical_columns = ['Area Type', 'City', 'Furnishing Status', 'Tenant Preferred', 'Point of Contact']

label_encoders = {}

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str)) # astype(str) data ma kunai pani accidental non-string values xa ki xaina ensure garxa
    label_encoders[col] = le  

print("\nCategorical columns encoded.")
print("Sample encoded data:")
print(df[categorical_columns].head(3))

feature_columns = [
    'BHK',            
    'Size',            
    'Area Type',       
    'City',             
    'Furnishing Status',
    'Tenant Preferred', 
    'Bathroom',         
    'Point of Contact', 
    'Posted Year',      
    'Posted Month',     
]

X = df[feature_columns]

y = df['Rent']

print("\nFeature matrix shape:", X.shape)
print("Target vector shape:", y.shape)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y,
    test_size=0.2,      
    random_state=42     
)

print(f"\nTraining samples: {X_train.shape[0]}")
print(f"Testing samples:  {X_test.shape[0]}")


model = RandomForestRegressor(
    n_estimators=100,   
    random_state=42,    
    n_jobs=-1          
)

print("\nTraining the model... (this may take 10-30 seconds)")
model.fit(X_train, y_train)

print("Model trained successfully!")


y_pred = model.predict(X_test)


mae = mean_absolute_error(y_test, y_pred)
r2  = r2_score(y_test, y_pred)

print(f"\nModel Evaluation on Test Set:")
print(f"  Mean Absolute Error: ₹{mae:,.0f}")
print(f"  R² Score:            {r2:.4f}")


model_data = {
    'model': model,                    
    'scaler': scaler,                   
    'label_encoders': label_encoders,   
    'feature_columns': feature_columns, 
}

model_path = os.path.join(BASE_DIR, 'model.pkl')

with open(model_path, 'wb') as f:
    pickle.dump(model_data, f)

print(f"\nModel saved to: {model_path}")
print("Training complete! You can now run the Django server.")
