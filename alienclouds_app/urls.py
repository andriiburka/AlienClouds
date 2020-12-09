from django.urls import path

from alienclouds_app.views import index, registerPage, IndexListView, contacts, loginPage, logoutUser

urlpatterns = (
    path('', index, name='index'),
    path('cbv/', IndexListView.as_view(), name='index2'),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('contacts/', contacts, name='contacts'),
)
