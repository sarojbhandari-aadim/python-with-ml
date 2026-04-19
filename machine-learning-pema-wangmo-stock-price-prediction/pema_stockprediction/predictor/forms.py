from django import forms
from django.core.exceptions import ValidationError

class StockPredictionForm(forms.Form):

    open_price = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'step': '0.01',
            'class': 'form-control',
            'placeholder': 'Open Price'
        }),
        label="Open Price",
        min_value=0.01
    )

    high = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'step': '0.01',
            'class': 'form-control',
            'placeholder': 'High Price'
        }),
        label="High Price",
        min_value=0.01
    )

    low = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'step': '0.01',
            'class': 'form-control',
            'placeholder': 'Low Price'
        }),
        label="Low Price",
        min_value=0.01
    )

    volume = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Volume'
        }),
        label="Volume",
        min_value=0
    )

    MODEL_CHOICES = [
        ('ridge', 'Ridge Regression'),
        ('linear', 'Linear Regression'),
        ('random_forest', 'Random Forest'),
    ]

    model_type = forms.ChoiceField(
        choices=MODEL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="ML Model",
        required=False,
        initial='ridge'
    )

    use_csv_data = forms.BooleanField(
        initial=True,
        widget=forms.HiddenInput(),
        required=False
    )

    # 
    def clean_open_price(self):
        value = self.cleaned_data.get('open_price')
        if value <= 0:
            raise ValidationError("Open price must be greater than 0")
        return value

    def clean_high(self):
        value = self.cleaned_data.get('high')
        if value <= 0:
            raise ValidationError("High price must be greater than 0")
        return value

    def clean_low(self):
        value = self.cleaned_data.get('low')
        if value <= 0:
            raise ValidationError("Low price must be greater than 0")
        return value

    def clean(self):
        cleaned_data = super().clean()
        open_price = cleaned_data.get('open_price')
        high = cleaned_data.get('high')
        low = cleaned_data.get('low')

        if high and low:
            if high <= low:
                raise ValidationError("High price must be greater than Low price")

        if open_price and high and low:
            if open_price > high or open_price < low:
                raise ValidationError("Open price must be between High and Low")

        return cleaned_data