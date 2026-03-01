from datetime import datetime
import uuid

def submit_contact(data):
    submission_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()
    
    contact_data = {
        'id': submission_id,
        'name': data['name'],
        'email': data['email'],
        'subject': data['subject'],
        'message': data['message'],
        'created_at': timestamp,
        'status': 'pending'
    }
    
    from app.services.email_service import send_notification
    send_notification(contact_data)
    
    return {
        'id': submission_id,
        'status': 'success',
        'message': 'Contact form submitted successfully'
    }
