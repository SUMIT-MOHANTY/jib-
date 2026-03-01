from flask import Flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from app.models.contact import db

def create_app(config_class=None):
    app = Flask(__name__)
    
    if config_class:
        app.config.from_object(config_class)
    else:
        from config import Config
        app.config.from_object(Config)
    
    CORS(app)
    db.init_app(app)
    
    # Initialize rate limiter
    Limiter(app, key_func=get_remote_address)
    
    with app.app_context():
        db.create_all()
    
    from app.routes.contact import register_routes
    register_routes(app)
    
    # Serve static frontend
    @app.route('/')
    def index():
        from flask import render_template
        return render_template('index.html')
    
    return app
