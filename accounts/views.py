from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from .forms import MemberForm, ProfileForm
from .models import Member, Profile


def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    if hasattr(request.user, 'profil'):
                        return HttpResponseRedirect(
                            reverse('interface')
                        )
                    else:
                        return HttpResponseRedirect(
                                    reverse('interface')
                                    )
                    # return HttpResponseRedirect(reverse('index'))
                else:
                    messages.danger(
                        request,
                        "That user account has been disabled."
                    )
            else:
                messages.danger(
                    request,
                    "Username or password is incorrect."
                )
    return render(request, 'sign_in.html', {'form': form})


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )
            return HttpResponseRedirect(reverse('interface'))  # TODO: go to profile
    return render(request, 'sign_up.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse('index'))


@login_required
def interface(request):
    try:
        profile = request.user.profil
    except:
        profile = ProfileForm()
        profile.save(request.user)
    try:
        members = Member.objects.filter(profile=profile.id)
    except:
        members = None
    total = 0
    if members:
        for m in members:
            total+=m.total
    profile.gtotal = total
    try:
        profile.save()
    except:
        profile.save(request.user or None)
    form = MemberForm()
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            try:
                member = form.save(profile)
                messages.success(request, 'Member created successfully')
                return HttpResponseRedirect(reverse('interface'))
            except Exception as e:
                messages.error(request, 'Error creating member: {}'.format(e))
                return HttpResponseRedirect(reverse('ineterface'))
    print(form)
    return render(request, 'interface.html',{'form':form, 'members':members, 'profile':profile})
