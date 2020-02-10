from django.db import models
from django.db.models import Max

# Create your models here.
class Guest(models.Model):
    GuestID = models.IntegerField(primary_key=True, unique=True)
    FirstName = models.TextField()
    LastName = models.TextField()
    Attending = models.BooleanField(blank=True, null=True)
    InvitationID = models.TextField()
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