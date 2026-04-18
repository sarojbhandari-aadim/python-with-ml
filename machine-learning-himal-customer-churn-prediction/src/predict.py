import joblib
import pandas as pd

def predict():
    # Load trained model
    model = joblib.load('models/churn_model.pkl')
    scaler = joblib.load('models/scaler.pkl')

    print("\nEnter customer details:")

    gender = input("Gender (Male/Female): ")
    senior = int(input("Senior Citizen (0/1): "))
    partner = input("Partner (Yes/No): ")
    dependents = input("Dependents (Yes/No): ")
    tenure = int(input("Tenure (months): "))
    phone = input("Phone Service (Yes/No): ")
    paperless = input("Paperless Billing (Yes/No): ")
    monthly = float(input("Monthly Charges: "))
    total = float(input("Total Charges: "))

    # Create dictionary
    data = {
        'gender': gender,
        'SeniorCitizen': senior,
        'Partner': partner,
        'Dependents': dependents,
        'tenure': tenure,
        'PhoneService': phone,
        'PaperlessBilling': paperless,
        'MonthlyCharges': monthly,
        'TotalCharges': total
    }

    df = pd.DataFrame([data])

   
    df['gender'] = df['gender'].map({'Male': 0, 'Female': 1})
    df['Partner'] = df['Partner'].map({'No': 0, 'Yes': 1})
    df['Dependents'] = df['Dependents'].map({'No': 0, 'Yes': 1})
    df['PhoneService'] = df['PhoneService'].map({'No': 0, 'Yes': 1})
    df['PaperlessBilling'] = df['PaperlessBilling'].map({'No': 0, 'Yes': 1})

    # Reorder columns to match the training data
    model_features = model.feature_names_in_
    df = df[model_features]

    # Scale the features
    df_scaled = scaler.transform(df)

    # Predict
    prediction = model.predict(df_scaled)

    if prediction[0] == 1:
        print("\nCustomer will churn")
    else:
        print("\nCustomer will stay ")