import pandas as pd
import os
import logging
from sklearn.linear_model import LinearRegression

logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, 'TESLA.csv')


def load_tesla_data():
    try:
        if not os.path.exists(CSV_PATH):
            logger.error("CSV file not found")
            return None

        df = pd.read_csv(CSV_PATH)

        df.columns = [col.strip() for col in df.columns]

        numeric_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        df = df.dropna()

        return df

    except Exception as e:
        logger.error(f"Error loading CSV: {e}")
        return None


def train_model():
    df = load_tesla_data()

    if df is None or df.empty:
        raise Exception("No data available")

    X = df[['Open', 'High', 'Low', 'Volume']]
    y = df['Close']

    model = LinearRegression()
    model.fit(X, y)

    return model


model = train_model()


def predict_price(open_price, high, low, volume):
    prediction = model.predict(
        pd.DataFrame([[open_price, high, low, volume]],
                     columns=['Open', 'High', 'Low', 'Volume'])
    )

    return float(prediction[0])

def predict_with_details(open_price, high, low, volume):
    predicted_close = predict_price(open_price, high, low, volume)

    change = predicted_close - open_price
    change_percent = (change / open_price) * 100 if open_price != 0 else 0

    return {
        'open': round(open_price, 2),
        'high': round(high, 2),
        'low': round(low, 2),
        'predicted_close': round(predicted_close, 2),
        'change': round(change, 2),
        'change_percent': round(change_percent, 2),
        'trend': 'UP' if change > 0 else 'DOWN'
    }



def get_model_info():
    df = load_tesla_data()

    return {
        'model': 'Linear Regression',
        'features': ['Open', 'High', 'Low', 'Volume'],
        'target': 'Close',
        'data_points': len(df) if df is not None else 0
    }


def get_stock_info():
    df = load_tesla_data()

    if df is None:
        return {
            'symbol': 'TSLA',
            'data_available': False
        }

    return {
        'symbol': 'TSLA',
        'data_available': True,
        'total_rows': len(df)
    }


if __name__ == "__main__":
    print("Testing ML Service...")

    result = predict_with_details(250, 260, 245, 10000000)

    print("Prediction Result:")
    print(result)