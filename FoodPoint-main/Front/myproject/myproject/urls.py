
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
import myapp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', myapp.views.SignIn, name='SignIn'),
    path('auth/',include('users.urls')),
]
