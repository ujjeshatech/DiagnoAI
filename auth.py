import jwt
import datetime
import bcrypt
from flask import Blueprint, request, jsonify
from functools import wraps
from flask import session,redirect


SECRET_KEY = "secret key"  # Use the same key as in app.py

auth_bp = Blueprint('auth_bp', __name__)

# Dummy user database (we should use a real one)
import json

def load_users():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users():
    with open("users.json", "w") as f:
        json.dump(users_db, f)

users_db = load_users()


# Token required decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            user = users_db.get(data["user"])
            if not user:
                return jsonify({"message": "Invalid token!"}), 401
        except:
            return jsonify({"message": "Token is invalid!"}), 401
        return f(*args, **kwargs)
    return decorated

# Signup Route
@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in users_db:
        return jsonify({"message": "User already exists!"}), 400

    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users_db[username] = hashed_pw.decode('utf-8')
    save_users()


    return jsonify({"message": "User registered successfully!"})

# Login Route
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user_hashed_pw = users_db.get(username)
    if not user_hashed_pw or not bcrypt.checkpw(password.encode('utf-8'), user_hashed_pw.encode('utf-8')):

        return jsonify({"message": "Invalid credentials!"}), 401

    token = jwt.encode(
        {"user": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
        SECRET_KEY,
        algorithm="HS256"
    )

    session["user"] = username
    return jsonify({"token": token, "message": "Login successful!"})


# Protected Route Example
@auth_bp.route('/protected', methods=['GET'])
@token_required
def protected():
    return jsonify({"message": "This is a protected route!"})

@auth_bp.route('/logout')
def logout():
    session.pop("user", None)
    return redirect('/login')
