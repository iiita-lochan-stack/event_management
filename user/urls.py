from .views import *
from django.urls import re_path as url
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
        url(r'^v1/createuser/$', csrf_exempt(CreateUser.as_view()), name = 'create_user'),
        url(r'^v1/deleteuser/$', csrf_exempt(DeleteUser.as_view()), name = 'delete_user'),
    ]