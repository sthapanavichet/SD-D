class EmailService:
    def send_email(self, to_email, subject, message):
        # In a real implementation, this would send an email
        print(f"Email sent to: {to_email}\nSubject: {subject}\nMessage:{message}")

class UserManager:
    def __init__(self, email_service):
        self.email_service = email_service
        self.users = []
    def register_user(self, user):
        self.users.append(user)

    def send_notification_to_users(self, notification):
        for user in self.users:
            if user.email_preference:
                self.email_service.send_email(user.email, notification.subject,notification.message)

class User:
    def __init__(self, name, email, email_preference=True):
        self.name = name
        self.email = email
        self.email_preference = email_preference

class Notification:
    def __init__(self, subject, message):
        self.subject = subject
        self.message = message