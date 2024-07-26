from main import EmailService, User, UserManager, Notification
import unittest
from unittest.mock import Mock, call


class TestEmailSystem(unittest.TestCase):
    def testEmail(self):
        emailService = Mock()

        userManager = UserManager(emailService)
        user1 = User("Indiana Jones", "Jones.Indiana291@gmail.com", True)
        user2 = User("Optimus Prime", "Autobot237@gmail.com", True)
        user3 = User("Jeff Bezos", "Jeff@gmail.com", True)
        users = [user1, user2, user3]

        user4 = User("Johnny Test", "Johnnytesting@yahoo.com", False)
        user5 = User("Average Jonas", "Jonas2131@hotmail.com", True)

        notification = Notification("Ambush!!", "There's an ambush from behind")

        userManager.register_user(user1)
        userManager.register_user(user2)
        userManager.register_user(user3)
        userManager.register_user(user4)

        userManager.send_notification_to_users(notification)

        # check if user1, 2 and 3 is sent an email or not.
        expected_calls = [call(user.email, notification.subject, notification.message) for user in users]
        emailService.send_email.assert_has_calls(expected_calls, any_order=True)

        # only 3 user will be sent an email, because user4 has email_preference as false and user5 is not registered.
        self.assertEqual(emailService.send_email.call_count, 3)

if __name__ == '__main__':
    unittest.main()
