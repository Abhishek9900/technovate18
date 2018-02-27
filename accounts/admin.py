from django.contrib import admin
from .models import Profile, Member

class ProfileAdmin(admin.ModelAdmin):
	model = Profile
	list_display = ('user','gtotal','status')

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Member)