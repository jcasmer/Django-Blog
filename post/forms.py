
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from post.models import BlogArticle, ContactRequest


class ContactRequestForm(ModelForm):                    
            
    class Meta:

        model = ContactRequest
        fields = ['name','email','content']