from email.policy import default
import uuid
from django.db import models

# Create your models here.

class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    # primary_key make this column as primary in database 
    # editable False which makes user can't touch in Form 
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    # null True means we are allowed to enter a row in DB as null
    # blank=true we are allowed to enter a balnk rec in the FORM 
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    # we are telling its a MANYTOMANY 
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) # create a timestamp automatically 

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'UP Vote'),
        ('down', 'DOWN Vote')
        
    )
    #owner
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # establish the ONETOMANY Relationship 
    # we created a Foreign Key if the project is deleted all the child will be deleted models.CASCADE
    body = models.TextField(null = True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField( default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self) -> str:
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField( default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self) -> str:
        return self.name

# lets bring the Django User Model 
from django.contrib.auth.models import User

class ProjecDetails(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    responsible = models.ForeignKey(User, on_delete=models.CASCADE)
    week_numer = models.CharField(max_length=2, blank=True)
    end_date = models.DateField()

    def __str__(self) -> str:
        return str(self.name)

    def save(self, *args, **kwargs):
        print(self.start_date.isocalendar()[1])
        if self.week_numer == "":
            self.week_numer = self.start_date.isocalendar()[1]

        super().save(*args, **kwargs)
