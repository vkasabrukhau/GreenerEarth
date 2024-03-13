from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import extendedUserModel, School

def signup(request):
    schoolios = School.objects.all()
    context={
        'schools': schoolios,
    }
    if(request.method == "POST"):
        firstName = request.POST['firstname']
        lastName = request.POST['lastname']
        birthday = request.POST['birthdate']
        cellNumber = request.POST['phonenumber']
        email = request.POST['email']
        school = request.POST['school']
        password = request.POST['password']
        
        if(User.objects.filter(email=email).exists):
            messages.info("This e-mail is already taken")
            return render(request, "signup.html", context)
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.set_password(password)
            user.save()

            extendedUser = extendedUserModel.objects.create(user=user, birthdate = birthday, schoolEmail = email, phoneNumber = cellNumber)
            extendedUser.save()

            selected_school = School.objects.get(name=school)
            selected_school.people.add(extendedUser)



    return render(request, "signup.html", context)

def signin(request):
    return render(request, "signin.html")


# Create your views here.
