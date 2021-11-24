from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'GUsers/register.html' 
    success_url = reverse_lazy('login')
 
