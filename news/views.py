from django.shortcuts import render, get_object_or_404
from .models import Article

def index(request):
    return render(request, 'news/template.html')

def article_list(request):
    articles = Article.objects.order_by('-published_date')  # Последние статьи
    return render(request, 'news/article_list.html', {'articles': articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'news/article_detail.html', {'article': article})
