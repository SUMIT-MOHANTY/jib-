from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Register SEO static routes
    from flask import send_from_directory
    
    @app.route('/robots.txt')
    def robots():
        return send_from_directory('static', 'robots.txt')
    
    @app.route('/sitemap.xml')
    def sitemap():
        return send_from_directory('static', 'sitemap.xml')
    
    return app
