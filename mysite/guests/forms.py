from django import forms
from .models import Guest

class SearchForm(forms.Form):
    FirstName = forms.CharField(label = 'First Name', widget=forms.Textarea(attrs={'rows':1, 'cols':15}))
    LastName = forms.CharField(label = 'Last Name', widget=forms.Textarea(attrs={'rows':1, 'cols':50}))
    Email = forms.EmailField(label = 'Email Address')

class RSVPForForm(forms.Form):
    Attending = forms.MultipleChoiceField(label = 'attend', widget=forms.CheckboxSelectMultiple, choices = [])
    Email = forms.EmailField(label = 'Email Address')


    def __init__(self, InvitationID, *args, **kwargs):
        super(RSVPForm, self).__init__(*args, **kwargs)
        self.fields['Attending'] = forms.MultipleChoiceField(label = 'attend', widget=forms.CheckboxSelectMultiple,
            choices=[(o.FirstName + ' ' + o.LastName, o.FirstName + ' ' + o.LastName) for o in Guest.objects.all().filter(InvitationID=InvitationID)]
        )
        
        
    