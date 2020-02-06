from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from .forms import SearchForm, RSVPForForm, AddEmailForm
from .models import Guest, WeddingParty, Email
from django.urls import reverse
from django.core.mail import send_mail
from django_pandas.managers import read_frame

# Create your views here.
def home(request):
    return render(request, 'guests/home.html')

def details(request):
    return render(request, 'guests/details.html')

def FindRSVP(request): 
    title = 'Find Your Invitation'
    result = "No Post"
    form = SearchForm()
    InvStatus = None
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                GuestObj = Guest.objects.get(LastName__iexact=cd['LastName'], 
                                           FirstName__iexact=cd['FirstName'])
                result = GuestObj.InvitationID + '!' + str(GuestObj.GuestID)
                InvStatus = GuestObj.Attending
            except:
                pass
            if InvStatus == None:
                if result != "No Post":
                    emailrecord = Email(InvitationID=GuestObj.InvitationID, Email=cd['Email'])
                    emailrecord.save()
                    return HttpResponseRedirect(reverse('guests:choosersvp', args=(result,)))
                else:
                    next
            else:
                return HttpResponseRedirect(reverse('guests:guestrsvp', args=(result,)))
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
            recepients = [i.Email for i in Email.objects.filter(InvitationID=invid)]
            guestobj = Guest.objects.get(GuestID=guestid)
            guestname = f'{guestobj.FirstName} {guestobj.LastName}'
            send_mail(
                'RSVP submitted',
                f'''An RSVP to our wedding has been submitted by {guestname}. Thank you! You can review and/or update your rsvp on our website at anytime in the RSVP section.\n\nThe Iseris''',
                'marsipang@gmail.com',
#                [recepients],
                ['pangie490@gmail.com', 'Iseriwedding@gmail.com'],
                fail_silently=False
            )
            return HttpResponseRedirect(reverse('guests:submitrsvp', args=(SearchResult,)))
        else:
            next
    else:
        next
    return render(request, 'guests/rsvp.html', {'form': form, 'title': title})

def SubmitRSVP(request, ChooseResult):    
    title = 'Thank You! Your RSVP has successfully been submitted'
    invid = ChooseResult.split('!')[0]
    guests = [{'Name':f'{i.FirstName} {i.LastName}', 'Attending':'Yes' if i.Attending else 'No'} for i in Guest.objects.all().filter(InvitationID=invid)]
    if Guest.objects.filter(InvitationID=invid, PlusOne=True).exists():
        plusone = [{'Name':f'+1: {i.PlusOneFirstName} {i.PlusOneLastName}' if i.PlusOneAttending else f'+1: {i.FirstName} {i.LastName} Plus One', 'Attending': 'Yes' if i.PlusOneAttending else 'No'} for i in Guest.objects.all().filter(InvitationID=invid, PlusOne=True)]
        guests = guests + plusone
    emails = [{'Email':i.Email} for i in Email.objects.all().filter(InvitationID=invid)]
    if request.method == 'POST' and 'Update' in request.POST:
        return HttpResponseRedirect(reverse('guests:choosersvp', args=(ChooseResult,)))
    elif request.method == 'POST' and 'AddEmail' in request.POST:
        return HttpResponseRedirect(reverse('guests:addemail', args=(ChooseResult,)))
    else:
        next    
    return render(request, 'guests/rsvpdetails.html', {'title':title, 'guests': guests, 'emails':emails})


def GuestRSVP(request, InvID):
    title = 'An RSVP FOR THIS INVITATION HAS ALREADY BEEN SUBMITTED'
    invid = InvID.split('!')[0]
    guests = [{'Name':f'{i.FirstName} {i.LastName}', 'Attending':'Yes' if i.Attending else 'No'} for i in Guest.objects.all().filter(InvitationID=invid)]
    if Guest.objects.filter(InvitationID=invid, PlusOne=True).exists():
        plusone = [{'Name':f'+1: {i.PlusOneFirstName} {i.PlusOneLastName}' if i.PlusOneAttending else f'+1: {i.FirstName} {i.LastName} Plus One', 'Attending': 'Yes' if i.PlusOneAttending else 'No'} for i in Guest.objects.all().filter(InvitationID=invid, PlusOne=True)]
        guests = guests + plusone
    emails = [{'Email':i.Email} for i in Email.objects.all().filter(InvitationID=invid)]
    if request.method == 'POST' and 'Update' in request.POST:
        return HttpResponseRedirect(reverse('guests:choosersvp', args=(InvID,)))
    elif request.method == 'POST' and 'AddEmail' in request.POST:
        return HttpResponseRedirect(reverse('guests:addemail', args=(InvID,)))
    else:
        next
    return render(request, 'guests/rsvpdetails.html', {'title':title, 'guests': guests, 'emails':emails})

def AddEmail(request, InvID):
    title = 'Add an Email'
    invid = InvID.split('!')[0]
    guestid = InvID.split('!')[1]
    form = AddEmailForm(invid)
    if request.method == 'POST':
        form = AddEmailForm(invid, request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            emailrecord = Email(InvitationID=invid, Email=cd['email'])
            emailrecord.save()
            guestobj = Guest.objects.get(GuestID=guestid)
            guestname = f'{guestobj.FirstName} {guestobj.LastName}'
            send_mail(
                'Email Added to Invitation',
                f'''The email {cd['email']} was successfully added by {guestname} to receive emails about the Iseri Wedding. If there are any updates made to the rsvp for your invitation or any notices about the wedding, this email will receive an email about it. If you'd like to review and/or update your RSVP submission, you can do so at anytime on our website in the RSVP section.\n\nThank you!\nThe Iseris''',
                'marsipang@gmail.com',
#                [cd['email']],
                ['pangie490@gmail.com', 'Iseriwedding@gmail.com'],
                fail_silently=False,
            )
            return HttpResponseRedirect(reverse('guests:submitrsvp', args=(InvID,)))
        else:
            next
    return render(request, 'guests/rsvp.html', {'form': form, 'title': title})

def registry(request):
    return render(request, 'guests/registry.html')

def travel(request):
    return render(request, 'guests/travel.html')

def weddingparty(request):
    Bride = [{'FirstName':i.FirstName, 'LastName':i.LastName, 'Title':i.Title, 'About':i.About} for i in WeddingParty.objects.all().filter(Relation='Bride')]
    Groom = [{'FirstName':i.FirstName, 'LastName':i.LastName, 'Title':i.Title, 'About':i.About} for i in WeddingParty.objects.all().filter(Relation='Groom')]
    Everybody = Bride + Groom
    return render(request, 'guests/weddingparty.html', {'Bride':Bride, 'Groom':Groom, 'Everybody':Everybody})