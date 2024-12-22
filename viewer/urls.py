from django.urls import path
from . import views


urlpatterns = [
    path('search/', views.search_courier, name='search_courier'),
]