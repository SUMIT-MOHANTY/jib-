class ValidationResult:
    def __init__(self, is_valid=True, errors=None):
        self.is_valid = is_valid
        self.errors = errors or []

def validate_contact_data(data):
    errors = []
    
    if not data.get('name'):
        errors.append('Name is required')
    elif len(data['name']) > 100:
        errors.append('Name must be at most 100 characters')
    
    if not data.get('email'):
        errors.append('Email is required')
    elif not _is_valid_email(data['email']):
        errors.append('Invalid email format')
    
    if not data.get('subject'):
        errors.append('Subject is required')
    elif len(data['subject']) > 200:
        errors.append('Subject must be at most 200 characters')
    
    if not data.get('message'):
        errors.append('Message is required')
    elif len(data['message']) > 2000:
        errors.append('Message must be at most 2000 characters')
    
    return ValidationResult(is_valid=len(errors) == 0, errors=errors)

def _is_valid_email(email):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
