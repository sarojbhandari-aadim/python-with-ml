import os
import pickle
import numpy as np
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .forms import PredictionForm
from .models import PredictionRecord

# ── Load model and scaler once at startup (not on every request) ──
BASE_ML = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ml")

with open(os.path.join(BASE_ML, "model.pkl"), "rb") as f:
    MODEL = pickle.load(f)

with open(os.path.join(BASE_ML, "scaler.pkl"), "rb") as f:
    SCALER = pickle.load(f)

# Feature order must match training order exactly!
FEATURES = ["Hours_Studied", "Attendance", "Previous_Scores",
            "Sleep_Hours", "Sample_Question_Papers_Practiced"]


def _predict(hours, attendance, prev_scores, sleep, papers):
    """
    Core prediction logic.
    Returns predicted score clamped to [0, 100].
    """
    raw = np.array([[hours, attendance, prev_scores, sleep, papers]], dtype=float)
    scaled = SCALER.transform(raw)
    pred = MODEL.predict(scaled)[0]
    return round(float(np.clip(pred, 0, 100)), 2)


def index(request):
    """
    Main prediction page: GET shows form, POST runs prediction.
    """
    form = PredictionForm()
    prediction = None
    history = PredictionRecord.objects.all()[:10]  # last 10 predictions

    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data
            prediction = _predict(
                d["hours_studied"], d["attendance"],
                d["previous_scores"], d["sleep_hours"],
                d["papers_practiced"],
            )
            # Save to DB
            PredictionRecord.objects.create(
                hours_studied=d["hours_studied"],
                attendance=d["attendance"],
                previous_scores=d["previous_scores"],
                sleep_hours=d["sleep_hours"],
                papers_practiced=d["papers_practiced"],
                predicted_score=prediction,
            )
            history = PredictionRecord.objects.all()[:10]

    return render(request, "predictor/index.html", {
        "form": form,
        "prediction": prediction,
        "history": history,
    })


def eda(request):
    """EDA charts page."""
    return render(request, "predictor/eda.html")


# ── REST API ──────────────────────────────────────────────────────

class PredictAPIView(APIView):
    """
    POST /api/predict/
    Body: { hours_studied, attendance, previous_scores, sleep_hours, papers_practiced }
    Returns: { predicted_score }
    """
    def post(self, request):
        try:
            d = request.data
            required = ["hours_studied", "attendance", "previous_scores",
                        "sleep_hours", "papers_practiced"]
            for field in required:
                if field not in d:
                    return Response(
                        {"error": f"Missing field: {field}"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            pred = _predict(
                float(d["hours_studied"]),
                float(d["attendance"]),
                float(d["previous_scores"]),
                float(d["sleep_hours"]),
                int(d["papers_practiced"]),
            )
            # Save API predictions too
            PredictionRecord.objects.create(
                hours_studied=d["hours_studied"],
                attendance=d["attendance"],
                previous_scores=d["previous_scores"],
                sleep_hours=d["sleep_hours"],
                papers_practiced=d["papers_practiced"],
                predicted_score=pred,
            )
            return Response({"predicted_score": pred}, status=status.HTTP_200_OK)

        except (ValueError, TypeError) as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)