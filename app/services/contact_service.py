from app import db
from app.models.contact import ContactSubmission
from app.services.email_service import send_notification

def submit_contact(data):
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
