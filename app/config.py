import os

class Config:
    SECRET_KEY = "dev-placeholder-secret-key-change-in-production"  # TODO: Replace with secure key for production
    SQLALCHEM_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///portfolio.db')
    SQLALCHEM_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'filesystem'
    PERMANENT_SESSION_LIFETIME = 3600
