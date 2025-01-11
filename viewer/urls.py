from django.urls import path
from . import views

app_name = 'viewer'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_courier, name='search_courier'),
    path('interactive_map/', views.interactive_map, name='interactive_map'),
    path('polygons/', views.manage_polygons, name='manage_polygons'),
    path('api/polygons/', views.get_polygons, name='get_polygons'),
]
