from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("eda/", views.eda, name="eda"),
    path("api/predict/", views.PredictAPIView.as_view(), name="api-predict"),
]