from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.fields import ImageField
from . import models

class CreatePost(forms.ModelForm):
    title = forms.CharField(max_length=50 ,widget=widgets.TextInput(attrs={'class':'title'}))
    description = forms.CharField(widget=widgets.Textarea(attrs={'class':'description'}))
    class Meta:
        model = models.UserPosts
        fields= ['title','slug','description','thumb']  
        
class UploadVideo(forms.ModelForm):
    class Meta:
        model = models.VideoUpload
        fields = ['title', 'slug','description','videofile']
