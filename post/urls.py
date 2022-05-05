# articles/urls.py
from django.urls import path

from .views import ArticleView, ArticleDetailView,ContactView

app_name = 'post'
urlpatterns = [
    path('', ArticleView.as_view(), name="index"),
    path('<slug:slug>-<int:id>', ArticleDetailView.as_view(), name="article_detail"),
    path('contact', ContactView.as_view(), name="contact"),
]