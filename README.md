# FinAI Assistant

An intelligent financial companion that combines AI-powered advisory, portfolio management, fraud detection, and market analytics to help users make informed investment decisions.

## Features

### AI Financial Assistant
- Real-time conversational AI powered by Google Gemini
- Personalized financial advice and investment guidance
- Context-aware responses with session management

### Portfolio Management
- Track and manage investment portfolios
- Monitor stock holdings with buy prices and quantities
- Calculate profit/loss across multiple stocks
- Real-time portfolio valuation

### Fraud Detection
- Automated fraud screening for suspicious stocks
- Blacklist checking for known fraudulent companies
- Price movement anomaly detection
- ML-based risk scoring system

### Market Analytics
- Interactive stock performance charts
- Real-time price tracking via Alpha Vantage API
- Visual data representation with Recharts

### Investment Education
- Comprehensive investment guides
- Risk assessment tools
- Market trend analysis

## Tech Stack

### Backend
- Flask - Web framework
- PostgreSQL - Database
- SQLAlchemy - ORM
- Google Gemini API - AI chatbot
- Alpha Vantage API - Stock data
- Werkzeug - Password hashing

### Frontend
- React 18 with TypeScript
- React Router - Navigation
- Tailwind CSS - Styling
- Framer Motion - Animations
- Recharts - Data visualization
- Lucide React - Icons

## Installation

### Prerequisites
- Python 3.8+
- Node.js 16+
- PostgreSQL
- API Keys for Google Gemini and Alpha Vantage

### Backend Setup

1. Clone the repository
```bash
git clone https://github.com/Pranshul-Thakur/finai-assistant.git
cd finai-assistant/backend
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install flask flask-sqlalchemy psycopg2-binary werkzeug google-generativeai requests python-dotenv
```

4. Configure environment variables
Create a `.env` file in the backend directory:
```env
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgresql://username:password@localhost/finance_db
API_KEY=your_gemini_api_key
ALPHA_VANTAGE_API_KEY=your_alphavantage_api_key
```

5. Initialize database
```bash
python app.py
```

### Frontend Setup

1. Navigate to frontend directory
```bash
cd ../frontend
```

2. Install dependencies
```bash
npm install
```

3. Start development server
```bash
npm run dev
```

## API Endpoints

### Authentication
- `POST /auth/signup` - Register new user
- `POST /auth/login` - User login
- `POST /auth/logout` - User logout

### Portfolio Management
- `POST /portfolio/add` - Add stock to portfolio
- `GET /portfolio` - Get user portfolio
- `POST /portfolio/profit` - Calculate profit/loss

### Chatbot
- `POST /chatbot/chat` - Send message to AI assistant

### Fraud Detection
- `POST /fraud/check` - Check stock for fraud indicators

## Project Structure

```
finai-assistant/
├── backend/
│   ├── routes/
│   │   ├── auth.py
│   │   ├── chatbot.py
│   │   ├── fraud_detection.py
│   │   ├── portfolio.py
│   │   └── stock_analysis.py
│   ├── utils/
│   │   ├── sentiment.py
│   │   └── stock_price.py
│   ├── app.py
│   ├── config.py
│   └── models.py
└── frontend/
    ├── components/
    │   ├── ChatBot.tsx
    │   ├── InvestmentGuide.tsx
    │   └── StockGraph.tsx
    ├── pages/
    │   ├── Dashboard.tsx
    │   ├── ChatbotPage.tsx
    │   ├── AnalyticsPage.tsx
    │   ├── InvestmentGuidePage.tsx
    │   └── PortfolioPage.tsx
    ├── App.tsx
    └── main.tsx
```

## Database Schema

### User Table
- id (Primary Key)
- username (Unique)
- password_hash

### Portfolio Table
- id (Primary Key)
- user_id (Foreign Key)
- stock_name
- buy_price
- quantity

### Fraud Report Table
- id (Primary Key)
- user_id (Foreign Key)
- stock_name
- reason
- timestamp

## Security Features

- Password hashing with Werkzeug
- Session-based authentication
- SQL injection prevention via SQLAlchemy ORM
- Input validation and sanitization
- Protected API endpoints
