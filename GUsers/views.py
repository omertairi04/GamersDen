from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm , UserChangeForm
from django.urls import reverse_lazy

from GUsers.forms import EditProfileForm, SignUpForm

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html' 
    success_url = reverse_lazy('login')
 
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html' 
    success_url = reverse_lazy('post:explore')
    
    def get_object(self):
        return self.request.user
 

