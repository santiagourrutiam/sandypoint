from django.conf.urls import include, url
from django.urls import path
from . import views

#Template Tagging
app_name = 'phonebook'

urlpatterns = [
    path('', views.frontPage, name='frontPage'),
    path('phonebook/',views.frontPage, name='frontPage'),
    path('addcontact/',views.addContact, name='addContact'),
    path('register/',views.registerNewUser, name='registerNewUser'),
    path('user_login/', views.user_login,name='user_login')
]
