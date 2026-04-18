# Customer Churn Prediction Project

# Description

This project is a Machine Learning-based web application developed using Django.
It predicts whether a customer will churn (leave) or stay based on their service and billing information.

The system uses a Logistic Regression model for binary classification and provides real-time predictions through a web interface.

# Dataset Used
Telecom Customer Churn Dataset
Total records: 7043
Features include:
Gender, Senior Citizen
Partner, Dependents
Tenure (months)
Phone Service
Internet Services
Monthly Charges, Total Charges

Target variable:

Churn (Yes / No)
Installation Steps
1. Clone the repository
git clone <repository-link>
cd customer-churn
2. Create virtual environment
conda create -n churn python=3.10
conda activate churn
3. Install required libraries
pip install -r requirements.txt
How to Run the Project
Run Django Web Application
cd webapp
python manage.py migrate
python manage.py runserver

Open in browser:

http://127.0.0.1:8000/