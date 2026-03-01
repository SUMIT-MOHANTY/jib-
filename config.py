import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///skills.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RATELIMIT_ENABLED = True
    RATELIMIT_STORAGE_URL = 'memory://'
