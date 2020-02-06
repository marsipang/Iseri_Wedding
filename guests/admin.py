from django.contrib import admin
from .models import Guest, WeddingParty, Email
from django.forms import Textarea
from django.db import models

class GuestAdmin(admin.ModelAdmin):
    fields = ['FirstName', 'LastName', 'InvitationID', 'PlusOne']
    list_display = ('FirstName', 'LastName', 'InvitationID', 'Attending', 'PlusOne', 'PlusOneAttending')
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':100})},
    }
    list_filter = ['Attending', 'PlusOne', 'InvitationID']
    search_fields = ['FirstName', 'LastName']
    
class WeddingPartyAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName')
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['FirstName', 'LastName', 'Title']:
            kwargs['widget'] = Textarea(attrs={'rows':1, 'cols':50})
        return super(WeddingPartyAdmin, self).formfield_for_dbfield(db_field,**kwargs)
    list_filter = ['Relation']

class EmailAdmin(admin.ModelAdmin):
    list_display = ('InvitationID', 'Email')
    
# Register your models here.
admin.site.register(Guest, GuestAdmin)
admin.site.register(WeddingParty, WeddingPartyAdmin)
admin.site.register(Email, EmailAdmin)