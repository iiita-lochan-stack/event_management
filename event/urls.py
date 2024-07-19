from .views import *
from django.urls import re_path as url
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
        url(r'^v1/addevent/$', csrf_exempt(AddEvent.as_view()), name = 'add_event'),
        url(r'^v1/getallevent/$', csrf_exempt(GetAllEvent.as_view()), name = 'get_all_event'),
        url(r'^v1/getevent/$', csrf_exempt(GetEvent.as_view()), name = 'get_event'),
    ]