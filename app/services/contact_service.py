from app.models.contact import ContactSubmission, db
from app.services.email_service import EmailService

class ContactService:
    @staticmethod
    def submit_contact(data: dict) -> ContactSubmission:
        """Create and save a new contact submission."""
        submission = ContactSubmission(
            name=data['name'].strip(),
            email=data['email'].strip(),
            subject=data['subject'].strip(),
            message=data['message'].strip(),
            status='submitted'
        )
        db.session.add(submission)
        db.session.commit()
        
        # Send notification email
        EmailService.send_notification(submission)
        
        return submission
