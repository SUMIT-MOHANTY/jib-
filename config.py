import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///contacts.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Rate limiting
    RATELIMIT_ENABLED = True
    RATELIMIT_DEFAULT = "5 per minute"
    RATELIMIT_STORAGE_URL = os.environ.get('RATELIMIT_STORAGE_URL', 'memory://')
    
    # Email configuration (placeholder - replace with real SendGrid/Mailgun API key)
    SMTP_HOST = os.environ.get('SMTP_HOST', 'smtp.example.com')
    SMTP_PORT = int(os.environ.get('SMTP_PORT', 587))
    SMTP_USER = os.environ.get('SMTP_USER', '')
    SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD', '')
    SMTP_FROM = os.environ.get('SMTP_FROM', 'noreply@example.com')
    SMTP_TO = os.environ.get('SMTP_TO', 'admin@example.com')
