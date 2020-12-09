from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('alien/', admin.site.urls),
    path('', include('alienclouds_app.urls')),
    path('', include('projects_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
