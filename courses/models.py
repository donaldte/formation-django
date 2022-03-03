from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = ('Course')
        verbose_name_plural = ('Courses')


    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("courses:course-detail", kwargs={"pk": self.pk})


        
class Language(models.Model):
    name = models.CharField(max_length=20) 

    def __str__(self):
        return self.name 



class Framework(models.Model):
    name = models.CharField(max_length=20) 
    language = models.ForeignKey(Language, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name 

    
"""
CASCADE
PROTECT
SET_NULL
SET_DEFAULT
DO_NOTHTING RDBMS
"""                   

class School(models.Model):
    name = models.CharField(max_length=20)

class Student(models.Model):
    name = models.CharField(max_length=50)
    school = models.ManyToManyField(School)    

class Profile(models.Model):
    school = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
