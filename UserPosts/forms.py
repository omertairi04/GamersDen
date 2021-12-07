from django import forms
from django.forms import widgets
from .models import Post , Game

choices = Game.objects.all().values_list('name','name')

game_choices = []

for game in choices:
    game_choices.append(game)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','game','body','header_image') #'author'
        
        widgets = {
            'title':forms.TextInput(attrs={'class':'title-input','placeholder':'Create a title'}),
#           'author': forms.Select(attrs={'class':'select-author'}),
            'game': forms.Select(choices=game_choices,attrs={'class':'select-game'}),
            'body':forms.Textarea(attrs={'class':'body-input','placeholder':'Add a description for your post'}),
        }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body', 'game')
        
        widgets = {
            'title':forms.TextInput(attrs={'class':'title-input','placeholder':'Create a title'}),
#           'author': forms.Select(attrs={'class':'select-author'}),
            'body':forms.Textarea(attrs={'class':'body-input','placeholder':'Add a description for your post'}),
            'game': forms.Select(choices=game_choices,attrs={'class':'select-game'}),
        }
