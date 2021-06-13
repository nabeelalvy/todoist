from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
from django.urls import resolve


def login_page(request):
    if request.user.is_authenticated:
        return render(request, 'todoit/home.html')
        # redirect(to='home')
    else:
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'todoit/home.html')
                # redirect('home')
            else:
                messages.info(request, "Username OR Password is incorrect")

        context = {}
        return render(request, 'user_reg/login.html', context)


def logmeout(request):
    logout(request)
    return render(request, 'user_reg/login.html')


def register_page(request):
    logout(request)
    if request.user.is_authenticated:
        redirect('/user/')
    else:
        if request.POST:
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            user = User(username=username, first_name=first_name, last_name=last_name, email=email)
            user.set_password(password)
            user.save()
            messages.success(request, "Account was created for " + username)
            # redirect('login')
            return render(request, 'user_reg/login.html')
        else:
            return render(request, 'user_reg/register.html')
