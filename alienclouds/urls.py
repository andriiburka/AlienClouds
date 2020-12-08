
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('nechuek/', admin.site.urls),
    path('', include('alienclouds_app.urls')),
    path('', include('projects_app.urls')),
]
