from django.shortcuts import render
import joblib
import numpy as np
import os
from .forms import AirQualityForm

# Load the model files
model_path = os.path.join(os.path.dirname(__file__), 'air_quality_rf_model.pkl')
scaler_path = os.path.join(os.path.dirname(__file__), 'scaler.pkl')
le_path = os.path.join(os.path.dirname(__file__), 'label_encoder.pkl')

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)
le = joblib.load(le_path)

def predict_air_quality(request):
    prediction_text = None
    predicted_class = None

    if request.method == 'POST':
        form = AirQualityForm(request.POST)
        if form.is_valid():
            input_data = [
                form.cleaned_data['Temperature'],
                form.cleaned_data['Humidity'],
                form.cleaned_data['PM2_5'],
                form.cleaned_data['NO2'],
                form.cleaned_data['SO2'],
                form.cleaned_data['CO'],
                form.cleaned_data['Proximity_to_Industrial_Areas'],
                form.cleaned_data['Population_Density']
            ]

            input_array = np.array(input_data).reshape(1, -1)
            input_scaled = scaler.transform(input_array)

            pred_encoded = model.predict(input_scaled)[0]
            predicted_class = le.inverse_transform([pred_encoded])[0]

            prediction_text = f"The predicted air quality is: <strong>{predicted_class}</strong>"

    else:
        form = AirQualityForm()

    return render(request, 'predictor/predict.html', {
        'form': form,
        'prediction_text': prediction_text,
        'predicted_class': predicted_class
    })