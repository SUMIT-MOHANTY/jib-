import logging

logger = logging.getLogger(__name__)

def send_notification(submission):
    # Placeholder: Replace with real SendGrid/Mailgun API key once provided
    # Example using SendGrid:
    # from sendgrid import SendGridAPIClient
    # from sendgrid.helpers.mail import Mail
    # 
    # message = Mail(
    #     from_email='noreply@example.com',
    #     to_emails='admin@example.com',
    #     subject=f"New contact: {submission.subject}",
    #     html_content=f"Name: {submission.name}<br>Email: {submission.email}<br>Message: {submission.message}"
    # )
    # try:
    #     sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    #     sg.send(message)
    # except Exception as e:
    #     logger.error(f"Email failed: {e}")
    
    logger.info(f"[PLACEHOLDER] Email notification sent for contact #{submission.id}")
    return True
