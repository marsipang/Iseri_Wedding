from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import SearchForm, RSVPForForm
from .models import Guest
from django.db.models.functions import Concat, Lower
from django.db.models import Count, F, Value
import json

# Create your views here.
def test(request):
    return render(request, 'guests/test.html')

def rsvp(request):    
    submitted = False
    result = "No Post"
    form = SearchForm()
    rsvpforform = RSVPForForm(result)
    if request.method == 'POST':
        if 'search' in request.POST:
            form = SearchForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                try:
                    result = Guest.objects.get(LastName__iexact=cd['LastName'], 
                                               Address__iexact=cd['Address']).InvitationID
                except:
                    pass
                if result != "No Post":
                    return HttpResponseRedirect(f'/guests/rsvp?submitted=True;found={result}')
                else:
                    pass
        elif 'RSVPfor' in request.POST:
            next
                    
    else:
        if 'submitted' in request.GET:
            submitted = True
        if ('found' in request.GET):
            result = request.GET['found']
            rsvpforform = RSVPForForm(result)
    
    return render(request, 'guests/rsvp.html', 
                  {'form': form, 'submitted': submitted, 'result': result, 'rsvpforform':rsvpforform})

def validate_guest(request):
    lname = request.GET.get('lname', None)
    addr = request.GET.get('addr', None)
    data = {
        'found': Guest.objects.filter(LastName__iexact=lname, Address__iexact=addr).exists()
    }
    return JsonResponse(data)

def registry(request):
    return render(request, 'guests/test.html')