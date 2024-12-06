from django.test import TestCase
from .models import CustomUser

# Create your tests here.

class UserTestCase(TestCase):
    def test_user_creation(self):
        user = CustomUser.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="password"
        )
        self.assertEqual(user.username, "testuser")

