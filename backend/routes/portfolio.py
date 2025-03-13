from flask import Blueprint, request, jsonify, session
from models import db, Portfolio

portfolio_bp = Blueprint('portfolio', __name__)

@portfolio_bp.route('/portfolio/add', methods=['POST'])
def add_stock():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    data = request.get_json()
    stock_name = data.get('stock_name')
    quantity = data.get('quantity')
    buy_price = data.get('buy_price')
    try:
        quantity = int(quantity)
        buy_price = float(buy_price)
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid quantity or buy price'}), 400
    if not stock_name or quantity <= 0 or buy_price <= 0:
        return jsonify({'error': 'Invalid input values'}), 400
    new_stock = Portfolio(
        user_id=session['user_id'],
        stock_name=stock_name,
        quantity=quantity,
        buy_price=buy_price
    )
    db.session.add(new_stock)
    db.session.commit()
    return jsonify({'message': 'Stock added to portfolio'}), 201

@portfolio_bp.route('/portfolio', methods=['GET'])
def get_portfolio():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    portfolio = Portfolio.query.filter_by(user_id=session['user_id']).all()
    portfolio_data = [
        {'stock_name': stock.stock_name, 'quantity': stock.quantity, 'buy_price': stock.buy_price}
        for stock in portfolio
    ]
    return jsonify({'portfolio': portfolio_data}), 200

@portfolio_bp.route('/portfolio/profit', methods=['POST'])
def check_profit():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    data = request.get_json()
    stock_profits = []
    total_profit = 0
    for entry in data:
        stock_name = entry.get("stock_name")
        sell_price = entry.get("sell_price")
        if not stock_name or sell_price is None:
            return jsonify({'error': 'Missing stock name or sell price'}), 400
        try:
            sell_price = float(sell_price)
        except ValueError:
            return jsonify({'error': f'Invalid sell price for {stock_name}'}), 400
        stock = Portfolio.query.filter_by(user_id=session['user_id'], stock_name=stock_name).first()
        if not stock:
            return jsonify({'error': f'Stock {stock_name} not found in portfolio'}), 404
        profit = (sell_price - stock.buy_price) * stock.quantity
        stock_profits.append({'stock_name': stock_name, 'profit': profit})
        total_profit += profit
    return jsonify({'total_profit': total_profit, 'stock_profits': stock_profits}), 200
