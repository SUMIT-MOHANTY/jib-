import re

class ValidationService:
    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_required_fields(data, fields):
        missing = [f for f in fields if not data.get(f, '').strip()]
        return len(missing) == 0, missing
