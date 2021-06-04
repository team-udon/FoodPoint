from django.shortcuts import render, redirect
import csv
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'))
        auth.login(request, user)
        return render(request, 'foodpointMain.html')
    else:
        return render(request, 'signin.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect. '})

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
