from django.contrib import admin
from .models import Guest

# Register your models here.
admin.site.register(Guest)

class GuestAdmin(admin.ModelAdmin):
    # ...
    list_display = ('FirstName', 'LastName')