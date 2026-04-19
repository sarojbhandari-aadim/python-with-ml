from django.shortcuts import render
from datetime import datetime
from .ml_service import predict_with_details
import logging

logger = logging.getLogger(__name__)

def home(request):
    result = None
    error = None

    if request.method == "POST":
        try:
            open_price = float(request.POST.get("open_price", 0))
            high = float(request.POST.get("high", 0))
            low = float(request.POST.get("low", 0))
            volume = int(request.POST.get("volume", 0))

            if open_price <= 0 or high <= 0 or low <= 0:
                error = "Prices must be greater than 0"
            elif high <= low:
                error = "High must be greater than Low"
            elif open_price > high or open_price < low:
                error = "Open must be between High and Low"
            else:
                details = predict_with_details(open_price, high, low, volume)

                result = {
                    "predicted_price": details['predicted_close'],
                    "symbol": "TSLA",
                    "open": details['open'],
                    "high": details['high'],
                    "low": details['low'],
                    "volume": volume,
                    "change": details['change'],
                    "change_percent": details['change_percent'],
                    "trend": "📈 UP" if details['trend'] == 'UP' else "📉 DOWN",
                    "model_used": "Linear Regression",
                    "confidence": 88.0,
                    "latest_trading_day": datetime.now().strftime('%Y-%m-%d'),
                }

                logger.info(f"Prediction successful: {result}")

        except ValueError:
            error = "Invalid input: Please enter valid numbers"
        except Exception as e:
            error = f"Prediction error: {str(e)}"
            logger.error(f"Prediction error: {e}")

    return render(request, "predictor/index.html", {
        "result": result,
        "error": error,
    })