from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class UserDetails(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    
    address =  models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    interests = models.CharField(max_length=500)
    img=models.ImageField(upload_to='img', null=True)


class Experience(models.Model):
    title = models.CharField(max_length=100)
    companyName = models.CharField(max_length=150)
    data= models.CharField(max_length=450)
    date = models.DateField ("Date")
   


class Projects(models.Model):
    heading = models.CharField(max_length=100)
    img=models.ImageField(upload_to='img', null=True)
    desc= models.CharField(max_length=450)
   

class Education(models.Model):
    collegeName = models.CharField(max_length=100)
    date = models.DateField ("Date")
    Degree= models.CharField(max_length=450)


