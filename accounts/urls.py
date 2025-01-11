from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import SubmittableLoginView, SubmittablePasswordChangeView, ProfileView

app_name = 'accounts'

urlpatterns = [
    path('login/', SubmittableLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', SubmittablePasswordChangeView.as_view(), name='password_change'),
]
