import os
import joblib
import pandas as pd
from django.shortcuts import render
from pathlib import Path

# Build paths inside the project. BASE_DIR is webapp/predictor/
# PROJECT_ROOT is the root of the entire repository
BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent.parent

# Load model and scaler using absolute paths from the root models directory
MODEL_PATH = PROJECT_ROOT / 'models' / 'churn_model.pkl'
SCALER_PATH = PROJECT_ROOT / 'models' / 'scaler.pkl'

# Load artifacts
# Use try-except to handle cases where models might not be trained yet
try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
except Exception as e:
    print(f"Error loading model/scaler: {e}")
    model = None
    scaler = None

def home(request):
    if request.method == 'POST':
        # Get data from form
        gender = request.POST.get('gender')
        senior = request.POST.get('senior') # Now expected as "Yes"/"No"
        partner = request.POST.get('partner')
        dependents = request.POST.get('dependents')
        tenure = int(request.POST.get('tenure'))
        phone = request.POST.get('phone')
        paperless = request.POST.get('paperless')
        monthly = float(request.POST.get('monthly'))
        total = float(request.POST.get('total'))

        # Prepare raw data dictionary
        data = {
            'gender': gender,
            'SeniorCitizen': 1 if senior == 'Yes' else 0,
            'Partner': partner,
            'Dependents': dependents,
            'tenure': tenure,
            'PhoneService': phone,
            'PaperlessBilling': paperless,
            'MonthlyCharges': monthly,
            'TotalCharges': total
        }

        df = pd.DataFrame([data])

        # Encoding categorical features
        df['gender'] = df['gender'].map({'Male': 0, 'Female': 1})
        df['Partner'] = df['Partner'].map({'No': 0, 'Yes': 1})
        df['Dependents'] = df['Dependents'].map({'No': 0, 'Yes': 1})
        df['PhoneService'] = df['PhoneService'].map({'No': 0, 'Yes': 1})
        df['PaperlessBilling'] = df['PaperlessBilling'].map({'No': 0, 'Yes': 1})

        # Ensure all columns expected by the model are present
        if model:
            try:
                model_features = model.feature_names_in_
            except AttributeError:
                # Fallback if model was trained on numpy array
                model_features = [
                    'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
                    'PhoneService', 'PaperlessBilling', 'MonthlyCharges', 'TotalCharges'
                ]
            
            for col in model_features:
                if col not in df.columns:
                    df[col] = 0
            
            # Reorder columns to match model training
            df = df[model_features]

            # CRITICAL: Apply Scaling
            if scaler:
                df_scaled = pd.DataFrame(scaler.transform(df), columns=model_features)
                prediction = model.predict(df_scaled)
                prob = model.predict_proba(df_scaled)[0][1]
            else:
                # Fallback if scaler is missing (less accurate)
                prediction = model.predict(df)
                prob = model.predict_proba(df)[0][1]

            result = "Customer likely to Churn" if prediction[0] == 1 else "Customer likely to Stay"
            prob_percent = round(prob * 100, 2)
        else:
            result = "Error: Model not loaded."
            prob_percent = 0

        return render(request, 'index.html', {
            'result': result,
            'prob': f"{prob_percent}%",
            'raw_data': data # For debugging if needed
        })

    return render(request, 'index.html')