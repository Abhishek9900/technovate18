from django.db import models
from django.utils import timezone
import datetime
import os
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
choice2 = (
    ('Appiness', 'Appiness'),
    ('Backyard Data Science', 'Backyard Data Science'),
    ('Game of Codes', 'Game of Codes'),
    ('Wolf of Web street', 'Wolf of Web street'),
    ('Robo Dangal', 'Robo Dangal'),
    ('Dizhard', 'Dizhard'),
    ('Flying SynDRONE', 'Flying SynDRONE'),
    ('Robo Soccer', 'Robo Soccer'),
    ('Enkindle', 'Enkindle'),
    ('Questa', 'Questa'),
    ('Gamers Crusade/LAN Gaming', 'Gamers Crusade/LAN Gaming'),
    ('Treasure Hunt', 'Treasure Hunt'),
    ('Nukkad Natak', 'Nukkad Natak'),
    ('Dance Fever', 'Dance Fever'),
    ('Capriccio/Singing', 'Capriccio/Singing'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, related_name='profil')
    gtotal = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    
    def __str__(self):
        return self.user.username + ' - ' + str(self.gtotal) + ' - ' + str(self.status)
    
class Member(models.Model):
    profile = models.ForeignKey(Profile, blank=True, null=True, related_name='members')
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200)
    mobile = PhoneNumberField()
    institute = models.CharField(max_length=500)
    event = models.CharField(max_length=1000)
    accomodation = models.BooleanField(default=False)
    total = models.IntegerField(default=250)
    
    def __str__(self):
        return self.name + ' - ' + self.mobile + ' - ' + self.institute