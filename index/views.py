from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index/index.html')

def about(request):
    return render(request, 'index/about.html')

def contact(request):
    return render(request, 'index/contact.html')    
