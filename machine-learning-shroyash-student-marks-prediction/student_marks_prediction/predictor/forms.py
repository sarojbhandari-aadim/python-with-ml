from django import forms

class PredictionForm(forms.Form):
    """
    Web form for collecting student data.
    Validation ensures realistic input ranges.
    """
    hours_studied = forms.FloatField(
        min_value=0, max_value=24,
        label="Hours Studied per Day",
        widget=forms.NumberInput(attrs={"step": "0.5", "placeholder": "e.g. 6"}),
    )
    attendance = forms.FloatField(
        min_value=0, max_value=100,
        label="Attendance (%)",
        widget=forms.NumberInput(attrs={"step": "1", "placeholder": "e.g. 85"}),
    )
    previous_scores = forms.FloatField(
        min_value=0, max_value=100,
        label="Previous Exam Score",
        widget=forms.NumberInput(attrs={"step": "0.1", "placeholder": "e.g. 72"}),
    )
    sleep_hours = forms.FloatField(
        min_value=0, max_value=24,
        label="Sleep Hours per Night",
        widget=forms.NumberInput(attrs={"step": "0.5", "placeholder": "e.g. 7"}),
    )
    papers_practiced = forms.IntegerField(
        min_value=0, max_value=10,
        label="Sample Papers Practiced",
        widget=forms.NumberInput(attrs={"placeholder": "e.g. 3"}),
    )