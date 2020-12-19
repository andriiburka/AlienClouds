from django.urls import path

from alienclouds_app.views import index, IndexListView, project_edit, project_delete
from alienclouds_app.views import item_details, project_details
from alienclouds_app.views import registerPage, loginPage, logoutUser
from alienclouds_app.views import shop, projects, upload_project, upload_item

urlpatterns = (
    path('', index, name='index'),
    path('cbv/', IndexListView.as_view(), name='index2'),

    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),

    path('projects/', projects, name='projects'),
    path('upload_project/', upload_project, name='upload_project'),  # create
    path('project_details/<int:pk>/', project_details, name='project_details'),  # read
    path('project_edit/<int:pk>/edit/', project_edit, name='project_edit'),  # edit
    path('project_delete/<int:pk>/delete/', project_delete, name='project_delete'),  # delete

    path('upload_item/', upload_item, name='upload_item'),
    path('shop/', shop, name='shop'),
    path('item_details/<int:pk>/', item_details, name='item_details'),
)
