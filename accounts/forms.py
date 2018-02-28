from django import forms
from .models import Profile, Member, choice2


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('gtotal',)
        
    def save(self, user, commit=True):
        profile = super(ProfileForm, self).save(commit=False)
        profile.user = user
        profile.save()
        return profile


class MemberForm(forms.ModelForm):
    event = forms.MultipleChoiceField(choices=choice2)
    
    def __init__(self, *args, **kwargs):
        assigned_users = kwargs.pop('assigned_to', [])
        super(MemberForm, self).__init__(*args, **kwargs)
        self.fields['total'].widget.attrs['readonly'] = True
        self.fields['event'].widget.attrs['multiple'] = True
        self.fields['accomodation'].label = "Click here to get accomodation"
   
    class Meta:
        model = Member
        fields = ('name', 'email', 'mobile', 'institute', 'event', 'accomodation', 'total')
        
    def save(self, profile, commit=True):
        member = super(MemberForm, self).save(commit=False)
        member.profile = profile
        member.save()
        return member