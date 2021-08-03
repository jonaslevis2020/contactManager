from contact.models import Contact
from django.contrib import admin
from django.contrib.auth.models import Group, User
from import_export.admin import ImportExportModelAdmin


# a class to customize the Contact model
class ContactAdmin(ImportExportModelAdmin):
    list_display = ('id', 'manager', 'name', 'email', 'phone', 'gender', 'info','date_added')
    list_editable = ('email', 'phone', 'gender', 'info',)
    list_display_links = ('name', 'id',)
    # list_max_show_all = 5
    list_per_page = 5
    search_fields = ('name', 'email', 'phone', 'gender', 'info',)
    list_filter = ('gender', 'info','date_added',)

# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)

