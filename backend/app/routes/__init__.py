from .loginRoute import login_bp

def init_routes(app):
    app.register_blueprint(login_bp)
