from typing import List
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
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
class CreateContent():
    def create(request):
        return render(request , 'UserPosts/create.html')
    
    def create_post(request):
        #template_name = 'edit.html'
        if request.method == "POST":
            form = forms.CreatePost(request.POST , request.FILES)
            if form.is_valid():
                user_post = form.save(commit=False)
                user_post.posted_by = request.user
                user_post.save()
                return redirect('index:index')
        else:
            form = forms.CreatePost()
        return render(request,'UserPosts/create_post.html', {'form':form})
            
        
    def add_clip(request):
        return HttpResponse('Create a clip')
    
    def add_game(request):
        return HttpResponse('Add a Game')

