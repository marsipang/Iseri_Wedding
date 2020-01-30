from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import SearchForm, RSVPForForm
from .models import Guest
from django.db.models.functions import Concat, Lower
from django.db.models import Count, F, Value
from django.urls import reverse
import re

# Create your views here.
def test(request):
    return render(request, 'guests/test.html')

def FindRSVP(request): 
    title = 'Find Your Invitation'
    result = "No Post"
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                GuestObj = Guest.objects.get(LastName__iexact=cd['LastName'], 
                                           FirstName__iexact=cd['FirstName'])
                result = GuestObj.InvitationID + '!' + str(GuestObj.GuestID)
                GuestObj.Email = cd['Email']
                GuestObj.save()
            except:
                pass
            if result != "No Post":
                return HttpResponseRedirect(reverse('guests:choosersvp', args=(result,)))
            else:
                next
    else:
        next
    return render(request, 'guests/rsvp.html', {'form': form, 'title': title})

def validate_guest(request):
    fname = request.GET.get('fname', None).strip()
    lname = request.GET.get('lname', None).strip()
    data = {
        'found': Guest.objects.filter(LastName__iexact=lname, FirstName__iexact=fname).exists()
    }
    return JsonResponse(data)

def ChooseRSVP(request, SearchResult):
    title = 'Choose Who To RSVP For'
    invid = SearchResult.split('!')[0]
    guestid = SearchResult.split('!')[1]
    form = RSVPForForm(invid)
    if request.method == 'POST':
        form = RSVPForForm(SearchResult, request.POST)
        if form.is_valid():
            cd = form.cleaned_data
#            title = cd['Invitees']
#            Guest.objects.filter(GuestID__in=id_list).update(myattribute=True)
            return HttpResponseRedirect(reverse('guests:test'))
            
    return render(request, 'guests/rsvp.html', {'form': form, 'title': title})



def registry(request):
    return render(request, 'guests/test.html')