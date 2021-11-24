from typing import List
from django.db import models
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from UserPosts.models import Post

class Explore(ListView):
    model = Post 
    template_name = 'UserPosts/explore.html'
    
class PostDetailView(DetailView):
    model = Post
    template_name = "UserPosts/post_detail.html"

