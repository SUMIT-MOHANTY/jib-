from app import db
from app.models.contact import ContactSubmission
from app.services.email_service import EmailService
from datetime import datetime

class ContactService:
    @staticmethod
    def submit_contact(data):
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()
        
        if not name or not email or not message:
            return {'success': False, 'error': 'Name, email, and message are required'}
        
        if '@' not in email:
            return {'success': False, 'error': 'Invalid email address'}
        
        submission = ContactSubmission(
            name=name,
            email=email,
            subject=subject,
            message=message,
            status='pending'
        )
        
        db.session.add(submission)
        db.session.commit()
        
        try:
            EmailService.send_notification(submission)
        except Exception as e:
            print(f'Email notification failed: {e}')
        
        return {'success': True, 'submission': submission.to_dict()}
    
    @staticmethod
    def get_all_submissions():
        submissions = ContactSubmission.query.order_by(ContactSubmission.created_at.desc()).all()
        return {'submissions': [s.to_dict() for s in submissions]}
    
    @staticmethod
    def get_submission_by_id(submission_id):
        submission = ContactSubmission.query.get(submission_id)
        if not submission:
            return {'success': False, 'error': 'Submission not found'}
        return {'success': True, 'submission': submission.to_dict()}
