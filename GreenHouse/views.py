from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import extendedUserModel, School
import datetime

now = datetime.datetime.now()

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
        school = request.POST['schoolinput']
        password = request.POST['password']
        
        if(User.objects.filter(email = email).exists()):
            messages.info("This e-mail is already taken")
            return render(request, "signup.html", context)
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.set_password(password)
            user.save()

            user.first_name = firstName
            user.last_name = lastName
            user.date_joined = now

            user.save()
            selected_school = School.objects.get(name=school)
            extendedUser = extendedUserModel.objects.create(user=user, birthdate = birthday, schoolEmail = email, phoneNumber = cellNumber, school=selected_school)
            extendedUser.save()

            user_login = authenticate(username = email, password = password)
            login(request, user_login)
            return redirect('/')
    else:
        return render(request, "signup.html", context)

def signin(request):
    if(request.method == "POST"):
        user_login = authenticate(username = request.POST["email"], password = request.POST["password"])
        if user_login is not None:
            login(request, user_login)
            return redirect('/')
        else:
            return redirect('signin')
    else:
        return render(request, 'signin.html')

@login_required
def home(request):
    return render(request, 'signin.html')


# Create your views here.
