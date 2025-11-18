from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importar y registrar rutas
    from app.server.routes.loginRoute import auth
    app.register_blueprint(auth, url_prefix="/api/auth")

    return app
