from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)
    
    # Register blueprints
    from app.routes.portfolio import portfolio_bp
    app.register_blueprint(portfolio_bp, url_prefix="/api/portfolio")
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    @app.route("/")
    def index():
        return {"message": "Portfolio API", "status": "running"}
    
    return app
