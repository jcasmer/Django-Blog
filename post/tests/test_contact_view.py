from this import d
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse

from post.models import ContactRequest
from post.forms import ContactRequestForm
from post.views import ContactView


class ContactViewTests(TestCase):
    
    def test_get_view(self):
        
        url = reverse('post:contact')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_post_view(self):
        
        data = {'name':'test name', 'content': 'this is a content test', 'email': 'email@email.com' }
        url = reverse('post:contact')
        resp = self.client.post(url,data=data)
        self.assertEqual(resp.status_code, 302)

    def test_post_invalid_data(self):

        data = {'name':'test name', 'content': 'this is a content test', 'email': '' }
        url = reverse('post:contact')
        resp = self.client.post(url,data=data)
        self.assertNotEqual(resp.status_code, 400)

        