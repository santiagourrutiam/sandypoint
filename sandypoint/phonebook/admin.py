from django.contrib import admin
from phonebook.models import Contact, UserProfileInfo, Sitrep

# Register your models here.

class ContactsAdmin (admin.ModelAdmin):
    fields = ['firstname','lastname','company','contact_type']
    search_fields = ['firstname','lastname','company', 'contact_type']
    list_filter = ['contact_type']


admin.site.register (Contact, ContactsAdmin)
admin.site.register (UserProfileInfo)
admin.site.register (Sitrep)