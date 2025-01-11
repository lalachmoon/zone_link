from django.urls import path
from . import views

app_name = 'viewer'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_courier, name='search_courier'),
]
