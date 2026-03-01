from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import Config

limiter = Limiter(key_func=get_remote_address, default_limits=["200 per day", "50 per hour"])

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    limiter.init_app(app)
    
    from app.routes.contact import register_routes
    register_routes(app)
    
    return app
