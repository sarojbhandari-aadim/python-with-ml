from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

def train(data):
    x = data.drop('Churn',axis = 1)
    y = data['Churn']

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2
    )

    # create model
    model = LogisticRegression(max_iter=1000)

    # train model
    model.fit(x_train, y_train)

    #check accuracy
    accuracy = model.score(x_test, y_test)

    # save model
    joblib.dump(model, 'models/churn_model.pkl')

    return model, accuracy