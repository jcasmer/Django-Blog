
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from django.urls import reverse
from libraries.model import BaseModel

class BlogArticle(BaseModel):
    
    title = models.CharField('Title',max_length=50)
    content = models.TextField('Content')
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    online = models.BooleanField('Online', default=True)
    publication = models.DateTimeField('Publication date', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:article_detail', kwargs={'slug': self.slug , 'id': str(self.id)})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogArticle, self).save(*args, **kwargs)


class ContactRequest(BaseModel):

    name = models.CharField('name',max_length=250)
    email = models.EmailField('Email')
    content = models.TextField('Content')
    date = models.DateTimeField('Date', auto_now_add=True)

    def __str__(self):
        return self.name