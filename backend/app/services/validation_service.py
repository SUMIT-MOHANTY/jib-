import re

def validate_contact_data(data):
    errors = []
    
    name = data.get('name', '')
    if not name or len(name.strip()) < 1:
        errors.append({'field': 'name', 'message': 'Name is required'})
    elif len(name) > 100:
        errors.append({'field': 'name', 'message': 'Name must be less than 100 characters'})
    
    email = data.get('email', '')
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not email:
        errors.append({'field': 'email', 'message': 'Email is required'})
    elif not re.match(email_pattern, email):
        errors.append({'field': 'email', 'message': 'Invalid email format'})
    
    subject = data.get('subject', '')
    if not subject or len(subject.strip()) < 1:
        errors.append({'field': 'subject', 'message': 'Subject is required'})
    elif len(subject) > 200:
        errors.append({'field': 'subject', 'message': 'Subject must be less than 200 characters'})
    
    message = data.get('message', '')
    if not message or len(message.strip()) < 1:
        errors.append({'field': 'message', 'message': 'Message is required'})
    elif len(message) > 2000:
        errors.append({'field': 'message', 'message': 'Message must be less than 2000 characters'})
    
    return {'valid': len(errors) == 0, 'errors': errors}
