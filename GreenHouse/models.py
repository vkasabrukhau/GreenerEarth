from django.db import models
from django.contrib.auth.models import User
from datetime import date

class School(models.Model):
    name = models.CharField(max_length=30, default='Blank School')

    def __str__(self):
        return self.name

class extendedUserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    birthdate = models.DateField(("Date"), default=date.today)
    schoolEmail = models.CharField(max_length=30, default='personalMail')
    phoneNumber = models.CharField(max_length=30, default='0')
    school = models.ForeignKey(School, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
