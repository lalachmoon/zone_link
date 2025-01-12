from django.urls import path
from . import views

app_name = 'viewer'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_courier, name='search_courier'),
    path('map/', views.map, name='map'),
    path('save-polygons/', views.save_polygons, name='save_polygons'),
    path('polygon/edit/<int:polygon_id>/', views.edit_polygon, name='edit_polygon'),
    path('polygon/delete/<int:polygon_id>/', views.delete_polygon, name='delete_polygon'),
    path('get-polygons/', views.get_polygons, name='get_polygons'),
]
