from django.contrib import auth
from django.shortcuts import render,redirect,get_object_or_404
from .models import Store
from django.contrib.auth.models import User

# Create your views here.

def new(request):
    return render(request, 'RegisterStore/registerStore-signUp.html')

def create(request): 
    new_Store=Store()
    new_Store.Store_name=request.POST['Store_name']
    new_Store.Store_tel=request.POST['Store_tel']
    new_Store.Store_add=request.POST['Store_add']
    new_Store.Store_num=request.POST['Store_num']
    new_Store.author=request.user
    new_Store.save()
    return redirect('home')

def delete(request, Store_id): #피드 삭제 함수
    delete_Store =  Store.objects.get(id=Store_id)
    delete_Store.delete()
    return redirect('home')
