from django import forms
from .models import Guest, Email

class SearchForm(forms.Form):
    FirstName = forms.CharField(label = 'First Name')
    LastName = forms.CharField(label = 'Last Name')
    Email = forms.EmailField(label = 'Email Address')
    
    def clean(self):
        fname = self.cleaned_data.get('FirstName')
        lname = self.cleaned_data.get('LastName')
        
        if Guest.objects.all().filter(FirstName__iexact=fname, LastName__iexact=lname).exists():
            next
        else:
            raise forms.ValidationError('Your invitation could not be found. Please double check all fields and try again.')

class DynamicMultipleChoiceField(forms.MultipleChoiceField): 
    def clean(self, value): 
        if len(value) != 1:
            raise forms.ValidationError('Please RSVP for this person')
        else:
            return value

class RSVPForForm(forms.Form):
    def __init__(self, InvitationID, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        
        super(RSVPForForm, self).__init__(*args, **kwargs)
        for i in Guest.objects.all().filter(InvitationID=InvitationID):
            self.fields['rsvp_' + str(i.GuestID)] = DynamicMultipleChoiceField(label=i.FirstName + ' ' + i.LastName, 
                        choices=[(True, 'Yes'), (False, 'No')], widget=forms.CheckboxSelectMultiple())        
            if i.PlusOne:
                self.fields['plusone'] = DynamicMultipleChoiceField(label='Plus One', 
                        choices=[(True, 'Yes'), (False, 'No')], widget=forms.CheckboxSelectMultiple())   
                self.fields['PlusOneFirstName'] = forms.CharField(label = 'Plus One First Name', required=False)
                self.fields['PlusOneLastName'] = forms.CharField(label = 'Plus One Last Name', required=False) 

    def clean(self):
        try:
            plusone = self.cleaned_data.get('plusone')
        
            if 'True' in plusone:
                msg = forms.ValidationError("This field is required")
                self.add_error('plusonefname', msg)
                self.add_error('plusonelname', msg)
        except:
            pass 
    
class AddEmailForm(forms.Form):
    email = forms.EmailField(label='Email')
    invid = forms.CharField(widget=forms.HiddenInput())
    
    def __init__(self, InvitationID, *args, **kwargs):
        super(AddEmailForm, self).__init__(*args, **kwargs)
        self.fields['invid'].initial = InvitationID
    
    def clean(self):
        emailid = self.cleaned_data.get('email')
        invitationid = self.cleaned_data.get('invid')

            
        if Email.objects.all().filter(Email__iexact=emailid, InvitationID=invitationid).exists():
            self.add_error('email', forms.ValidationError("Email is already registered to the invitation"))
