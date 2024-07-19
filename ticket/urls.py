from .views import *
from django.urls import re_path as url
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
        url(r'^v1/createticket/$', csrf_exempt(CreateTicket.as_view()), name = 'create_ticket'),
        url(r'^v1/deleteticket/$', csrf_exempt(DeleteTicket.as_view()), name = 'delete_ticket'),
        url(r'^v1/buyticket/$', csrf_exempt(BookTicket.as_view()), name = 'buy_ticket'),
    ]