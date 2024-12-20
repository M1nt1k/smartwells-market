from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('contract_offer/', views.contract_offer, name='contract_offer'),
    path('privacy/', views.privacy, name='privacy'),
]