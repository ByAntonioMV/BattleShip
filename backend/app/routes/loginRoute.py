from flask import Blueprint, request, jsonify
import mysql.connector
import jwt
from datetime import datetime, timedelta
from config import Config

login_bp = Blueprint("login_bp", __name__)

@login_bp.route("/api/login", methods=["POST"])
def login_usuario():
    data = request.json

    nombre = data.get("nombre")
    password = data.get("pass")  # mismo campo que registro

    # Validación mínima
    if not nombre or not password:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    conn = None
    cursor = None

    try:
        # Conexión usando Config.DB_URI
        conn = mysql.connector.connect(**Config.DB_URI)
        cursor = conn.cursor(dictionary=True)

        # Query desde el config
        cursor.execute(Config.SQL_SELECT_USUARIO_BY_NAME, (nombre,))
        usuario = cursor.fetchone()

        if not usuario:
            return jsonify({"error": "Usuario no encontrado"}), 404

        # Comparar contraseñas (sin hash en tu sistema actual)
        if usuario["pass"] != password:
            return jsonify({"error": "Contraseña incorrecta"}), 401

        # Crear JWT
        token = jwt.encode(
            {
                "UserID": usuario["UserID"],
                "nombre": usuario["nombre"],
                "exp": datetime.utcnow() + timedelta(hours=12)
            },
            Config.SECRET_KEY,
            algorithm="HS256"
        )

        return jsonify({
            "mensaje": "Login exitoso",
            "token": token,
            "usuario": usuario
        }), 200

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
