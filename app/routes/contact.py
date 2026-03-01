from flask import Blueprint, request, jsonify
from app.services.contact_service import ContactService

contact_bp = Blueprint('contact', __name__, url_prefix='/api/contact')

def register_routes(app):
    app.register_blueprint(contact_bp)

@contact_bp.route('/submit', methods=['POST'])
def submit_contact():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    result = ContactService.submit_contact(data)
    
    if result.get('success'):
        return jsonify(result), 201
    return jsonify(result), 400

@contact_bp.route('/submissions', methods=['GET'])
def get_submissions():
    result = ContactService.get_all_submissions()
    return jsonify(result), 200

@contact_bp.route('/submissions/<int:submission_id>', methods=['GET'])
def get_submission(submission_id):
    result = ContactService.get_submission_by_id(submission_id)
    if result.get('submission'):
        return jsonify(result), 200
    return jsonify(result), 404
