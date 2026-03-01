import re

class ValidationService:
    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_name(name):
        return bool(name and len(name.strip()) >= 2)
    
    @staticmethod
    def validate_message(message):
        return bool(message and len(message.strip()) >= 10)
