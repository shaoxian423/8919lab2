from flask import Flask, request, jsonify
import logging
import sys

app = Flask(__name__)

# configure logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# daemonstration users
USERS = {"admin": "password123"}

@app.route('/')
def home():
    return "Welcome to 8919 Lab 2"

@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        logger.error("Login failed: Missing username or password")
        return jsonify({"status": "error", "message": "Missing username or password"}), 400

    if username in USERS and USERS[username] == password:
        logger.info(f"Login successful for user: {username}")
        return jsonify({"status": "success", "message": "Login successful"}), 200
    else:
        logger.error(f"Login failed for user: {username}")
        return jsonify({"status": "error", "message": "Invalid credentials"}), 401