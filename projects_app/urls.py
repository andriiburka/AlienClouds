from django.urls import path
from projects_app.views import upload_project, project_details, all_projects


urlpatterns = (
    path('allprojects/', all_projects, name='all projects'),
    path('upload_project/', upload_project, name='upload_project'),
    path('project_details/', project_details, name='project_details'),
)
