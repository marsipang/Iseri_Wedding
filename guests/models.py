from django.db import models

# Create your models here.
class Guest(models.Model):
    FirstName = models.TextField()
    LastName = models.TextField()
    Attending = models.BooleanField(blank=True, null=True)
    InvitationID = models.TextField()
    GuestID = models.IntegerField()
    UpdateBy = models.TextField(blank=True, null=True)
    PlusOne = models.BooleanField(blank=True)
    PlusOneFirstName = models.TextField(blank=True, null=True)
    PlusOneLastName = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.FirstName
    def check_rsvp(self):
        return self.Attending
    check_rsvp.admin_order_field = 'Attending'
    check_rsvp.boolean = True
    check_rsvp.short_description = 'Published recently?'

class Email(models.Model):
    InvitationID = models.TextField()
    Email = models.EmailField()


class WeddingParty(models.Model):
    FirstName = models.TextField()
    LastName = models.TextField()
    Relation = models.TextField()
    Title = models.TextField()
    About = models.TextField()