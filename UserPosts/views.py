from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . models import UserPosts
from . import forms

# Create your views here.
def Explore(request):
    posts = UserPosts.objects.all().order_by('date')
    context = {
        'posts':posts
    }
    return render(request, 'UserPosts/explore.html', context)

def post_details(request , slug):
    # return HttpResponse(slug)
    post = UserPosts.objects.get(slug=slug)
    context={
        'post':post
    }
    return render(request,'UserPosts/post_detail.html' ,context)

@login_required()
def create_content(request):
    return render(request,'UserPosts/create_content.html')
"""
def create_image(request):
    form = forms.CreatePost()
    return render(request , 'UserPosts/post_image.html',{'form':form})
"""
