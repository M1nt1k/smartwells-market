from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.article_list, name='article_list'),  # Главная страница
    path('<slug:slug>/', views.article_detail, name='article_detail'),  # Детальная страница статьи
]