from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import extendedUserModel, School

def signup(request):
    schoolios = School.objects.all()
    context={
        'schools': schoolios,
    }
    


# Create your views here.
