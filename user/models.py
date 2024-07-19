from django.db import models
from ticket.models import *
# Create your models here.
class User(models.Model):
    ''''''
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)    
    mobile_number = models.CharField(max_length=255, db_index=True, editable = True, null=True, blank=True)
    ip_address = models.GenericIPAddressField(protocol="both", unpack_ipv4=False, null=True, blank=True)
    email_id = models.EmailField(max_length=255, db_index=True, null=True, blank=True, editable = True)
    has_role = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    tickets = models.ManyToManyField(Ticket, null=True, blank=True)
    is_email_verified = models.BooleanField(default=True)
    is_phone_verified = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.first_name + ' ' +  self.email_id + ' ' + self.mobile_number