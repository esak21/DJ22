from dataclasses import fields
from django import forms
from django.contrib import admin
from .models import TicketModel
from .forms import TicketAdminForm

    
# Customizae the Admin Display Panel 
class TicketAdminConfig(admin.ModelAdmin):
    list_display = ('ticketId', 'title', 'assigned_to','assigned_email', 'priority', 'created_at')
    ordering = ('created_at','priority')
    list_filter = ('priority',)
    search_fields = ('ticketId', 'assigned_to', 'raised_by')

    form = TicketAdminForm

    fieldsets = (
        ('TicketInformation', {'fields': ('ticketId', 'title', 'description')}),
        ('TesterInformation', {'fields': ( 'assigned_to', 'assigned_email', 'raised_by')}),
        ('OtherInformation', {'fields': ( 'created_at','attachment')}),
    )


# Register your models here.
admin.site.register(TicketModel, TicketAdminConfig)