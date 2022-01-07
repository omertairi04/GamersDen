from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , null=True)
    bio = models.TextField(null=True , blank=True , default=None)
    profile_pic = models.ImageField(null=True,blank=True, upload_to ='user/profile_pics')
    Website = models.CharField(max_length=255, null=True,blank=True)
    Facebook = models.CharField(max_length=255, null=True,blank=True)
    Twitter = models.CharField(max_length=255, null=True,blank=True)
    Instagram = models.CharField(max_length=255, null=True,blank=True)
    Steam = models.CharField(max_length=255, null=True,blank=True)
    
    following = models.ManyToManyField(
        "self",blank=True,related_name="followers",symmetrical=False,
    )

    def __str__(self):
        return f'{self.user.username} Profile' 

    def get_absolute_url(self):
        return reverse("index:index")