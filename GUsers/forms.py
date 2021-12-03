from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class': 'email-input'}))
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def __init__(self,*args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'username-input'
        self.fields['password1'].widget.attrs['class'] = 'pass-input'
        self.fields['password2'].widget.attrs['class'] = 'pass-input'
 
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

        
        
        
        