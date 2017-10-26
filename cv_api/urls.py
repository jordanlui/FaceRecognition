"""cv_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

# Django 1.11 version imports
from django.contrib.auth.views import login
from face_detector.views import *
# New Django changes format from:
# url(r'^contact/$', 'myapp.views.contact'),
# TO:
# url(r'^contact/$', contact, name='contact'),


urlpatterns = [
	url(r'^face_detection/detect/$', detect, name='detect'),
	# url(r'^admin/', admin, name='admin')
	url(r'^admin/', admin.site.urls)
]


# urlpatterns = [
#     url(r'^face_detection/detect/$', 'face_detector.views.detect'),
#     # url(r'^$', 'cv_api.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', admin.site.urls),
# ]

# urlpatterns = patterns('',
#     # Examples:
 
#     url(r'^face_detection/detect/$', 'face_detector.views.detect'),
 
#     # url(r'^$', 'cv_api.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
 
#     url(r'^admin/', include(admin.site.urls)),
# )
