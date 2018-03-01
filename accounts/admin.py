from django.contrib import admin
from .models import Profile, Member
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'gtotal', 'status')


class MemberResource(resources.ModelResource):
    class Meta:
        model = Member
        fields = ('id', 'profile', 'name', 'email', 'institute', 'accomodation')
    
    
class ProfileAdmin(ImportExportModelAdmin):
    resource_class = ProfileResource
    list_display = ('user', 'gtotal', 'status')
    list_filter = ('user', 'status')
    search_fields = ['user']
    
class MemberAdmin(ImportExportModelAdmin):
    resource_class = MemberResource
    list_display = ('profile', 'name', 'email', 'institute', 'accomodation')
    list_filter = ('profile__user', 'name', 'email', 'institute', 'accomodation')
    search_fields = ['event', 'institute']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Member, MemberAdmin)