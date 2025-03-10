from flask import Flask, render_template, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import yfinance as yf
import openai
import os

app = Flask(__name__)
app.secret_key = 'API_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/finance_db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    stock_symbol = db.Column(db.String(10), nullable=False)
    buy_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    buy_date = db.Column(db.DateTime, nullable=False)

def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period='1d')
    return data['Close'].iloc[-1] if not data.empty else None

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    hashed_password = generate_password_hash(data['password'])
    new_user = User(username=data['username'], password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password_hash, data['password']):
        session['user_id'] = user.id
        return jsonify({"message": "Login successful!"})
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/add_stock', methods=['POST'])
def add_stock():
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    data = request.json
    new_stock = Portfolio(
        user_id=session['user_id'],
        stock_symbol=data['symbol'].upper(),
        buy_price=data['buy_price'],
        quantity=data['quantity'],
        buy_date=data['buy_date']
    )
    db.session.add(new_stock)
    db.session.commit()
    return jsonify({"message": "Stock added successfully!"})

@app.route('/portfolio', methods=['GET'])
def portfolio():
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    stocks = Portfolio.query.filter_by(user_id=session['user_id']).all()
    portfolio_data = []
    for stock in stocks:
        current_price = get_stock_price(stock.stock_symbol)
        profit_loss = (current_price - stock.buy_price) * stock.quantity if current_price else None
        portfolio_data.append({
            "symbol": stock.stock_symbol,
            "buy_price": stock.buy_price,
            "quantity": stock.quantity,
            "current_price": current_price,
            "profit_loss": profit_loss
        })
    return jsonify(portfolio_data)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a financial assistant."},
                  {"role": "user", "content": data['message']}]
    )
    return jsonify({"response": response['choices'][0]['message']['content']})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)