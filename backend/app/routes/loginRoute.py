from flask import Blueprint, jsonify

login_bp = Blueprint("login", __name__, url_prefix="/auth")

@login_bp.get("/login")
def login():
    return jsonify({"message": "Login OK"})
