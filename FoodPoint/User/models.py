from django.db import models

# Create your models here.

class Post(models.Model):
    photo = models.ImageField(upload_to = "photos/%m/%d",blank = True, null = True)
    user = models.CharField(max_length = 100)
    pub_date = models.DateTimeField()
