from flask import request, jsonify
from app.services.validation_service import validate_contact_data
from app.services.contact_service import ContactService

def register_routes(app, db):
    @app.route('/api/contact', methods=['POST'])
    def submit_contact():
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Request body must be JSON'}), 400
        
        validation = validate_contact_data(data)
        if not validation.is_valid:
            return jsonify({'errors': validation.errors}), 400
        
        submission = ContactService.submit_contact(data, db)
        
        return jsonify({
            'message': 'Contact form submitted successfully',
            'id': submission.id
        }), 201
