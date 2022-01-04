from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
# FOR YOU PAGE
@login_required(login_url=('/welcome/'))
def index(request):
    return render(request, 'index/index.html')

def about(request):
    return render(request, 'index/about.html')

def contact(request):
    return render(request, 'index/contact.html')    

def welcome(request):
    return render(request , 'index/welcome.html')
