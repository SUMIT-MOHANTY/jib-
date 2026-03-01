from flask import Flask
from flask_cors import CORS
from config import config_by_name
import os

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config_by_name.get(config_name, config_by_name['default']))
    
    CORS(app)
    
    from app.routes.contact import register_routes
    register_routes(app)
    
    return app
