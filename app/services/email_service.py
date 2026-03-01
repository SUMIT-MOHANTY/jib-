from app.models.contact import ContactSubmission

class EmailService:
    @staticmethod
    def send_notification(submission: ContactSubmission) -> bool:
        # In production, integrate with SMTP server
        # For now, simulate successful email sending
        print(f"[EMAIL] Notification sent for submission: {submission.id}")
        return True
