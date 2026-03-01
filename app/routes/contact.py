from flask import request, jsonify
from app.services.contact_service import submit_contact

def register_routes(app):
    @app.route('/api/contact', methods=['POST'])
    def contact():
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        if not name or not email or not message:
            return jsonify({'error': 'Missing required fields'}), 400
        
        submission = submit_contact(data)
        return jsonify({'success': True, 'id': submission.id}), 201
