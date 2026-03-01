from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from app.models.skills import db
from app.routes.skills import register_routes

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skills.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    limiter = Limiter(
        key_func=get_remote_address,
        app=app,
        default_limits=[]
    )
    
    register_routes(app)
    
    with app.app_context():
        db.create_all()
    
    return app
