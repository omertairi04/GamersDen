from django.http.response import Http404
from django.shortcuts import get_object_or_404, render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout
from gamers.models import Profile
from .forms import ProfileForm, UserRegisterForm, UserUpdateForm ,ProfileUpdateForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from verify_email.email_handler import send_verification_email
from django.views.generic import DetailView

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
    return render(request ,'gamers/signup.html', {'form':form})

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

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'gamers/gamers_details.html'
    
    def get_context_data(self, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView ,self).get_context_data(**kwargs)
        page_user = get_object_or_404(Profile ,id=self.kwargs['pk'])
        context["page_user"] = page_user 
        return context
    

"""@login_required(login_url="gamers:login")
def gamers_details(request , user):
    if request.method == "GET":
        u = Profile.objects.filter(user = request.user)
         NEW Query
        #profile_form = ProfileForm(instance=request.user.profile)
    if request.method == "POST":
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
        "u":u,
        #'user':request.user,
        #'u_profile':u_profile
    }

    return render(request , 'gamers/gamers_details.html',context) """

def o_profile(request , user):
    # If no such user exists raise 404
    try:
        user = Profile.objects.get(user = request.user)
    except:
        raise Http404
    # Flag that determines if we should show editable elements in template
    editable = False
    # Handling non authenticated user for obvious reasons
    if request.user.is_authenticated() and request.user == user:
        editable = True


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
            if 'update' in request.GET:
                return redirect(request.GET['gamers:account'])
            else:
                return redirect('index:index')
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
