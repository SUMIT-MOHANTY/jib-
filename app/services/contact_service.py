from app.models import db, ContactSubmission


def submit_contact(data: dict) -> ContactSubmission:
    submission = ContactSubmission(
        name=data.get('name'),
        email=data.get('email'),
        subject=data.get('subject'),
        message=data.get('message'),
        ip_address=data.get('ip_address'),
        user_agent=data.get('user_agent')
    )
    db.session.add(submission)
    db.session.commit()
    return submission
