from django import forms

GENDER_CHOICES = [
    ("Male", "Male"),
    ("Female", "Female"),
]

SMOKER_CHOICES = [
    ("Yes", "Yes"),
    ("No", "No"),
]

YES_NO_CHOICES = [
    (1, "Yes"),
    (0, "No"),
]

ACTIVITY_CHOICES = [
    ("Low", "Low"),
    ("Medium", "Medium"),
    ("High", "High"),
]

INSURANCE_CHOICES = [
    ("None", "None"),
    ("Government", "Government"),
    ("Private", "Private"),
]

CITY_CHOICES = [
    ("Urban", "Urban"),
    ("Semi-Urban", "Semi-Urban"),
    ("Rural", "Rural"),
]


class MedicalCostForm(forms.Form):
    age = forms.IntegerField(label="Age", min_value=1, max_value=120)
    gender = forms.ChoiceField(label="Gender", choices=GENDER_CHOICES)
    bmi = forms.FloatField(label="BMI", min_value=10.0, max_value=60.0)
    smoker = forms.ChoiceField(label="Smoker", choices=SMOKER_CHOICES)

    diabetes = forms.ChoiceField(label="Diabetes", choices=YES_NO_CHOICES)
    hypertension = forms.ChoiceField(label="Hypertension", choices=YES_NO_CHOICES)
    heart_disease = forms.ChoiceField(label="Heart Disease", choices=YES_NO_CHOICES)
    asthma = forms.ChoiceField(label="Asthma", choices=YES_NO_CHOICES)

    physical_activity_level = forms.ChoiceField(label="Physical Activity Level", choices=ACTIVITY_CHOICES)
    daily_steps = forms.IntegerField(label="Daily Steps", min_value=0, max_value=50000)
    sleep_hours = forms.FloatField(label="Sleep Hours / Day", min_value=0.0, max_value=24.0)
    stress_level = forms.IntegerField(label="Stress Level (1-10)", min_value=1, max_value=10)

    doctor_visits_per_year = forms.IntegerField(label="Doctor Visits / Year", min_value=0, max_value=50)
    hospital_admissions = forms.IntegerField(label="Hospital Admissions", min_value=0, max_value=30)
    medication_count = forms.IntegerField(label="Medication Count", min_value=0, max_value=30)

    insurance_type = forms.ChoiceField(label="Insurance Type", choices=INSURANCE_CHOICES)
    insurance_coverage_pct = forms.FloatField(label="Insurance Coverage %", min_value=0.0, max_value=100.0)
    city_type = forms.ChoiceField(label="City Type", choices=CITY_CHOICES)

    previous_year_cost = forms.FloatField(label="Previous Year Medical Cost ($)", min_value=0.0)

    def cleaned_feature_dict(self):
        data = self.cleaned_data
        return {
            "age": int(data["age"]),
            "gender": data["gender"],
            "bmi": float(data["bmi"]),
            "smoker": data["smoker"],
            "diabetes": int(data["diabetes"]),
            "hypertension": int(data["hypertension"]),
            "heart_disease": int(data["heart_disease"]),
            "asthma": int(data["asthma"]),
            "physical_activity_level": data["physical_activity_level"],
            "daily_steps": int(data["daily_steps"]),
            "sleep_hours": float(data["sleep_hours"]),
            "stress_level": int(data["stress_level"]),
            "doctor_visits_per_year": int(data["doctor_visits_per_year"]),
            "hospital_admissions": int(data["hospital_admissions"]),
            "medication_count": int(data["medication_count"]),
            "insurance_type": data["insurance_type"],
            "insurance_coverage_pct": float(data["insurance_coverage_pct"]),
            "city_type": data["city_type"],
            "previous_year_cost": float(data["previous_year_cost"]),
        }
