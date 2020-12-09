from django.urls import path

from alienclouds_app.views import registerPage, IndexListView, contacts
from alienclouds_app.views import loginPage
from alienclouds_app.views import logoutUser

from alienclouds_app.views import index
from alienclouds_app.views import blog

urlpatterns = (
    path('', index, name='index'),
    path('cbv/', IndexListView.as_view(), name='index2'),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('blog/', blog, name='blog'),
    path('contacts/', contacts, name='contacts'),
)
