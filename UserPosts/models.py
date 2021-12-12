from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.urls import reverse
from datetime import datetime , date
from ckeditor.fields import RichTextField

CATEGORIES = (
    ('Shooter','Shooter'),
    ('RPG','RPG'),
    ('Online','Online'),
    ('Offline','Offline')
)
    

class Game(models.Model):
    name = models.CharField(max_length=255,blank=False,null=False)
    description = models.TextField(max_length=500 , blank=True,null=True , default=None)
    game_image = models.ImageField(null=False , blank=False ,upload_to="games/images", default="root/playpage/images/def_img.jpg")
    category = models.CharField(choices=CATEGORIES,max_length=255,default='Shooter')
    published_by = models.ForeignKey(User , related_name="published_by",on_delete=models.CASCADE)
    steam_page = models.CharField(max_length=255 , blank=True ,null=True)
    date_added = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User , related_name="liked_games")
    
    def __str__(self):
        return self.name
    
    def total_likes(self):
        return self.likes.count()
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Game, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post:playpage")


class Post(models.Model):
    title = models.CharField(max_length=255,blank=False,null=False)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    header_image = models.ImageField(null=False , blank=False ,upload_to="user/images", default="UserPosts/static/user_posts/images/game.png")
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

class Comment(models.Model):
    user = models.ForeignKey(User , related_name="comments",on_delete=models.CASCADE)
    post = models.ForeignKey(Post , related_name="comments",on_delete=models.CASCADE)
    body = models.TextField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.post.title , self.user.username)

