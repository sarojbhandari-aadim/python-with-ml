import pandas as pd

def load_data():
    data = pd.read_csv('data/churn.csv')
    return data

def show_basic_info(data):
    print("\n First 5 rows:")
    print(data.head())

    print("\n Columns:")
    print(data.columns)

    print("\n Info:")
    print(data.info())

    print("\n Missing values: ")
    print(data.isnull().sum())

def clean_data(data):
    data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors = 'coerce')

    data = data.dropna()

    data = data.drop('customerID', axis = 1)

    return data

def convert_target(data):
    data['Churn'] = data['Churn'].map({'No': 0, 'Yes': 1})
    return data

def encode_data(data):
    data['gender'] = data['gender'].map({'Male':0, 'Female':1})

    yes_no_columns = [
        'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling'
    ]

    for col in yes_no_columns:
        data[col] = data[col].map({'No':0, 'Yes':1})

    return data

def encode_all(data):
    data = pd.get_dummies(data)

    return data