from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Store( models.Model):
    Store_name = models.TextField() 
    Store_tel = models.TextField() 
    Store_add = models.TextField() 
    Store_num = models.TextField() 
    # author= models.ForeignKey(User, related_name='store', on_delete =models.CASCADE)

    def __str__(self):
        return "가게 : " + self.Store_name
    def summary(self):
        return self.Store_name[:100]
