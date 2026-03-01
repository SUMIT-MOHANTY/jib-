from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from app.models import db
from app.utils import limiter
from app.routes import register_routes


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)
    db.init_app(app)
    limiter.init_app(app)
    register_routes(app)

    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({'error': 'Bad request'}), 400

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({'error': 'Not found'}), 404

    @app.errorhandler(429)
    def rate_limit(e):
        return jsonify({'error': 'Too many requests'}), 429

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({'error': 'Internal server error'}), 500

    with app.app_context():
        db.create_all()

    return app
