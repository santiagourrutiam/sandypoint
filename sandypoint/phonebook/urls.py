from django.conf.urls import include, url
from django.urls import path
from phonebook import views

#Template Tagging
app_name = 'phonebook'

urlpatterns = [
    path('', views.userLogin, name='userLogin'),
    path('phonebook/',views.showAllContacts, name='showAllContacts'),
    path('addcontact/',views.addContact, name='addContact'),
    path('register/',views.registerNewUser, name='registerNewUser'),
    path('userlogin/', views.userLogin,name='userLogin'),
    path('addsitrep/', views.addNewSitrep,name='addNewSitrep'),
    path('showsitrep/', views.showAllSitrep,name='showAllSitrep'),
    path('search/', views.filteredContacts,name='filteredContacts'),
]
