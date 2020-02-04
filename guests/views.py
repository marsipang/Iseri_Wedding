from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import SearchForm, RSVPForForm, RSVPForm
from .models import Guest, WeddingParty, Email
from django.db.models.functions import Concat, Lower
from django.db.models import Count, F, Value
from django.urls import reverse
import re

# Create your views here.
def home(request):
    return render(request, 'guests/home.html')

def details(request):
    return render(request, 'guests/details.html')

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
                emailrecord = Email(InvitationID=GuestObj.InvitationID, Email=cd['Email'])
                emailrecord.save()
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
    title = 'Let us know Who is Attending'
    invid = SearchResult.split('!')[0]
    guestid = SearchResult.split('!')[1]
    form = RSVPForForm(invid)
    if request.method == 'POST':
        form = RSVPForForm(invid, request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cdfields = cd.keys()
            Result = []
            for field in cdfields:
                if field == 'plusone':
                    Guest.objects.filter(GuestID__in=guestid).update(PlusOneAttending=''.join(cd[field]))
                elif field in ['PlusOneFirstName', 'PlusOneLastName']:
                    if cd['plusone'] == True:
                        Guest.objects.filter(GuestID__in=guestid).update(field=cd[field])
                    else:
                        next
                else:
                    gid = field.replace('rsvp_', '')
                    Guest.objects.filter(GuestID__in=gid).update(Attending=''.join(cd[field]))
            return HttpResponseRedirect(reverse('guests:submitrsvp', args=(invid,)))
        else:
            next
    else:
        next
    return render(request, 'guests/rsvp.html', {'form': form, 'title': title})

def SubmitRSVP(request, ChooseResult):    
    return render(request, 'guests/rsvpthankyou.html')


def registry(request):
    return render(request, 'guests/registry.html')

def travel(request):
    return render(request, 'guests/travel.html')

def weddingparty(request):
    Bride = [{'FirstName':i.FirstName, 'LastName':i.LastName, 'Title':i.Title, 'About':i.About} for i in WeddingParty.objects.all().filter(Relation='Bride')]
    Groom = [{'FirstName':i.FirstName, 'LastName':i.LastName, 'Title':i.Title, 'About':i.About} for i in WeddingParty.objects.all().filter(Relation='Groom')]
    Everybody = Bride + Groom
    return render(request, 'guests/weddingparty.html', {'Bride':Bride, 'Groom':Groom, 'Everybody':Everybody})