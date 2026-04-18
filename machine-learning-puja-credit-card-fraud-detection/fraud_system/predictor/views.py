import numpy as np
from django.shortcuts import render
from .utils import model, scaler, feature_names

def home(request):
    result = None

    if request.method == "POST":

        try:
           
            amount = float(request.POST["amount"])
            merchant_id = int(request.POST["merchant_id"])
            hour = int(request.POST["hour"])

            day_map = {
                "monday": 0,
                "tuesday": 1,
                "wednesday": 2,
                "thursday": 3,
                "friday": 4,
                "saturday": 5,
                "sunday": 6,
            }

            day_input = request.POST["day"].lower()
            day = day_map.get(day_input)

            if day is None:
                return render(request, "home.html", {
                    "result": " Invalid day entered"
                })

            transaction_type = request.POST["transaction_type"]
            location = request.POST["location"]

            data = dict.fromkeys(feature_names, 0)

            # numeric features
            data["Amount"] = amount
            data["MerchantID"] = merchant_id
            data["hour"] = hour
            data["day"] = day

            # one-hot: TransactionType
            if transaction_type.lower() == "refund":
                data["TransactionType_refund"] = 1

            # one-hot: Location
            location_key = f"Location_{location}"
            if location_key in data:
                data[location_key] = 1

          
            input_data = np.array(
                [data[col] for col in feature_names]
            ).reshape(1, -1)

            # scale
            input_scaled = scaler.transform(input_data)

            # predict
            result = model.predict(input_scaled)[0]

        except Exception as e:
            result = f" Error: {str(e)}"

    return render(request, "home.html", {"result": result})