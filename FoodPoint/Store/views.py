from django.contrib import auth
from django.shortcuts import render,redirect,get_object_or_404
from .models import Store
from django.contrib.auth.models import User

# Create your views here.

def storeList(request):
    stores=Store.objects.all()
    return render(request, 'searchResult.html',{'stores':stores}) #첫화면

def detail(request, Store_id):
    store=get_object_or_404(Store,pk=Store_id)
    return render(request, 'storeMain.html',{'store':store}) #피드 디테일화면

def new(request):
    return render(request, 'registerStore-signUp.html')

def create(request): 
    new_Store=Store()
    new_Store.Store_name=request.POST.get('Store_name', '')
    new_Store.Store_tel=request.POST.get('Store_tel', '')
    new_Store.Store_add=request.POST.get('Store_add', '')
    new_Store.Store_num=request.POST.get('Store_num', '')
    new_Store.author=request.user
    new_Store.save()
    return redirect('home')

def delete(request, Store_id): # 삭제 함수
    delete_Store =  Store.objects.get(id=Store_id)
    delete_Store.delete()
    return redirect('home')

def edit(request, Store_id): # 피드 수정 페이지 출력 함수
    edit_store = Store.objects.get(id=Store_id)
    return render(request, 'registerStore-edit.html', {'edit_store':edit_store})

def update(request, Store_id): # 수정 함수 post로 db 수정
    update_Store = Store.objects.get(id=Store_id)
    update_Store.Store_name=request.POST.get('Store_name', '')
    update_Store.Store_tel=request.POST.get('Store_tel', '')
    update_Store.Store_add=request.POST.get('Store_add', '')
    update_Store.Store_num=request.POST.get('Store_num', '')
    update_Store.save()
    return redirect('detail', update_Store.id)