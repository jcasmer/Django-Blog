from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse

from post.views import ArticleView


class ArticleViewTests(TestCase):
    
    def test_arcticle_view(self):
        
        url = reverse('post:index')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['page_obj'].number,1)

        