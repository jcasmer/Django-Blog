from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import View, DetailView

from post.models import BlogArticle


class ArticleView(View):

    template_name = 'post/index.html'

    def get(self, request):
        '''
        Method get
        '''
        articles = BlogArticle.objects.filter(online=True).order_by('-publication')
        paginator = Paginator(articles, 5) # Show 5 articles per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request, self.template_name,  {'page_obj': page_obj})


class ArticleDetailView(DetailView):
    
    model = BlogArticle
    template_name = "post/article_detail.html"