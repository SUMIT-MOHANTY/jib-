from flask import Flask, jsonify, send_from_directory
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Serve static SEO files
    @app.route('/robots.txt')
    def robots():
        return send_from_directory('static', 'robots.txt')
    
    @app.route('/sitemap.xml')
    def sitemap():
        return send_from_directory('static', 'sitemap.xml')
    
    # Health check endpoint with SEO
    @app.route('/')
    @app.route('/health')
    def health():
        return jsonify({
            'status': 'healthy',
            'service': app.config['SITE_NAME'],
            'version': '1.0.0',
            '_meta': {
                'title': app.config['SITE_NAME'],
                'description': app.config['SITE_DESCRIPTION']
            }
        })
    
    # Register blueprints (will be added when routes exist)
    # from routes.project_routes import project_bp
    # app.register_blueprint(project_bp, url_prefix='/api')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
