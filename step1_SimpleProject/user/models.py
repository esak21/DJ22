import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# BaseUserManager - provides allows us to create a new user and create super user  
# Create your models here.

class TicketingBaseManager(BaseUserManager):
    def create_user(self,email, password, name,  mobileno,userimage, lastname=None, **other_fields):
        if not email: 
            raise ValueError("ERROR::  EMAIL is Not Provided")

        email = self.normalize_email(email) # lowecase the domain part 
        
        user = self.model(
            email= email,
            name= name, 
            mobileno = mobileno,
            lastname=lastname, 
            userimage=userimage
            **other_fields
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, name, mobileno, lastname, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)

        

        # LETS add Validation 
        if other_fields.get('is_staff') is not True:
            raise ValueError('SUPERUSER must be assigned to is_staff:True')

        if other_fields.get('is_active') is not True:
            raise ValueError('SUPERUSER must be assigned to is_active:True')        
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError('SUPERUSER must be assigned to is_superuser:True')

        return self.create_user(email, password, name, mobileno, lastname, **other_fields)
        


class TicketingUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff =models.BooleanField(default=False)
    description = models.TextField(max_length=500, blank=True)
    userimage = models.FileField(null=True, blank=True, upload_to="images/") 
    lastname = models.CharField(max_length=50, blank=True)
    mobileno = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    # Specify the Manager 
    objects = TicketingBaseManager()

    # Which column to be used as username 
    USERNAME_FIELD =  'email'

    # REQUIRED Fields when creating the superuser
    # email is available by default
    
    REQUIRED_FIELDS = ['name','mobileno', 'lastname'  ]

    def get_full_name(self):
        if self.lastname:
            return  f"{self.name}{self.lastname}"
        return f"{self.name}"


    def get_mobile_number(self):
        return self.mobileno

    def __str__(self) -> str:
        return self.name
    