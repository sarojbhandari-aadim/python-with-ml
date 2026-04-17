from rest_framework import serializers

class PredictionInputSerializer(serializers.Serializer):
    hours_studied = serializers.FloatField(min_value=0, max_value=24)
    attendance = serializers.FloatField(min_value=0, max_value=100)
    previous_scores = serializers.FloatField(min_value=0, max_value=100)
    sleep_hours = serializers.FloatField(min_value=0, max_value=24)
    papers_practiced = serializers.IntegerField(min_value=0, max_value=10)