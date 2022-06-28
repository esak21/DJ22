from django.db import models
from django.forms import CharField

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=25)

    # Create Releationship 
    # A Language Python was known by many programmers 
    # A Single Programmer can know many lanaguages like python jave ruby 
    # so its a manyToMaany relationship , we need to put this logically 

    def __str__(self) -> str:
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=100)

    # create relationship between programmer and company 
    # if a company is deleted , then that refers in each column has to be deleted as well 
    company = models.ForeignKey(Company, on_delete= models.CASCADE)

    # manytomany relationship Field 
    # Language class has to be moved up 
    languages = models.ManyToManyField(Language)
    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=25)
    # create Foreign Key here 
    # this Column represent another Table 
    language = models.ForeignKey(Language, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=25)


    def __str__(self) -> str:
        return self.name