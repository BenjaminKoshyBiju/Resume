from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class UserDetails(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    user = models.ForeignKey(User,default=None, on_delete=models.CASCADE)
    address =  models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    interests = models.CharField(max_length=500)


class Experience(models.Model):
    title = models.CharField(max_length=100)
    companyName = models.CharField(max_length=150)
    data= models.CharField(max_length=450)
    user = models.ForeignKey(User,default=None, on_delete=models.CASCADE)


class Projects(models.Model):
    heading = models.CharField(max_length=100)
    img=models.ImageField(upload_to='img', null=True)
    desc= models.CharField(max_length=450)
    user = models.ForeignKey(User,default=None, on_delete=models.CASCADE)

class Education(models.Model):
    collegeName = models.CharField(max_length=100)
    date = models.DateField ("Date")
    Degree= models.CharField(max_length=450)
    user = models.ForeignKey(User,default=None, on_delete=models.CASCADE)

