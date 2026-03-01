import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///portfolio.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # SEO Configuration
    SITE_NAME = 'Portfolio API'
    SITE_URL = os.environ.get('SITE_URL', 'http://localhost:5000')
    SITE_DESCRIPTION = 'Portfolio Management API - Manage your portfolio projects with RESTful endpoints'
    TWITTER_HANDLE = '@portfolio'
    OG_IMAGE_URL = os.environ.get('OG_IMAGE_URL', 'http://localhost:5000/static/og-default.jpg')
    AUTHOR_NAME = os.environ.get('AUTHOR_NAME', 'Portfolio Owner')
    
    # Canonical URLs
    API_BASE_URL = SITE_URL + '/api'
    JSON_API_MIMETYPE = 'application/vnd.api+json'
