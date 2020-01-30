from django.urls import path

from . import views

app_name = 'guests'
urlpatterns = [
    path('', views.test, name='test'),
    path('rsvp', views.FindRSVP, name='rsvp'),
    path('rsvp/Select/<SearchResult>', views.ChooseRSVP, name='choosersvp'),
    path('rsvp/Submit/<ChooseResult>', views.SubmitRSVP, name='submitrsvp'),
    path('ajax/validate_guest/', views.validate_guest, name='validate_guest'),
]