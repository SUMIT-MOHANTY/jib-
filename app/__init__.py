from flask import Flask
from app.routes.contact import register_routes

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    register_routes(app)
    return app

app = create_app()
