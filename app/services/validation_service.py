import re
from dataclasses import dataclass
from typing import Optional

@dataclass
class ValidationResult:
    is_valid: bool
    errors: list
    
class ValidationService:
    EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    @staticmethod
    def validate_contact_data(data: dict) -> ValidationResult:
        errors = []
        
        if not data.get('name') or len(data['name']) < 1:
            errors.append('Name is required')
        elif len(data['name']) > 100:
            errors.append('Name must be less than 100 characters')
        
        email = data.get('email', '')
        if not email:
            errors.append('Email is required')
        elif not ValidationService.EMAIL_PATTERN.match(email):
            errors.append('Invalid email format')
        
        if not data.get('subject') or len(data['subject']) < 1:
            errors.append('Subject is required')
        elif len(data['subject']) > 200:
            errors.append('Subject must be less than 200 characters')
        
        if not data.get('message') or len(data['message']) < 1:
            errors.append('Message is required')
        elif len(data['message']) > 2000:
            errors.append('Message must be less than 2000 characters')
        
        return ValidationResult(is_valid=len(errors) == 0, errors=errors)
