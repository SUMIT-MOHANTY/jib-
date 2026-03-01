from datetime import datetime

class ContactSubmission:
    def __init__(self, id, name, email, subject, message, created_at=None, status='pending'):
        self.id = id
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message
        self.created_at = created_at or datetime.utcnow()
        self.status = status
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message,
            'created_at': self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at,
            'status': self.status
        }
