from flask import Blueprint, request, jsonify
from app.models import db, ContactSubmission
from app.services.contact_service import submit_contact
from app.services.email_service import send_notification
from app.services.validation_service import validate_contact_data
from app.utils.rate_limiter import limiter

contact_bp = Blueprint('contact', __name__)


@contact_bp.route('/api/contact', methods=['GET'])
def get_contacts():
    submissions = ContactSubmission.query.order_by(ContactSubmission.created_at.desc()).all()
    return jsonify([s.to_dict() for s in submissions]), 200


@contact_bp.route('/api/contact', methods=['POST'])
@limiter.limit("5 per minute")
def create_contact():
    data = request.get_json()
    validation = validate_contact_data(data)
    if not validation.valid:
        return jsonify({'error': 'Validation failed', 'details': validation.errors}), 400
    data['ip_address'] = request.remote_addr
    data['user_agent'] = request.headers.get('User-Agent', '')
    submission = submit_contact(data)
    send_notification(submission)
    return jsonify(submission.to_dict()), 201


@contact_bp.route('/api/contact/<int:id>', methods=['GET'])
def get_contact(id):
    submission = ContactSubmission.query.get_or_404(id)
    return jsonify(submission.to_dict()), 200


@contact_bp.route('/api/contact/<int:id>', methods=['PUT'])
def update_contact(id):
    submission = ContactSubmission.query.get_or_404(id)
    data = request.get_json()
    submission.is_read = data.get('is_read', submission.is_read)
    db.session.commit()
    return jsonify(submission.to_dict()), 200
