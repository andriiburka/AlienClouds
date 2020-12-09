from django.urls import path
from projects_app.views import upload, all_projects


urlpatterns = (
    path('projects/', all_projects, name='all projects'),
    path('upload/', upload, name='upload'),
)
