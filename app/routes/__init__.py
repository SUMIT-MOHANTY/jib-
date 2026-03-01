from .projects import projects_bp
from .about import about_bp
from .blog import blog_bp
from .contact import contact_bp


def register_routes(app):
    app.register_blueprint(projects_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(blog_bp)
    app.register_blueprint(contact_bp)
