from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout

from gamers.models import Profile
from .forms import UserRegisterForm, UserUpdateForm ,ProfileUpdateForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from verify_email.email_handler import send_verification_email

#from gamers.models import Gamer
from . import forms
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST , request.FILES)
        if form.is_valid():
            user = form.save()
            login(request , user)
            messages.success(request,'Your account has now been created!')
            #return redirect('gamers:validation_page')
            return redirect('index:index')
    else:
        form = forms.SignUpForm()
    return render(request ,'gamers/signup.html', { 'form':form })

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request , user)
            return redirect('index:index')
    else:
        form = AuthenticationForm()
    return render(request , 'gamers/login.html', { 'form':form })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('index:index')

@login_required(login_url="gamers:login")
def gamers_details(request,username):
    if request.method =="POST":
        u = Profile.objects.get(username = username)
        u_form = UserUpdateForm(request.POST ,instance=request.user)
        p_form = ProfileUpdateForm(request.POST ,
                                request.FILES,
                                instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('gamers:account')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request , 'gamers/gamers_details.html',context)

def update_profile(request):
    if request.method =="POST":
        u_form = UserUpdateForm(request.POST ,instance=request.user)
        p_form = ProfileUpdateForm(request.POST ,
                                request.FILES,
                                instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('gamers:account')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form,
    }

    return render(request , 'gamers/update_profile.html',context)

@login_required()
def validation_page(request):
    return render(request, 'gamers/validation_p.html')
