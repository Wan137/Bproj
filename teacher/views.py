from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .models import Teacher


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        try:
            user = Teacher.objects.create(email=email, name=name)
            user.set_password(password)
            user.save()
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('index')
        except:
            messages.error(request, 'Not correct some value')
    else:
        messages.error(request, 'Not correct password')
    return render(request, 'users/register.html')


def login_user(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = Teacher.objects.get(email=email)
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('index')
        except:
            messages.error(request, 'Not correct login or password')
    return render(request, 'users/login.html')
