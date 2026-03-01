from flask import jsonify, render_template, request

ERROR_MESSAGES = {
    404: {"code": "NOT_FOUND", "message": "Resource not found"},
    500: {"code": "INTERNAL_ERROR", "message": "An internal server error occurred"},
    400: {"code": "BAD_REQUEST", "message": "Invalid input data"},
    429: {"code": "RATE_LIMITED", "message": "Too many requests"}
}

def register_error_handlers(app):
    @app.errorhandler(404)
    def handle_404(error):
        if request.is_json or request.path.startswith('/api'):
            return jsonify({"error": ERROR_MESSAGES[404]}), 404
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def handle_500(error):
        if request.is_json or request.path.startswith('/api'):
            return jsonify({"error": ERROR_MESSAGES[500]}), 500
        return render_template('errors/500.html'), 500

    @app.errorhandler(400)
    def handle_400(error):
        message = str(error) if str(error) else ERROR_MESSAGES[400]["message"]
        return jsonify({"error": {"code": "BAD_REQUEST", "message": message}}), 400

    @app.errorhandler(429)
    def handle_429(error):
        return jsonify({"error": ERROR_MESSAGES[429]}), 429

    return app
