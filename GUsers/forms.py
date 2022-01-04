from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from .models import Profile

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','profile_pic','Website','Facebook','Twitter','Instagram','Steam')
        
        widgets = {
            'bio':forms.Textarea(attrs={'class':'body-input','placeholder':'Add a description for your post'}),
            'Website':forms.TextInput(attrs={'class':'title-input','placeholder':'Add your Website'}),
            'Facebook':forms.TextInput(attrs={'class':'title-input','placeholder':'Add your Facebook'}),
            'Twitter':forms.TextInput(attrs={'class':'title-input','placeholder':'Add your Twitter'}),
            'Instagram':forms.TextInput(attrs={'class':'title-input','placeholder':'Add your Instagram'}),
            'Steam':forms.TextInput(attrs={'class':'title-input','placeholder':'Add your Steam'}),
    }

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
            label='Password', widget=forms.PasswordInput(attrs={'class':'pass-input'}))
    password2 = forms.CharField(
            label='Confirm Password(again)', widget=forms.PasswordInput(attrs={'class':'pass-input'}))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class': 'email-input', 'placeholder':'Enter your email'}))
    checkbox = forms.BooleanField(label="I agree to the rules of @GamersDen",widget=forms.CheckboxInput(attrs={'class':'checkbox'}))

    help_text = {
                'email':None,
                'username':None,
        }

    class Meta:
        model = User
        fields = ('username','email','password1','password2','checkbox')

class EditProfileForm(UserChangeForm):
    """ first_name = forms.CharField(required=False , widget=forms.TextInput(attrs={'class':'first_name'}))
        last_name = forms.CharField(required=False , widget=forms.TextInput(attrs={'class':'last_name'}))"""

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class':'form-control'}))

#    last_login = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class':'form-control'}))
#    is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
#    is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
#    is_active = forms.CharField(max_length=100 , widget=forms.CheckboxInput(attrs={'class':'form-check'}))
#    date_joined = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username','email') #'password','last_login','date_joined'

        
        
        
        