from django.forms import fields
from django.views.generic import ListView, DetailView ,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required 
from django.shortcuts import redirect, render , get_object_or_404
from .forms import PostForm , EditForm
from django.urls import reverse_lazy , reverse
from UserPosts.models import Game, Post
from django.http import HttpResponseRedirect

def LikeView(request , pk):
    post = get_object_or_404(Post , id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    # ADD JQUERY
    return HttpResponseRedirect(reverse('post:post-detail' , args=[str(pk)]))

class Explore(ListView):
    model = Post 
    template_name = 'UserPosts/explore.html'
    ordering = ['-post_date']
    
    def get_context_data(self, *args, **kwargs):
        game_menu = Game.objects.all()
        context = super(Explore , self).get_context_data(*args, **kwargs)
        context['game_menu'] = game_menu
        return context

def GameView(request , game): # game = <str:game>
    game_posts = Post.objects.filter(game = game.replace('-' ,' '))
    return render(request, 'UserPosts/games.html', {'game':game.title().replace('-' ,' ') 
                                                    , 'game_posts':game_posts})

class PostDetailView(DetailView):
    model = Post
    template_name = "UserPosts/post_detail.html"

    def get_context_data(self, *args, **kwargs):
        game_menu = Game.objects.all()
        context = super(PostDetailView , self).get_context_data(*args, **kwargs)
        
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context['game_menu'] = game_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "UserPosts/create_post.html"
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class AddGameView(CreateView):
    model = Game
    #form_class = PostForm
    template_name = "UserPosts/add_game.html"
    fields = '__all__'
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "UserPosts/update_post.html"

def CreateContent(request):
    return render(request , 'UserPosts/create.html')

class DeletePostView(DeleteView):
    model = Post
    template_name = "UserPosts/delete_post.html"
    success_url = reverse_lazy('post:explore')
    