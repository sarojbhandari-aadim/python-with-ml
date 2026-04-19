from django.shortcuts import render
from .forms import SalesForecastForm
from .ml.predict import predict_sales


def home(request):
    result = None

    if request.method == "POST":
        form = SalesForecastForm(request.POST)

        if form.is_valid():
            features = form.get_feature_dict()
            result = predict_sales(features)
    else:
        form = SalesForecastForm()

    return render(request, "form.html", {"form": form, "result": result})