import uuid
from app.models.contact import ContactSubmission
from app.services.email_service import EmailService

class ContactService:
    @staticmethod
    def submit_contact(data: dict) -> ContactSubmission:
        submission = ContactSubmission(
            id=str(uuid.uuid4()),
            name=data['name'],
            email=data['email'],
            subject=data['subject'],
            message=data['message']
        )
        
        # Send email notification
        EmailService.send_notification(submission)
        
        return submission
