from flask import Flask, request
import logging
import os

app = Flask(__name__)

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 模拟用户数据库
USERS = {"admin": "password123"}

@app.route('/')
def home():
    return "Welcome to 8919 Lab 2"

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        logger.error(f"Login failed: Missing username or password")
        return {"status": "error", "message": "Missing username or password"}, 400

    if username in USERS and USERS[username] == password:
        logger.info(f"Login successful for user: {username}")
        return {"status": "success", "message": "Login successful"}, 200
    else:
        logger.error(f"Login failed for user: {username}")
        return {"status": "error", "message": "Invalid credentials"}, 401

if __name__ == '__main__':
    app.run(debug=True)