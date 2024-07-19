from django.db import models
from django_google_maps import fields as map_fields
from ticket.models import Ticket
from user.models import User

# Create your models here.
# model to have enent with like event id, event name, date, location(using google django map), available tickes 

class Event(models.Model):
    ''''''
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=155)
    location = map_fields.GeoLocationField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    available_tickets = models.ForeignKey(Ticket, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.event_id + ' ' +  self.name + ' ' + self.location