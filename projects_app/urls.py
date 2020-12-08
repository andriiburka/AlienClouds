from django.urls import path

from alienclouds_app.views import all_projects

urlpatterns = (
    path('projects/', all_projects, name='all projects'),

)
