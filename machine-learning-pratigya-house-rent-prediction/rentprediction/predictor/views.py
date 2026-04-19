import pickle
import numpy as np
import os
from django.shortcuts import render


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'model.pkl')

with open(model_path, 'rb') as f:
    model_data = pickle.load(f)

model           = model_data['model']
scaler          = model_data['scaler']
label_encoders  = model_data['label_encoders']
feature_columns = model_data['feature_columns']


def predict_view(request):
    prediction = None
    error = None

    if request.method == 'POST':
        try:
            bhk              = int(request.POST.get('bhk'))
            size             = float(request.POST.get('size'))
            area_type        = request.POST.get('area_type')
            city             = request.POST.get('city')
            furnishing       = request.POST.get('furnishing_status')
            tenant           = request.POST.get('tenant_preferred')
            bathroom         = int(request.POST.get('bathroom'))
            point_of_contact = request.POST.get('point_of_contact')
            posted_year      = int(request.POST.get('posted_year'))
            posted_month     = int(request.POST.get('posted_month'))

            def encode(col_name, value):
                le = label_encoders[col_name]
                if value not in le.classes_:
                    value = le.classes_[0]
                return le.transform([value])[0]

            area_type_enc  = encode('Area Type',         area_type)
            city_enc       = encode('City',              city)
            furnishing_enc = encode('Furnishing Status', furnishing)
            tenant_enc     = encode('Tenant Preferred',  tenant)
            contact_enc    = encode('Point of Contact',  point_of_contact)

            input_data = np.array([[
                bhk, size, area_type_enc, city_enc,
                furnishing_enc, tenant_enc, bathroom,
                contact_enc, posted_year, posted_month,
            ]])

            input_scaled   = scaler.transform(input_data)
            predicted_rent = model.predict(input_scaled)[0]
            prediction     = round(float(predicted_rent), 2)

        except Exception as e:
            error = f"Error: {str(e)}"

    context = {
        'prediction':  prediction,
        'error':       error,
        'area_types':  list(label_encoders['Area Type'].classes_),
        'cities':      list(label_encoders['City'].classes_),
        'furnishings': list(label_encoders['Furnishing Status'].classes_),
        'tenants':     list(label_encoders['Tenant Preferred'].classes_),
        'contacts':    list(label_encoders['Point of Contact'].classes_),
    }

    return render(request, 'index.html', context)  # if file is in templates/index.html