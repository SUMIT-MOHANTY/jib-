from flask import Flask
from flask_login import LoginManager
from flask_session import Session
from app.models import db, Admin

login_manager = LoginManager()
session_app = Session()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    db.init_app(app)
    session_app.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(Admin, int(user_id))
    
    from app.auth.routes import auth_bp
    from app.dashboard.routes import dashboard_bp
    from app.projects.routes import projects_bp
    from app.skills.routes import skills_bp
    from app.about.routes import about_bp
    from app.contact.routes import contact_bp
    
    app.register_blueprint(auth_bp, url_prefix='/admin')
    app.register_blueprint(dashboard_bp, url_prefix='/admin')
    app.register_blueprint(projects_bp, url_prefix='/admin/projects')
    app.register_blueprint(skills_bp, url_prefix='/admin/skills')
    app.register_blueprint(about_bp, url_prefix='/admin/about')
    app.register_blueprint(contact_bp, url_prefix='/admin/contact')
    
    with app.app_context():
        db.create_all()
        if not Admin.query.filter_by(username='admin').first():
            admin = Admin(username='admin')
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
    
    return app
