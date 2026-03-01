from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

db = SQLAlchemy()
limiter = Limiter(key_func=get_remote_address, default_limits=["5 per minute"])

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    limiter.init_app(app)
    
    from app.routes import contact
    contact.register_routes(app, db)
    
    with app.app_context():
        db.create_all()
    
    @app.route('/')
    def index():
        from flask import send_from_directory
        return send_from_directory('static', 'index.html')
    
    return app
