from django.contrib import admin
from .models import Guest, WeddingParty, Email

# Register your models here.
admin.site.register(Guest)
admin.site.register(WeddingParty)
admin.site.register(Email)

class GuestAdmin(admin.ModelAdmin):
    # ...
    list_display = ('FirstName', 'LastName')
    
class WeddingPartyAdmin(admin.ModelAdmin):
    # ...
    list_display = ('FirstName', 'LastName')

class EmailAdmin(admin.ModelAdmin):
    list_display = ('InvitationID', 'Email')