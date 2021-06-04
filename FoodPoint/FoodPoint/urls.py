"""FoodPoint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Main.views import *
from Store.views import *
from User.views import *
from Accounts.views import *
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signIn/', signIn, name="signIn"),
    path('introduce/', introduce, name="introduce"),
    path('register/', register, name="register"),
    path('search/', search, name="search"),
    path('User/getPoint', getPoint, name="getpoint"),
    path('User/photoUpload', photoUpload, name="photoUpload"),
    
    path('accounts/signup/', signup, name="signup"),
    path('accounts/login/', login, name="login"),
    path('accounts/logout', logout, name='logout'),
    path('store/new', new, name='new'),
    path('store/create', create, name='create'),
    path('store/delete/<int:Store_id>', delete, name='delete'),
    path('store/edit/<int:Store_id>', edit, name='edit'),
    path('store/update/<int:Store_id>', update, name='update'),
    path('store/storeList', storeList, name='storeList'),
    path('store/detail/<int:Store_id>', detail, name='detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
