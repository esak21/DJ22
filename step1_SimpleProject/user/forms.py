from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import TicketingUser


class TicketingUserForm(UserCreationForm):
    class Meta:
        model = TicketingUser
        fields = ['email','name', 'lastname', 'mobileno', 'description', 'is_superuser', 'userimage']
        