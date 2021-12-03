from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime , date
from ckeditor.fields import RichTextField


class Game(models.Model):
    name = models.CharField(max_length=255,blank=False,null=False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Game, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post:explore")

class Post(models.Model):
    title = models.CharField(max_length=255,blank=False,null=False)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    game = models.CharField(max_length=255,default='Minecraft')
    body = RichTextField(blank=True , null=True)
    # body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User , related_name="game_posts")
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def snippet(self):
        if self.body > '[:50]':
            return self.body[:50] + '...'
        else:
            return self.body[:50] + '...'
        
    def get_absolute_url(self):
        return reverse("post:explore")
    
    