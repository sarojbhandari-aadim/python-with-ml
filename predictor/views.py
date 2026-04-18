from django.shortcuts import render, redirect
import joblib
import pandas as pd
import os
from .forms import CropForm

def predict_yield(request):
    # Try to pop result from session for a clean refresh (PRG pattern)
    result = request.session.pop('prediction_result', None)
    
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            try:
                # 1. Define paths for our saved "Brain" files
                ml_dir = os.path.join(os.path.dirname(__file__), 'ml')
                model_path = os.path.join(ml_dir, 'crop_yield_model.pkl')
                scaler_path = os.path.join(ml_dir, 'scaler.pkl')
                cols_path = os.path.join(ml_dir, 'model_columns.pkl')

                # 2. Load the saved files
                model = joblib.load(model_path)
                scaler = joblib.load(scaler_path)
                model_columns = joblib.load(cols_path)
                
                # 3. Create DataFrame from user input
                input_data = pd.DataFrame([{
                    'Area': form.cleaned_data['area'],
                    'Item': form.cleaned_data['item'],
                    'Year': form.cleaned_data['year'],
                    'average_rain_fall_mm_per_year': form.cleaned_data['rainfall'],
                    'pesticides_tonnes': form.cleaned_data['pesticides'],
                    'avg_temp': form.cleaned_data['temp']
                }])
                
                # 4. Manual Preprocessing (One-Hot Encoding)
                # Convert the user input into the same "Dummy" format used in training
                input_encoded = pd.get_dummies(input_data)
                
                # Align columns: ensures input has the same columns as the training data
                input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)
                
                # 5. Manual Scaling
                input_scaled = scaler.transform(input_encoded)
                
                # 6. Prediction
                prediction = model.predict(input_scaled)[0]
                
                # Save result to session and redirect (prevents resubmission on refresh)
                request.session['prediction_result'] = f"{round(prediction, 2)} hg/ha"
                return redirect(request.path)

            except Exception as e:
                result = f"Error: {str(e)}"
    else:
        form = CropForm()
    
    return render(request, 'predictor/index.html', {'form': form, 'result': result})