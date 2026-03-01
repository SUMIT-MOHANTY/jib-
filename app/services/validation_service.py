import re

class ValidationResult:
    def __init__(self, is_valid, errors=None):
        self.is_valid = is_valid
        self.errors = errors or []

def validate_contact_data(data):
    errors = []
    
    if not data.get('name') or len(data['name']) < 1 or len(data['name']) > 100:
        errors.append('Name is required and must be between 1-100 characters')
    
    email = data.get('email', '')
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not email or not re.match(email_pattern, email):
        errors.append('Valid email is required')
    
    if not data.get('subject') or len(data['subject']) < 1 or len(data['subject']) > 200:
        errors.append('Subject is required and must be between 1-200 characters')
    
    if not data.get('message') or len(data['message']) < 1 or len(data['message']) > 2000:
        errors.append('Message is required and must be between 1-2000 characters')
    
    return ValidationResult(len(errors) == 0, errors)
