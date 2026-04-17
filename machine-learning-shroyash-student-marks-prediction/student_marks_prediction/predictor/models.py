from django.db import models

class PredictionRecord(models.Model):
    """
    Stores every prediction made through the web form or API.
    Useful for auditing and building a history dashboard.
    """
    hours_studied = models.FloatField()
    attendance = models.FloatField()
    previous_scores = models.FloatField()
    sleep_hours = models.FloatField()
    papers_practiced = models.IntegerField()
    predicted_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Prediction: {self.predicted_score:.1f} @ {self.created_at:%Y-%m-%d %H:%M}"