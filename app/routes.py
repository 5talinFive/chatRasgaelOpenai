from flask import Blueprint, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

bp = Blueprint('main', __name__)

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Te llamas Rasgael, presentate como tal, asistente virtual del Colegio Rafael Galeth"},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7,
    )
    return jsonify({"message": response.choices[0].message['content']})