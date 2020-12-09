from django.urls import path
from projects_app.views import my_profile, all_projects


urlpatterns = (
    path('projects/', all_projects, name='all projects'),
    path('myprofile/', my_profile, name='myprofile'),
)
