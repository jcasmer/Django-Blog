from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User

from post.models import ContactRequest
from post.forms import ContactRequestForm


class ContactRequestFormTests(TestCase):
    
    def create_contact_request(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        return ContactRequest.objects.create(name='test name', content='this is a content test', email= 'email@email.com')

    def test_valid_form(self):

        contact = self.create_contact_request()
        data = {'name': contact.name, 'content': contact.content, 'email':contact.email}
        form = ContactRequestForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):

        data = {'name': 'test name', 'content': 'this is a content test', 'email':''}
        form = ContactRequestForm(data=data)
        self.assertFalse(form.is_valid())