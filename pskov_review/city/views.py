from .models import City
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'city/loginuser.html',
                      {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'city/loginuser.html',
                          {'form': AuthenticationForm(), 'error': "Неверны логин или пароль"})
        else:
            login(request, user)
            return redirect('currentuser')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


def index(request):
    projects = City.objects.all()
    return render(request, 'city/index.html', {'projects': projects})


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'city/signupuser.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentuser')
            except IntegrityError:
                return render(request, 'city/signupuser.html', {'form': UserCreationForm,
                                                                'error': "Пользователь с таким именем уже существует"})
        else:
            return render(request, 'city/signupuser.html', {'form': UserCreationForm,
                                                            'error': "Пароли не совпадают"})


def currentuser(request):
    return render(request, 'city/currentuser.html')
