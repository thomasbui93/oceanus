from django.test import TestCase
from user_management.utils.email import is_valid_email

class TestEmailUtils(TestCase):
    def test_email(self):
        self.assertEqual(is_valid_email('khoa.bui@smartbox.com'), True)
        self.assertEqual(is_valid_email('ac'), False)