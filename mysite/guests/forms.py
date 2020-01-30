from django import forms
from .models import Guest

class SearchForm(forms.Form):
    FirstName = forms.CharField(label = 'First Name', widget=forms.Textarea(attrs={'rows':1, 'cols':15}))
    LastName = forms.CharField(label = 'Last Name', widget=forms.Textarea(attrs={'rows':1, 'cols':50}))
    Email = forms.EmailField(label = 'Email Address')

class DynamicMultipleChoiceField(forms.MultipleChoiceField): 
    def clean(self, value): 
        return value

class RSVPForForm(forms.Form):
    Invitees = DynamicMultipleChoiceField(label='', widget=forms.CheckboxSelectMultiple, choices=[])
    def __init__(self, InvitationID, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        
        super(RSVPForForm, self).__init__(*args, **kwargs)
        self.fields['Invitees'].choices = [(o.GuestID, o.FirstName + ' ' + o.LastName) for o in Guest.objects.all().filter(InvitationID=InvitationID)]
        
