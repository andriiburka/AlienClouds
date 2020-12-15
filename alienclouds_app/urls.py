from django.urls import path

from alienclouds_app.views import \
    index, \
    loginPage, \
    logoutUser, \
    registerPage, \
    all_projects, \
    IndexListView, \
    upload_project, \
    project_details


urlpatterns = (
    path('', index, name='index'),
    path('cbv/', IndexListView.as_view(), name='index2'),

    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),

    path('allprojects/', all_projects, name='all_projects'),
    path('upload_project/', upload_project, name='upload_project'),

    path('project_details/<int:pk>', project_details, name='project_details'),
)
