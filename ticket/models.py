from django.db import models

# Create your models here.
class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.ticket_id + ' ' +  self.updated_at