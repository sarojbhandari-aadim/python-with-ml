from django import forms

class AirQualityForm(forms.Form):
    Temperature = forms.FloatField(
        label="Temperature (°C)",
        widget=forms.NumberInput(attrs={'step': '0.1'})
    )
    Humidity = forms.FloatField(
        label="Humidity (%)",
        widget=forms.NumberInput(attrs={'step': '0.1'})
    )
    PM2_5 = forms.FloatField(label="PM2.5")
    NO2 = forms.FloatField(label="NO2")
    SO2 = forms.FloatField(label="SO2")
    CO = forms.FloatField(label="CO")
    Proximity_to_Industrial_Areas = forms.FloatField(label="Proximity to Industrial Areas")
    Population_Density = forms.FloatField(label="Population Density")