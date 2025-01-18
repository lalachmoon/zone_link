from django.urls import path
from . import views

app_name = 'viewer'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_courier, name='search_courier'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('subscribe/<str:plan_slug>/', views.subscribe, name='subscribe'),
    path('confirm-subscription/', views.confirm_subscription, name='confirm_subscription'),

]
