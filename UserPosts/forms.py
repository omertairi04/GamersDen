from django import forms
from django.db.models import fields
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.UserPosts
        fields= ['title', 'slug','description','thumb']  
