from django.contrib import admin
from phonebook.models import Contact, UserProfileInfo

# Register your models here.
admin.site.register (Contact)
admin.site.register (UserProfileInfo)