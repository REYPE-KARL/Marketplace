from django.test import TestCase

# Create your tests here.
from .models import Contact


class UsersManagersTests(TestCase):

    def test_create_contact(self):
        contact = Contact()
        contact.name = 'normal'
        contact.email = 'normal@user.com'
        contact.subject = 'normal is here and now.'
        contact.save()

        self.assertEqual(contact.name, 'normal')
        self.assertEqual(contact.email, 'normal@user.com')
        self.assertEqual(contact.subject, 'normal is here and now.')
        self.assertEqual(str(contact), f'{contact.name}')