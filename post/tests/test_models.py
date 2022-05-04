from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User

from post.models import BlogArticle, ContactRequest


class BlogArticleModelTests(TestCase):

    def create_article(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        return BlogArticle.objects.create(title="test title", content="this is a content test", author= self.user)
    
    def test_blog_article_creation(self):
        article = self.create_article()
        self.assertTrue(isinstance(article, BlogArticle))
        self.assertIs(article.online, True)
        self.assertEqual(article.slug, 'test-title')
        self.assertEqual(article.title, 'test title')
        self.assertEqual(article.content, 'this is a content test')
        self.assertEqual(article.get_absolute_url(), '/test-title-'+ str(article.id))
        self.assertEqual(article.__str__(), 'test title')


class ContactRequestModelTests(TestCase):

    def create_contact_request(self):
        self.factory = RequestFactory()
        return ContactRequest.objects.create(name="test name", content="this is a content test", email= 'email@email.com')
    
    def test_blog_article_creation(self):
        contact = self.create_contact_request()
        self.assertTrue(isinstance(contact, ContactRequest))
        self.assertEqual(contact.__str__(), 'test name')