import uuid
from datetime import datetime

class ContactSubmission:
    def __init__(self, data):
        self.id = str(uuid.uuid4())
        self.name = data.get('name')
        self.email = data.get('email')
        self.message = data.get('message')
        self.created_at = datetime.utcnow()

def submit_contact(data):
    submission = ContactSubmission(data)
    return submission
