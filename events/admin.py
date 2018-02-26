# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from events.models import Events,Profile,CampusRepresantative
# Register your models here.

class EventAdmin(admin.ModelAdmin):
	model = Events
	list_display  = ('EventName' ,'EventDescription','eventCost')

class ProfileAdmin(admin.ModelAdmin):
	model = Profile
	list_display = ('Name','PhoneNo','Institute_Uni')

class CampusRepresentativeAdmmin(admin.ModelAdmin):
	model = CampusRepresantative
	list_display = ('Name','Phone','email','Institute')

admin.site.register(Events,EventAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(CampusRepresantative,CampusRepresentativeAdmmin)	