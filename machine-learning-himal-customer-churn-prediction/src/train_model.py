import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib

def train(data):
    x = data.drop('Churn',axis = 1)
    y = data['Churn']

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    # Scale the features
    scaler = StandardScaler()
    # Ensure scaled data remains a DataFrame to preserve feature names for the model
    x_train_scaled = pd.DataFrame(scaler.fit_transform(x_train), columns=x_train.columns)
    x_test_scaled = pd.DataFrame(scaler.transform(x_test), columns=x_test.columns)

    # create model
    model = LogisticRegression(max_iter=1000)

    # train model
    model.fit(x_train_scaled, y_train)

    #check accuracy
    accuracy = model.score(x_test_scaled, y_test)

    # save model and scaler
    joblib.dump(model, 'models/churn_model.pkl')
    joblib.dump(scaler, 'models/scaler.pkl')

    return model, accuracy