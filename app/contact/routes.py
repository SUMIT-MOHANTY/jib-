from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models import db, ContactMessage

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('')
@login_required
def list():
    messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()
    return render_template('contact/list.html', messages=messages)

@contact_bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    message = ContactMessage.query.get_or_404(id)
    db.session.delete(message)
    db.session.commit()
    flash('Message deleted successfully', 'success')
    return redirect(url_for('contact.list'))
