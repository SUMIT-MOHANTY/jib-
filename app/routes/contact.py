from flask import Blueprint, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from app.services.validation_service import ValidationService
from app.services.contact_service import ContactService
from app.models.contact import db

limiter = Limiter(key_func=get_remote_address)
contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/api/contact', methods=['POST'])
def submit_contact():
    data = request.get_json()
    
    # Validate input
    is_valid, errors = ValidationService.validate_contact_data(data)
    if not is_valid:
        return jsonify({'success': False, 'errors': errors}), 400
    
    try:
        submission = ContactService.submit_contact(data)
        return jsonify({
            'success': True,
            'message': 'Thank you for your message! We will get back to you soon.',
            'id': submission.id
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': 'An error occurred. Please try again.'}), 500

def register_routes(app):
    app.register_blueprint(contact_bp)
