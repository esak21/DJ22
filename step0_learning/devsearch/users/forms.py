from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Lets Create a new or customized UserCreationForm 

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        # Below Fields will be displayed when the form is available in the WEB Page
        fields = [
            'first_name',
            'email',
            'username',
            'password1',
            'password2',

        ]
        # we are changing the Labels 
        labels = {
            'first_name': 'Name'
        }