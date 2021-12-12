from django import forms
from django.forms import widgets
from .models import CATEGORIES, Comment, Post ,Game

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

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            'rows':'4',    
        }))

    class Meta:
        model = Comment
        fields = ('body',)

class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        
        widgets = {
            'body':forms.Textarea(attrs={'class':'body-input','placeholder':'Add a comment'})
        }

class AddGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name','description','game_image','category','steam_page')
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'name-input','placeholder':"Your game's name"}),
            'description':forms.Textarea(attrs={'class':'body-input','placeholder':'Add a description for your game'}),
            'category': forms.Select(choices=CATEGORIES,attrs={'class':'select-category'}),
            'steam_page':forms.TextInput(attrs={'class':'name-input','placeholder':"Link your steam game page :p"}),
        }

