from django.shortcuts import render
from .forms import MedicalCostForm
from .ml_service import predict_medical_cost


def index(request):
    prediction = None
    error = None

    if request.method == "POST":
        form = MedicalCostForm(request.POST)
        if form.is_valid():
            try:
                features = form.cleaned_feature_dict()
                result = predict_medical_cost(features)
                prediction = result
            except Exception as e:
                error = str(e)
    else:
        form = MedicalCostForm()

    return render(request, "predictor/index.html", {
        "form": form,
        "prediction": prediction,
        "error": error,
    })
