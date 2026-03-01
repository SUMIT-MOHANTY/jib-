# Contact Form Backend Service

Flask-based REST API for contact form submission.

## Setup

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   ```bash
   cp backend/.env.example backend/.env
   ```

3. Run the backend:
   ```bash
   python run.py
   ```

## API Endpoints

- `POST /api/contact` - Submit contact form

## Tech Stack

- Flask
- SQLAlchemy
- Flask-CORS
- python-dotenv
