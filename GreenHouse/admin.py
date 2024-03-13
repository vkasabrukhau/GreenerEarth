from django.contrib import admin
from .models import extendedUserModel, School

# Register your models here.
admin.site.register(extendedUserModel)
admin.site.register(School)