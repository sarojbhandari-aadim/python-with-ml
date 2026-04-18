## Credit Card Fraud Detection System
#### Description

A Django-based web application that detects whether a transaction is Fraudulent or Normal using Machine Learning.
The system takes user input, processes it using a trained model, and displays the prediction result in real time.

#### Features
- User-friendly web interface (Django)
- Real-time fraud prediction
- Data preprocessing (encoding, feature extraction)
- Machine Learning model integration using .pkl
- Displays prediction result 

#### Algorithm Used
- Logistic Regression
- Data Scaling using StandardScaler

#### Dataset
1) Credit Card Fraud Dataset
    - Contains transaction details such as:
    - Transaction amount
    - Transaction type
    - Location
    - Date & time
2) Target:
    - 0 → Normal Transaction
    - 1 → Fraud Transaction

#### Project Workflow
1) Data preprocessing (cleaning, encoding, feature engineering)
2) Model training using Logistic Regression
3) Model saved using Pickle (.pkl)
4) Integrated into Django backend
5) User input - Model prediction - Result displayed


#### Installation
   pip install -r requirements.txt

#### How to Run
python manage.py runserver

Open in browser:

http://127.0.0.1:8000/

Project Structure
- ml_model/ - Jupyter notebook and pickle files
- fraud_system/ - Django app
- templates/ - HTML files


