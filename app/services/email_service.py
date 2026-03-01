import logging
from app.models.contact import ContactSubmission

logger = logging.getLogger(__name__)

class EmailService:
    @staticmethod
    def send_notification(submission: ContactSubmission) -> bool:
        """
        Send notification email for new contact submission.
        In production, this would integrate with SMTP.
        """
        try:
            # Simulate email sending - in production, use Flask-Mail or similar
            logger.info(f"Notification email would be sent for submission {submission.id}")
            logger.info(f"To: {submission.email}, Subject: {submission.subject}")
            return True
        except Exception as e:
            logger.error(f"Failed to send email: {str(e)}")
            return False
