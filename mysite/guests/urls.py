from django.urls import path

from . import views

app_name = 'guests'
urlpatterns = [
    path('', views.test, name='test'),
    path('rsvp', views.rsvp, name='rsvp')
]