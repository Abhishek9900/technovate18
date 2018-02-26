# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,HttpResponseRedirect,render_to_response,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
from django.contrib.auth import login,logout,authenticate
from events.models import Events,Profile,CampusRepresantative
from django.contrib.auth.decorators import login_required
from json import dump
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.template import Context, Template,RequestContext

import hashlib
from datetime import datetime as dt
def index(request):
    user = request.user
    if user.is_authenticated:
        return render(request,'index.html')
    return render(request,'index.html')
    #return HttpResponseRedirect('/2018')

def index2018(request):
    return render(request, 'index2018.html')



def about(request):
    return render(request,'about.html')

def sponsor(request):
    return render(request,'sponsors.html')


def join(request):
    return render(request,'join.html')



@login_required(login_url='/')
def dashboard(request):
    return HttpResponseRedirect('/')


def tevents(request):
    return render(request,'tevents.html')



def LOG_OUT(request):
    logout(request)
    return redirect('/')


def update_hosp(request):
    
    user = request.user
    user.profile.is_hosp = True 
    user.profile.payment_to_be_paid += user.profile.number_of_team_members * 500 + 500
    user.profile.save()
    return HttpResponse('')
    


def campusRe(request):
    if request.method == 'POST':
        C = CampusRepresantative()
        C.Name = request.POST['Name']
        C.Institute = request.POST['ins']
        email = request.POST['email']
        phone = request.POST['ph']
        try:
            cam = CampusRepresantative.objects.get(email=email)
        except ObjectDoesNotExist:
            C.email = request.POST['email']
            C.Phone  = request.POST['ph']
            C.save()
            #html = render_to_string('email/email_campurRepre.html',{'name':C.Name,'institute':C.Institute})
            #send_mail('Campus Respresentative',
            #' ',
            #'technovate@iiitnr.ac.in',
            #[C.email],
            #html_message = html
            #)
            return HttpResponseRedirect('/')
        else:

            html = render_to_string('email/email_campurRepre.html',{'name':C.Name,'institute':C.Institute,'caution':"caution"})

            send_mail('You have already registered',
            ' ',
            'technovate.iiitnr@gmail.com',
            [C.email],
            html_message = html
            )
            return HttpResponseRedirect('/')
