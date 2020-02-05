from django.urls import path

from . import views

app_name = 'guests'
urlpatterns = [
    path('', views.home, name='home'),
    path('details', views.details, name='details'),
    path('rsvp', views.FindRSVP, name='rsvp'),
    path('rsvp/Select/<SearchResult>', views.ChooseRSVP, name='choosersvp'),
    path('rsvp/Submit/<ChooseResult>', views.SubmitRSVP, name='submitrsvp'),
    path('rsvp/Reply/<InvID>', views.GuestRSVP, name='guestrsvp'),
    path('rsvp/AddEmail/<InvID>', views.AddEmail, name='addemail'), 
    path('ajax/validate_guest/', views.validate_guest, name='validate_guest'),
    path('registry', views.registry, name='registry'),
    path('travel', views.travel, name='travel'),
    path('weddingparty', views.weddingparty, name='weddingparty')
]