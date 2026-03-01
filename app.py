from flask import Flask
from config import Config
from models import db
from schemas import ma
from routes.project_routes import project_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    ma.init_app(app)
    
    app.register_blueprint(project_bp)
    
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
