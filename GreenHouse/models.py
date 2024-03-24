from django.db import models
from django.contrib.auth.models import User
from datetime import date
from colorfield.fields import ColorField
from django.core.validators import int_list_validator
from datetime import date

class extendedUserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    birthdate = models.DateField(("Date"), default=date.today)
    schoolEmail = models.CharField(max_length=30, default='personalMail')
    phoneNumber = models.CharField(max_length=30, default='0')
    role = models.CharField(max_length=30, default="Student")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class leafChange(models.Model):
    length = models.IntegerField(default = 0)
    width = models.IntegerField(default = 0)
    color = ColorField()

class leaf(models.Model):
    healthy = models.BooleanField(default = True)
    plant_updates = models.ManyToManyField(leafChange)

class plantHeights(models.Model):
    height = models.IntegerField(default = 50)
    date = models.DateField(("Date"), default=date.today)

class plant(models.Model):
    name = models.CharField(max_length=30, default="Plantie")
    type = models.CharField(max_length=30, default='')
    idealTemp = models.IntegerField(default=70)
    idealMoisture = models.IntegerField(default=70)
    idealSoilMoisture = models.IntegerField(default=30)
    heightUpdates = models.ManyToManyField(plantHeights)

class quandrant(models.Model):
    humidity = models.IntegerField(default=40)
    temperature = models.IntegerField(default=40)
    acidity = models.IntegerField(default=40)
    soil_moisture = models.IntegerField(default=40)
    plants = models.ManyToManyField(plant)
    arduino_status = models.BooleanField(default=False)

class box(models.Model):
    quandrants = models.ManyToManyField(quandrant)
    max_num_plants = models.IntegerField(default=20)
    plants_occupied = models.IntegerField(default=0)
    health_rating = models.IntegerField(default=80)
    plant_types = models.IntegerField(default=5)
    temp_avg = models.IntegerField(default=80)
    humidity_avg = models.IntegerField(default=80)

class School(models.Model):
    name = models.CharField(max_length=30, default='Blank School')
    boxes = models.ManyToManyField(box)

    def __str__(self):
        return self.name