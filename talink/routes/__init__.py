from flask import Flask

def register_routes(app: Flask):
    # Home (/)
    from .home import home_bp
    app.register_blueprint(home_bp)
