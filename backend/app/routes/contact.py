from flask import Blueprint, request, jsonify
from app.services.validation_service import validate_contact_data
from app.services.contact_service import submit_contact

contact_bp = Blueprint('contact', __name__, url_prefix='/api')

@contact_bp.route('/contact', methods=['POST'])
def submit_contact_form():
    data = request.get_json()
    
    validation_result = validate_contact_data(data)
    if not validation_result['valid']:
        return jsonify({'errors': validation_result['errors']}), 400
    
    result = submit_contact(data)
    return jsonify(result), 201

def register_routes(app):
    app.register_blueprint(contact_bp)
