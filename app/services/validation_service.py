import re


class ValidationResult:
    def __init__(self, valid: bool, errors: list = None):
        self.valid = valid
        self.errors = errors or []


def validate_contact_data(data: dict) -> ValidationResult:
    errors = []

    if not data.get('name') or len(data.get('name', '')) < 1:
        errors.append('Name is required')
    elif len(data.get('name', '')) > 100:
        errors.append('Name must be less than 100 characters')

    email = data.get('email', '')
    if not email:
        errors.append('Email is required')
    elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        errors.append('Invalid email format')

    if not data.get('subject') or len(data.get('subject', '')) < 1:
        errors.append('Subject is required')
    elif len(data.get('subject', '')) > 200:
        errors.append('Subject must be less than 200 characters')

    if not data.get('message') or len(data.get('message', '')) < 1:
        errors.append('Message is required')
    elif len(data.get('message', '')) > 2000:
        errors.append('Message must be less than 2000 characters')

    return ValidationResult(valid=len(errors) == 0, errors=errors)
