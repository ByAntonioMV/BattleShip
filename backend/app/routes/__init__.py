from .loginRoute import login_bp
from .registerRoute import registro_bp
from .VictoriasRooute import victorias_bp

def init_routes(app):
    app.register_blueprint(login_bp)
    app.register_blueprint(registro_bp)
    app.register_blueprint(victorias_bp)
