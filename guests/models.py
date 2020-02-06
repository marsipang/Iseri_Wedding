from django.db import models
from django.db.models import Max

def get_new_default():
    if Guest.objects.all().count() == 0:
        new_order_default = 1
    else:
        new_order_default = Guest.objects.all().aggregate(Max('GuestID'))['GuestID__max']+1
    return new_order_default

# Create your models here.
class Guest(models.Model):
    FirstName = models.TextField()
    LastName = models.TextField()
    Attending = models.BooleanField(blank=True, null=True)
    InvitationID = models.TextField()
    GuestID = models.IntegerField(default = get_new_default, unique=True)
    UpdateBy = models.TextField(blank=True, null=True)
    PlusOne = models.BooleanField(blank=True)
    PlusOneAttending = models.BooleanField(blank=True, null=True)
    PlusOneFirstName = models.TextField(blank=True, null=True)
    PlusOneLastName = models.TextField(blank=True, null=True)
    

class Email(models.Model):
    InvitationID = models.TextField()
    Email = models.EmailField()


class WeddingParty(models.Model):
    FirstName = models.TextField(max_length=50)
    LastName = models.TextField(max_length=50)
    Relation = models.TextField(choices=[('Bride', 'Bride'), ('Groom', 'Groom')])
    Title = models.TextField(max_length=50)
    About = models.TextField()