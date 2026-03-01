class EmailService:
    @staticmethod
    def send_notification(submission):
        print(f'Email notification sent for submission {submission.id}')
        print(f'From: {submission.email}')
        print(f'Subject: {submission.subject}')
        return True
