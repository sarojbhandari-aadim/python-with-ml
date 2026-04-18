import numpy as np
from .ml_model import model, scaler, feature_names

def predict_fraud(input_data):

    # convert input to correct order
    input_array = np.array([input_data])

    # scale input
    input_scaled = scaler.transform(input_array)

    # prediction
    prediction = model.predict(input_scaled)

    return prediction[0]