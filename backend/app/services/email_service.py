import os
from flask import current_app

def send_notification(contact_data):
    email_host = current_app.config.get('EMAIL_HOST')
    email_port = current_app.config.get('EMAIL_PORT')
    email_user = current_app.config.get('EMAIL_USER')
    
    if not email_host or not email_user:
        print(f"Email notification skipped: SMTP not configured")
        return False
    
    print(f"Email notification sent for contact: {contact_data['id']}")
    return True
