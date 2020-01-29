from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from .models import Guest

# Create your views here.
def test(request):
    return render(request, 'guests/test.html')

def rsvp(request):    
    submitted = False
    result = "No Post"
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            query = cd['LastName']
            try:
                result = Guest.objects.get(LastName=query).FirstName
            except:
                result = 'Sorry! No match found'
            # assert False
            if result == "No Post":
                return HttpResponseRedirect('/guests/rsvp?submitted=True;found=False')
            else:
#                return HttpResponseRedirect('/guests/rsvp?submitted=True;found=True')
                return HttpResponseRedirect(f'/guests/rsvp?submitted=True;found={result}')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
#        if ('found' in request.GET) & (request.GET['found'] == 'True'):
#            result = 'Hooray!'
        if ('found' in request.GET):
            result = request.GET['found']
    
    return render(request, 'guests/rsvp.html', {'form': form, 'submitted': submitted, 'result': result})

def registry(request):
    return render(request, 'guests/test.html')