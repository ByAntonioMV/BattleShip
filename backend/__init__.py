from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Cargar configuración
    app.config.from_object(Config)

    # Inicializar base de datos
    db.init_app(app)

    # Registrar blueprints (rutas)
    from app.routes import init_routes
    init_routes(app)

    return app
