from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    portfolio = db.relationship('Portfolio', backref='owner', lazy=True)
    
    def __repr__(self):
        return f'<User {self.username}>'
    
class portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    stock_name = db.Column(db.String(10), nullable=False)
    buy_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<Portfolio {self.stock_name} - {self.quantity} shares>'