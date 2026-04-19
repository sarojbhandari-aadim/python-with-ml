# House Rent Prediction System: 
    House rent prediction system is a django web application that predict the monthly rent of a house based on property details using machine learning.

# Algorithm used:
    Alogrithm i have used in this project are:
        - Random Forest Regressor : i used random forest regressor over linear regressor because it give more accurate result than   linear regression . My dataset has:different cities,different house types,non-linear pricing so random forest algorithm handel this well than linear regressor.

        - Label Encoding + Standard Scaler (Preprocessing): label encoding convert text into number and standard scaler normalize data

# Dataset
- House_Rent_Dataset.csv - 4,746 house listings
- Source: Kaggle (House_Rent_Dataset)
- Features: BHK, Size, City, Furnishing Status, Tenant Preferred, etc.

# Installation
    pip install -r requirements.txt

# How to Run
    1. Clone the repository
    2. Install requirements:
   pip install django pandas scikit-learn numpy
    3. Train the model:py train_model.py
    4. Run server:py manage.py runserver
    5. Open browser: http://127.0.0.1:8000

# Project Structure
    - train_model.py - ML training script
    - model.pkl - Saved trained model
    - predictor/ - Django app
    - predictor/templates/ - HTML files
    - House_Rent_Dataset.csv - Dataset (not included in repo)

# Output Screenshots

## Prediction Form: 

![alt text](image.png)

## Prediction Result:

![alt text](image-1.png)