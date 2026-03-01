from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    from app.errors import register_error_handlers
    register_error_handlers(app)
    
    from app.routes.contact import register_routes
    register_routes(app)
    
    return app
