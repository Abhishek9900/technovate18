"""Technovate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from events import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index,name='index'),
    url(r'^2018/', views.index2018,name='index2018'),
    url(r'^join/',views.join,name='join'),
    url(r'^register$',views.register,name='register'),
    #url(r'^dashboard/update_profile/', views.UpdateAndCreateProfile, name='UpdateProfile'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^login$', views.LOG_IN, name='login'),
    url(r'^logout/', views.LOG_OUT, name='logout'),
    url(r'^events/', views.tevents, name='events'),
    url(r'^about$',views.about,name='about'),
    url(r'^verify$',views.verify,name='verify'),
    url(r'^send$',views.s,name='sendchitti'),
    url(r'pay/', views.pay, name = 'pay'),
    url(r'Success/', views.success, name='success'),
    url(r'Failure/', views.failure, name='failure'),
    url(r'^representative$',views.campusRe,name='representative'),
    url(r'^enroll$',views.enrollTo,name="enroll"),
    url(r'hospitality/', views.update_hosp, name='hosp'),
    url(r'team/', views.update_team, name='team'),
    url(r'send_details/', views.send_details, name='send_details'),
]