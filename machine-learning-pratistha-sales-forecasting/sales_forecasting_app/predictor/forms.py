from django import forms

SHIP_MODE = [
    (0, "Standard Class"),
    (1, "Second Class"),
    (2, "First Class"),
    (3, "Same Day"),
]

SEGMENT = [
    (0, "Consumer"),
    (1, "Corporate"),
    (2, "Home Office"),
]

REGION = [
    (0, "West"),
    (1, "East"),
    (2, "Central"),
    (3, "South"),
]

CATEGORY = [
    (0, "Furniture"),
    (1, "Office Supplies"),
    (2, "Technology"),
]

class SalesForecastForm(forms.Form):
    SHIP_MODE = forms.ChoiceField(choices=SHIP_MODE)
    SEGMENT = forms.ChoiceField(choices=SEGMENT)
    REGION = forms.ChoiceField(choices=REGION)
    CATEGORY = forms.ChoiceField(choices=CATEGORY)

    QUANTITY = forms.IntegerField(min_value=1)
    DISCOUNT = forms.FloatField(min_value=0, max_value=1)
    POSTAL_CODE = forms.IntegerField()

    SHIP_MONTH = forms.IntegerField(min_value=1, max_value=12)
    SHIP_DAY = forms.IntegerField(min_value=1, max_value=31)

    def get_feature_dict(self):
        data = self.cleaned_data

        return {
            "Ship Mode": int(data["SHIP_MODE"]),
            "Segment": int(data["SEGMENT"]),
            "Region": int(data["REGION"]),
            "Category": int(data["CATEGORY"]),
            "Quantity": int(data["QUANTITY"]),
            "Discount": float(data["DISCOUNT"]),
            "Postal Code": int(data["POSTAL_CODE"]),
            "Ship Month": int(data["SHIP_MONTH"]),
            "Ship Day": int(data["SHIP_DAY"]),
        }