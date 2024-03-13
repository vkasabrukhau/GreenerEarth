from django.db import models
from django.contrib.auth.models import User
from datetime import date

class extendedUserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    birthdate = models.DateField(("Date"), default=date.today)
    schoolEmail = models.CharField(max_length=30, default='personalMail')
    phoneNumber = models.CharField(max_length=30, default='0')

class School(models.Model):
    name = models.CharField(max_length=30, default='Blank School')
    people = models.ManyToManyField(extendedUserModel)
