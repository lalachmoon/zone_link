"""
URL configuration for zone_link project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from viewer import views

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Include app URL configurations
    path('', include('viewer.urls')),  # Routes for viewer app
    path('accounts/', include('accounts.urls')),  # Routes for accounts app
    path('map/', views.map, name='map'),
    path('save-polygons/', views.save_polygons, name='save_polygons'),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

