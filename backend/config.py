# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "super-secret-key"

    # =====================
    #   DATOS DE CONEXIÓN
    # =====================

    DB_USER = os.environ.get('DB_USER', 'alain')
    DB_PASS = os.environ.get('DB_PASS', '12345')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', '3306')
    DB_NAME = os.environ.get('DB_NAME', 'BatallaNavalDB')

    # Para SQLAlchemy
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Para mysql.connector (tu ruta de registro)
    DB_URI = {
        "host": DB_HOST,
        "user": DB_USER,
        "password": DB_PASS,
        "database": DB_NAME,
        "port": DB_PORT
    }

    # =====================
    #       QUERIES
    # =====================

    SQL_SELECT_TOP10_VICTORIAS = """
    SELECT nombre, victorias
    FROM Usuario
    ORDER BY victorias DESC
    LIMIT 10;
    """

    SQL_SELECT_USUARIO_BY_NAME = """
    SELECT UserID, nombre, pass, dinero, victorias, derrotas, MazoSeleccionado
    FROM Usuario
    WHERE nombre = %s;
    """
    SQL_INSERT_USUARIO = """
    INSERT INTO Usuario (nombre, pass, dinero, victorias, derrotas, MazoSeleccionado)
    VALUES (%s, %s, %s, %s, %s, %s);
    """

    SQL_SELECT_USUARIOS = "SELECT * FROM Usuario;"

    SQL_SELECT_USUARIO_BY_ID = "SELECT * FROM Usuario WHERE UserID = %s;"

    SQL_UPDATE_USUARIO = """
    UPDATE Usuario
    SET nombre=%s, pass=%s, dinero=%s, victorias=%s, derrotas=%s, MazoSeleccionado=%s
    WHERE UserID=%s;
    """
