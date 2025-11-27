from flask import Blueprint, jsonify
import mysql.connector
from config import Config

victorias_bp = Blueprint("victorias_bp", __name__)

@victorias_bp.route("/api/victorias", methods=["GET"])
def top10_victorias():
    try:
        conn = mysql.connector.connect(**Config.DB_URI)
        cursor = conn.cursor(dictionary=True)

        # Ejecuta la query del TOP 10
        cursor.execute(Config.SQL_SELECT_TOP10_VICTORIAS)
        resultados = cursor.fetchall()

        return jsonify({"top_10_jugadores": resultados}), 200

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

    finally:
        try:
            if cursor: cursor.close()
        except: pass
        try:
            if conn: conn.close()
        except: pass
