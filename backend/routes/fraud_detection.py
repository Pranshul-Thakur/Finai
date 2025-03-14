from flask import Blueprint, request, jsonify, session
from models import db, FraudReport, Portfolio
import random  # Placeholder for ML model
import requests
import os

fraud_bp = Blueprint('fraud', __name__)
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

def detect_fraud(stock_name, buy_price):
    """
    Detects fraud based on price movement, volume anomalies, or blacklisted stocks.
    Placeholder for ML model.
    """
    BLACKLISTED_STOCKS = ["XYZ Corp", "ScamStock123", "PumpAndDump Ltd"]
    if stock_name in BLACKLISTED_STOCKS:
        return True, f"{stock_name} is flagged as a blacklisted stock!"
    current_price = get_stock_price(stock_name)
    if current_price:
        price_change = ((current_price - buy_price) / buy_price) * 100
        if abs(price_change) > 50:
            return True, f"Unusual price movement detected for {stock_name}: {price_change:.2f}% change."
    ml_fraud_score = random.uniform(0, 1)
    if ml_fraud_score > 0.7:  
        return True, f"Stock {stock_name} is flagged as high risk ({ml_fraud_score:.2f} fraud probability)."

    return False, None

def get_stock_price(stock_name):
    """
    Fetches live stock price from Alpha Vantage API (Optional)
    """
    if not ALPHA_VANTAGE_API_KEY:
        return None
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_name}&interval=5min&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url).json()
    try:
        latest_time = list(response["Time Series (5min)"].keys())[0]
        return float(response["Time Series (5min)"][latest_time]["1. open"])
    except (KeyError, IndexError):
        return None

@fraud_bp.route('/fraud/check', methods=['POST'])
def check_fraud():
    """
    API endpoint for checking stock fraud
    """
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    data = request.get_json()
    stock_name = data.get('stock_name')
    buy_price = data.get('buy_price')
    if not stock_name or not buy_price:
        return jsonify({'error': 'Missing stock details'}), 400
    is_fraud, reason = detect_fraud(stock_name, buy_price)
    if is_fraud:
        fraud_entry = FraudReport(user_id=session['user_id'], stock_name=stock_name, reason=reason)
        db.session.add(fraud_entry)
        db.session.commit()
        return jsonify({'fraud_detected': True, 'reason': reason}), 200
    return jsonify({'fraud_detected': False, 'message': 'No fraud detected'}), 200
