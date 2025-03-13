from flask import Flask
from config import Config
from models import db
from routes.auth import auth_bp
from routes.portfolio import portfolio_bp
from routes.chatbot import chatbot_bp
from routes.stock_analysis import stock_analysis_bp
from routes.fraud_detection import fraud_detection_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(portfolio_bp, url_prefix='/portfolio')
app.register_blueprint(chatbot_bp, url_prefix='/chatbot')
app.register_blueprint(stock_analysis_bp, url_prefix='/stocks')
app.register_blueprint(fraud_detection_bp, url_prefix='/fraud')

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
