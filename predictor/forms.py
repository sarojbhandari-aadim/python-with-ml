from django import forms
import pandas as pd
import os

# Get unique values for dropdowns
try:
    csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'yield_df.csv')
    df = pd.read_csv(csv_path)
    COUNTRIES = sorted([(c, c) for c in df['Area'].unique()])
    CROPS = sorted([(i, i) for i in df['Item'].unique()])
except:
    COUNTRIES = [('India', 'India')]
    CROPS = [('Rice', 'Rice')]

class CropForm(forms.Form):
    area = forms.ChoiceField(
        choices=COUNTRIES,
        label="Country/Region",
        help_text="Select the country or region for the prediction.",
        widget=forms.Select(attrs={'class': 'form-select select2-dropdown'})
    )
    item = forms.ChoiceField(
        choices=CROPS,
        label="Crop Type",
        help_text="Choose the crop type from the list.(e.g., Rice)",
        widget=forms.Select(attrs={'class': 'form-select select2-dropdown'})
    )
    year = forms.IntegerField(
        label="Target Year",
        help_text="Enter the target year (e.g., 2026).",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 2026'})
    )
    rainfall = forms.FloatField(
        label="Average Rainfall (mm)",
        help_text="Average annual rainfall in mm (e.g., 1200).",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 1200'})
    )
    pesticides = forms.FloatField(
        label="Pesticides (tonnes)",
        help_text="Total pesticides used in tonnes (e.g., 500).",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 500'})
    )
    temp = forms.FloatField(
        label="Avg Temperature (°C)",
        help_text="Mean annual temperature in °C (e.g., 22.5).",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 22.5'})
    )