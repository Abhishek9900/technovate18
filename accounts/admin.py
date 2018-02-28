from django.contrib import admin
from .models import Profile, Member


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('user', 'gtotal', 'status')
    list_filter = ('user', 'status')


class MemberAdmin(admin.ModelAdmin):
    model = Member
    list_display = ('profile', 'name', 'email', 'institute', 'accomodation')
    list_filter = ('profile__user', 'name', 'email', 'institute', 'accomodation')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Member, MemberAdmin)