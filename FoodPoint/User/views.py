from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def getPoint(request):
    return render(request, 'getPoint.html')

def photoUpload(request):
    new_post = Post()
    new_post.photo =  request.FILES['image']
    new_post.user = request.POST.get('user','')
    new_post.pub_date = timezone.now()
    new_post.save()

    return redirect('home')