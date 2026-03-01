from app.models.contact import ContactSubmission
from app.services.email_service import send_notification

class ContactService:
    @staticmethod
    def submit_contact(data, db):
        submission = ContactSubmission(
            name=data['name'],
            email=data['email'],
            subject=data['subject'],
            message=data['message']
        )
        db.session.add(submission)
        db.session.commit()
        
        send_notification(submission)
        
        return submission
