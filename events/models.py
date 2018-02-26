from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Table for events in Technovate
class Events(models.Model):
    EventName = models.CharField(max_length=50)
    EventDescription = models.CharField(max_length=1000)
    eventCost = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    Event_Cat = models.IntegerField(default=0)
    #image = models.ImageField(upload_to='static/events',blank=True)

    #get_event_name function for retrieving event name
    def get_event_name(self):
        return self.EventName

    # get_event_description function for retrieving event description
    def get_event_description(self):
        return self.EventDescription

    def __str__(self):
        return self.EventName

#Table for participants registering for event in Technovate
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100,blank=True)
    events = models.ManyToManyField(Events,blank=True)
    PhoneNo = models.CharField(max_length=10)
    Institute_Uni = models.CharField(max_length=100)
    payment_to_be_paid = models.IntegerField(default=250)
    payment_paid = models.IntegerField(default=0)
    is_active = models.BooleanField(null=False,default=False)
    secret_code = models.CharField(max_length=5,default=0)
    is_paid = models.BooleanField(default=False)
    number_of_team_members = models.IntegerField(default=0)
    is_hosp = models.BooleanField(default=False)
    payment_mode = models.CharField(default='Online', max_length=10)

    #get_participated_in function for retrieving list of participated events by profile
    def get_participated_in(self):
         pass

    #A method for retrieving  phone number
    def get_phone_no(self):
        return self.PhoneNo

    # A method of getting institute name
    def get_Institute_Uni(self):
        return self.Institute_Uni

    def __str__(self):
        return self.user.get_full_name() + ' ' + self.Institute_Uni

    def payment_due(self):
        return self.payment_to_be_paid

    def payment_pay(self):
        return self.payment_paid

    def get_no_of_team_membmers(self):
        return str(self.number_of_team_members)

    # in progress
    class Admin:
        list_display = ('user.get_full_name','user.email')


class CampusRepresantative(models.Model):
    Name = models.CharField(max_length=100)
    Institute = models.CharField(max_length=100)
    Phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.Name + ' ' + self.Institute