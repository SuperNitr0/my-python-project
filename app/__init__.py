from flask import Flask

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Welcome to the Flask App!"

    return app
