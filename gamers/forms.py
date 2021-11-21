from typing import Text
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.db.models.fields import TextField
from django.forms import widgets
from django.forms.fields import ImageField
from django.utils import timezone
from django.forms.widgets import EmailInput, PasswordInput, TextInput, Textarea
from .models import Profile

class AccountForm(forms.Form):
    pass
    #username = forms.CharField(max_length=20)
    #bio = forms.CharField(widget=forms.Textarea(attrs={'class':'description_box'}))
    #pfp = forms.ImageField(label="Enter a profile picture") # default = "static/gamers/defpfp.jpg"
    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #bio

class usernamefield(forms.CharField):
    def to_python(self, value):
        return value.lower()

class SignUpForm(UserCreationForm , forms.ModelForm):

    GENDER =(
    ("M", "Male"),
    ("F", "Female"),
)

    username = usernamefield(max_length=100,widget=TextInput(attrs={'class':'username'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'class':'password'}) , label="Enter your password:")
    password2 = forms.CharField(widget=PasswordInput(attrs={'class':'password'}) , label="Re-enter your password:")
    email = forms.EmailField(required=True ,widget=EmailInput(attrs={'class':'emailfield'}) ,label="Enter your email")
    image = forms.ImageField(required=False)
    gender = forms.ChoiceField(choices=GENDER)
    date_born = forms.DateField(
        widget=forms.SelectDateWidget(
            years=[x for x in range(1940,timezone.now().date().year + 1)],
            attrs={
                'class': 'date_born',
            }
        )
    )
    class Meta:
        model = User
        fields = ["username","password1","password2",'date_born', "email",'image','gender'] #"birthdate"


    def save(self , commit=True):
        user = super(SignUpForm , self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.date_born = self.cleaned_data['date_born']
        user.image = self.cleaned_data['image']
        user.gender = self.cleaned_data['gender']


        if commit:
            user.save()
        return user

    def clean_date_born(self):
        date_born = self.cleaned_data.get('date_born')
        if timezone.now().date() - date_born < timezone.timedelta(6574):
            raise ValidationError('You are under 18.')
        return date_born
        

class UserUpdateForm(forms.ModelForm):
    GENDER = (
        ('M','MALE'),
        ('F','FEMALE')
    )
    username = usernamefield()
    email = forms.EmailField()

    class Meta:
        model = User
        fields=('username','email') #'bio'

class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(widget=Textarea(attrs={
        'class':'description_box',
    }), label="Enter your description")
    class Meta:
        model = Profile
        fields=['image', 'bio', 'gender']
""" NEW FORM """
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=('user','image','bio','gender')
