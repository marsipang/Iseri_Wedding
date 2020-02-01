from django.contrib import admin
from .models import Guest, WeddingParty

# Register your models here.
admin.site.register(Guest)
admin.site.register(WeddingParty)

class GuestAdmin(admin.ModelAdmin):
    # ...
    list_display = ('FirstName', 'LastName')
    
class WeddingPartyAdmin(admin.ModelAdmin):
    # ...
    list_display = ('FirstName', 'LastName')