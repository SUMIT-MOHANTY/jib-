from flask import Blueprint, request, jsonify
from app.services.validation_service import validate_contact_data
from app.services.contact_service import submit_contact
from app.utils.rate_limiter import limiter

bp = Blueprint('contact', __name__, url_prefix='/api')

@bp.route('/contact', methods=['POST'])
@limiter.limit("5 per minute")
def contact():
    data = request.get_json()
    
    validation = validate_contact_data(data)
    if not validation.is_valid:
        return jsonify({'errors': validation.errors}), 400
    
    submission = submit_contact(data)
    return jsonify(submission.to_dict()), 201
