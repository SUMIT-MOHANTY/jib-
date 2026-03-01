from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='../frontend/build', static_url_path='')
    app.config.from_object(config_class)
    db.init_app(app)
    
    from app.routes import contact
    app.register_blueprint(contact.bp)
    
    @app.route('/')
    def index():
        return app.send_static_file('index.html')
    
    return app
