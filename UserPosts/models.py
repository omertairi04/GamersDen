from django.db import models
from django.contrib.auth.models import User
import random

# Create your models here.
class UserPosts(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default="UserPosts/static/user_posts/images/noimg.png")
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE,)

    def __str__(self):
        return self.title

class VideoUpload(models.Model):
    title = title = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()
    videofile = models.FileField(upload_to="videouploads/")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class AddGame(models.Model):
    title = title = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()
    game_file = models.FileField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    