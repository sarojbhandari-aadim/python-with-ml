import joblib
import numpy as np
import os
from django.shortcuts import render

# Load the model once when server starts
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'ml_model', 'laptop_price_prediction_model.pkl')
model = joblib.load(MODEL_PATH)

def predict(request):
    prediction = None
    if request.method == 'POST':
        try:
            # Numeric inputs
            ram = float(request.POST.get('ram'))
            weight = float(request.POST.get('weight'))
            opsys = float(request.POST.get('opsys'))
            touchscreen = int(request.POST.get('touchscreen'))
            ips = int(request.POST.get('ips'))
            ppi = float(request.POST.get('ppi'))
            cpu_brand = float(request.POST.get('cpu_brand'))
            cpu_frequency = float(request.POST.get('cpu_frequency'))
            memory_size = float(request.POST.get('memory_size'))
            ssd = float(request.POST.get('ssd'))
            hdd = float(request.POST.get('hdd'))
            flash_storage = float(request.POST.get('flash_storage'))
            hybrid = float(request.POST.get('hybrid'))
            gpu_brand = float(request.POST.get('gpu_brand'))

            # Brand (one-hot) — only one should be 1
            brand = request.POST.get('brand')
            brands = ['Acer','Apple','Asus','Chuwi','Dell','Fujitsu','Google',
                      'HP','Huawei','LG','Lenovo','MSI','Mediacom','Microsoft',
                      'Razer','Samsung','Toshiba','Vero','Xiaomi']
            brand_values = [1 if b == brand else 0 for b in brands]

            # Laptop type (one-hot) — only one should be 1
            laptop_type = request.POST.get('laptop_type')
            types = ['2 in 1 Convertible','Gaming','Netbook','Notebook','Ultrabook','Workstation']
            type_values = [1 if t == laptop_type else 0 for t in types]

            # Combine all features in correct order
            features = np.array([[
                ram, opsys, weight,
                *brand_values,
                *type_values,
                touchscreen, ips, ppi,
                cpu_brand, cpu_frequency,
                memory_size, ssd, hdd, flash_storage, hybrid,
                gpu_brand
            ]])

            result = model.predict(features)
            prediction = "{:.2f}".format(float(result[0]))

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render(request, 'predictor/index.html', {'prediction': prediction})