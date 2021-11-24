from django.contrib.auth.models import User
from django.db import models
import random

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255,blank=False,null=False)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    body = models.TextField()
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    