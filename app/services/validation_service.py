import re
from typing import Dict, Tuple, Optional

class ValidationService:
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    @staticmethod
    def validate_contact_data(data: dict) -> Tuple[bool, Optional[dict]]:
        errors = {}
        
        # Name validation
        name = data.get('name', '').strip()
        if not name:
            errors['name'] = 'Name is required'
        elif len(name) > 100:
            errors['name'] = 'Name must be 100 characters or less'
        
        # Email validation
        email = data.get('email', '').strip()
        if not email:
            errors['email'] = 'Email is required'
        elif not ValidationService.EMAIL_REGEX.match(email):
            errors['email'] = 'Invalid email format'
        
        # Subject validation
        subject = data.get('subject', '').strip()
        if not subject:
            errors['subject'] = 'Subject is required'
        elif len(subject) > 200:
            errors['subject'] = 'Subject must be 200 characters or less'
        
        # Message validation
        message = data.get('message', '').strip()
        if not message:
            errors['message'] = 'Message is required'
        elif len(message) > 2000:
            errors['message'] = 'Message must be 2000 characters or less'
        
        if errors:
            return False, errors
        return True, None
