from django import forms
from .models import Guest

class SearchForm(forms.Form):
    FirstName = forms.CharField(label = 'First Name')
    LastName = forms.CharField(label = 'Last Name')
    Email = forms.EmailField(label = 'Email Address')

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
                self.fields['plusonefname'] = forms.CharField(label = 'Plus One First Name', required=False)
                self.fields['plusonelname'] = forms.CharField(label = 'Plus One Last Name', required=False)

                def get_fields(self, request, obj=None):
                    if obj is None:
                        next
                    else:
                        self.fields.append('status')   

    
    def clean(self):
        plusone = self.cleaned_data.get('plusone')
    
        if 'True' in plusone:
            msg = forms.ValidationError("This field is required")
            self.add_error('plusonefname', msg)
            self.add_error('plusonelname', msg)



        
class RSVPForm(forms.Form):
    rsvp = forms.ChoiceField(label='', choices=[(True, 'Yes'), (False, 'No')])
    plusone = forms.BooleanField(label = 'Plus One Attending')
    plusonefname = forms.CharField(label = 'Plus One First Name')
    plusonelname = forms.CharField(label = 'Plus One Last Name')
    email = forms.EmailField(label = 'Email')    