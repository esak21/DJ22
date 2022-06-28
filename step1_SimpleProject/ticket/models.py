from datetime import datetime

from django.db import models
from random import randint
# Create your models here.

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

def get_ticketId_generator():
    ticket_id = f"COG{randint(1111,9999)}"
    print(ticket_id)
    return ticket_id

ASSIGNED_TO = (
    ('QHF390', 'esakki'),
    ('MZR006', 'steve'),
)

PRIORITY = (
    (1, 'VeryHigh'),
    (2, 'HIGH'),
    (3, 'LOW'),
)


class TicketModel(models.Model):
    
    ticketId = models.CharField(max_length=25, blank=False, null=False, default=get_ticketId_generator())
    title =  models.CharField(max_length=25, blank=False, null=False)
    assigned_to = models.CharField(max_length=25, blank=False, null=False, choices=ASSIGNED_TO)
    description = models.CharField(max_length=255, blank=False, null=False)
    attachment = models.FileField(upload_to='bugs/TicketModel/', verbose_name="adding bug screenshot")
    priority = models.IntegerField( choices=PRIORITY)
    raised_by = models.CharField(max_length=25, blank=False, null=False)
    assigned_email = models.CharField(max_length=25, blank=False, null=False)
    created_at = models.DateTimeField(default=datetime.now)


    def __str__(self) -> str:
        return self.ticketId



