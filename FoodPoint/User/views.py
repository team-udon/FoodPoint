from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def getPoint(request):
    return render(request, 'getPoint.html')

def photoUpload(request):
    new_post = Post()
    new_post.photo =  request.FILES['image']
    new_post.user = request.POST['user']
    new_post.pub_date = timezone.now()
    new_post.save()
 