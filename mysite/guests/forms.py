from django import forms

class ContactForm(forms.Form):
  LastName = forms.CharField(label = 'Last Name', widget=forms.Textarea(attrs={'rows':1, 'cols':50}))
  Address = forms.CharField(label = 'Address', widget=forms.Textarea(attrs={'rows':2, 'cols':15}))