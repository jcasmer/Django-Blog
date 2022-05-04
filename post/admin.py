

from django.contrib import admin
from .models import BlogArticle, ContactRequest


@admin.register(BlogArticle)
class BlogArticleAdmin(admin.ModelAdmin):
    ordering = ['publication']
    fields = ['title','content','slug','author','online']
    prepopulated_fields = {"slug": ("title",)}


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    ordering = ['date']   
    fields = ['name','email','content']

    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request,obj=None):
        return False
