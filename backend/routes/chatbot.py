from flask import Blueprint, request, jsonify, session
import google.generativeai as genai
import os

chatbot_bp = Blueprint('chatbot', __name__)
genai.configure(api_key=os.getenv('API_KEY'))
user_sessions = {}

def get_chatbot_response(user_id, message):
    """Handles chatbot responses with session awareness using Gemini API."""
    if user_id not in user_sessions:
        user_sessions[user_id] = []
    user_sessions[user_id].append({"role": "user", "content": message})
    model = genai.GenerativeModel("gemini-1.5-turbo")
    response = model.generate_content(message)
    bot_reply = response.text.strip()
    user_sessions[user_id].append({"role": "assistant", "content": bot_reply})

    return bot_reply

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    """Handles user queries and provides AI-generated responses using Gemini."""
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    data = request.get_json()
    message = data.get('message')
    if not message:
        return jsonify({'error': 'Message is required'}), 400
    response = get_chatbot_response(session['user_id'], message)
    return jsonify({'response': response}), 200