from django.urls import path

from alienclouds_app.views import registerPage, IndexListView, contacts, upload
from alienclouds_app.views import loginPage
from alienclouds_app.views import logoutUser

from alienclouds_app.views import index
from alienclouds_app.views import blog

urlpatterns = (
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('upload/', upload, name='upload'),

    path('', index, name='index'),
    path('2/', IndexListView.as_view(), name='index2'),
    path('blog/', blog, name='blog'),
    path('contacts/', contacts, name='contacts'),
)
