from django.contrib.auth import logout
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView , CreateView
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm , UserChangeForm
from django.urls import reverse_lazy

from GUsers.forms import EditProfileForm, ProfilePageForm, SignUpForm
from GUsers.models import Profile

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    
    def get_context_data(self, *args,**kwargs):
        user = Profile.objects.all()
        context = super(ShowProfilePageView , self).get_context_data(*args, **kwargs)
        #
        page_user = get_object_or_404(Profile , id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic','Website','Facebook','Twitter','Instagram','Steam']
    success_url = reverse_lazy('index:index')
    
    
    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
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
 
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name="registration/change-password.html"
    success_url = reverse_lazy('post:explore')
