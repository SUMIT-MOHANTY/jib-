from flask import request, jsonify
from app.limiter import limiter
from app.services.validation_service import ValidationService
from app.services.contact_service import ContactService

def register_routes(app):
    @app.route('/api/contact', methods=['POST'])
    @limiter.limit("5 per minute")
    def submit_contact():
        data = request.get_json()
        
        if not data:
            return jsonify({'success': False, 'errors': ['Request body is required']}), 400
        
        # Validate input
        validation_result = ValidationService.validate_contact_data(data)
        if not validation_result.is_valid:
            return jsonify({'success': False, 'errors': validation_result.errors}), 400
        
        # Process submission
        submission = ContactService.submit_contact(data)
        
        return jsonify({
            'success': True,
            'submission_id': submission.id
        }), 201
