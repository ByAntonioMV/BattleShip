from flask import Blueprint, request, jsonify
import mysql.connector
from config import Config

registro_bp = Blueprint("registro_bp", __name__)

@registro_bp.route("/api/registro", methods=["POST"])
def registrar_usuario():
    data = request.json

    nombre = data.get("nombre")
    password = data.get("pass")
    dinero = data.get("dinero")
    victorias = data.get("victorias")
    derrotas = data.get("derrotas")
    mazo = data.get("MazoSeleccionado")

    # Validación mínima
    if not nombre or not password:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    try:
        # Conexión con mysql.connector usando Config.DB_URI
        conn = mysql.connector.connect(**Config.DB_URI)
        cursor = conn.cursor()

        # Ejecutar query del Config
        cursor.execute(
            Config.SQL_INSERT_USUARIO,
            (nombre, password, dinero, victorias, derrotas, mazo)
        )

        conn.commit()
        return jsonify({"mensaje": "Usuario registrado con éxito"}), 201

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

    finally:
        try:
            if cursor:
                cursor.close()
        except:
            pass

        try:
            if conn:
                conn.close()
        except:
            pass
