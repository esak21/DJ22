from lib2to3.pytree import Base
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """ Manager for the User Profiles"""

    def create_user(self,email,name,password=None):
        """ Create a new User Profile """
        if not email: 
            raise ValueError("ERROR: USER MUST HAVE VALID EMAIL")
        # normalize will lower all the letters in the second half (after the @)
        email = self.normalize_email(email)

        user = self.model(email=email, name=name)
        # AbstractBaseUser model comes with the set_password , 
        # #we want to make sure password is converted to HASH and never stored as plain text 
        user.set_password(password)
        
        user.save(using=self._db) # standard procdure to save a model 

        return user

    def create_superuser(self, email, name, password):
        """ Create a new Super user """

        user = self.create_user(email=email, name=name, password=password)
        # adding user as superuser
        user.is_superuser = True
        user.is_staff = True

        # savin the user 
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database Model for users in the System"""
    email = models.EmailField(max_length=255, unique=True)
    name=models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) # if the user profile is activated or not 
    is_staff=models.BooleanField(default=False) # if the user is Admin or Not  

    # Django uses the CLI to Create super users for that to work we have to create the custom model Manager 
    objects = UserProfileManager() 

    # To Work With Django admin and authentication 
    # we have to specify the userName Field 
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['name']

    # Django to interact with custom user Model 

    def get_full_name(self ):
        """ Retrieve Full Name of the User"""
        return self.name
    
    def get_short_name(self):
        """ REtrieve short name of the user"""
        return self.name

    def __str__(self):
        """ String Representation of the Object"""
        return self.email



class ProfileFeedItem(models.Model):
    """ Profile Sttaus Update """
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # user profile is referenced here 
        on_delete=models.CASCADE
        )
    status_text = models.CharField(max_length=255)
    created_on = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.status_text