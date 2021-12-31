from django.forms import fields
from django.views.generic import ListView, DetailView ,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required 
from django.shortcuts import redirect, render , get_object_or_404
from . forms import AddGameForm, CommentForm, EditCommentForm, EditGameForm, PostForm , EditForm
from django.urls import reverse_lazy , reverse
from UserPosts.models import Comment, Game, Post
from django.http import HttpResponseRedirect, request

# MAIN PAGES VIEWS

class Explore(ListView):
    model = Post 
    template_name = 'UserPosts/explore.html'
    ordering = ['-post_date']
    
    def get_context_data(self, *args, **kwargs):
        game_menu = Game.objects.all()
        context = super(Explore , self).get_context_data(*args, **kwargs)
        context['game_menu'] = game_menu
        return context

class PlayPageView(ListView):
    model = Game
    template_name = 'UserPosts/playpage.html'
    ordering = ['-date_added']

def GameView(request , game): # game = <str:game>
    game_posts = Game.objects.filter(game = game.replace('-' ,' '))
    return render(request, 'UserPosts/games.html', {'game':game.title().replace('-' ,' ') 
                                                    , 'game_posts':game_posts})

def CreateContent(request):
    return render(request , 'UserPosts/create.html')

# DETAIL VIEWS

class PostDetailView(DetailView):
    model = Post
    template_name = "UserPosts/post_detail.html"
    form = CommentForm
    def post(self, request, pk,*args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return HttpResponseRedirect(reverse('post:post-detail' , args=[str(pk)]))
    
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
        context['form'] = self.form
        return context

class GameDetailView(DetailView):
    model = Game
    template_name = "UserPosts/game_detail.html"

    form = CommentForm
    def game(self, request, pk,*args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            game = self.get_object()
            form.instance.user = request.user
            form.instance.game = game
            form.save()
            return redirect(reverse('post:game-detail' , args=[str(pk)]))
    
    def get_context_data(self, *args, **kwargs):
        game_menu = Game.objects.all()
        context = super(GameDetailView , self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Game, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        # stuff == game_posts ose dishka tjeter
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context['game_menu'] = game_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        context['form'] = self.form
        return context


# ADD VIEWS
    
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
    form_class = AddGameForm
    template_name = "UserPosts/add_game.html"
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.published_by = self.request.user
        self.object.save()
        return super().form_valid(form)
    
# UPDATE VIEWS
    
class UpdateGameView(UpdateView):
    model = Game
    form_class = EditGameForm
    template_name = "UserPosts/update_game_view.html"
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "UserPosts/update_post.html"

class UpdateCommentView(UpdateView):
    model = Comment
    form_class = EditCommentForm
    template_name = "UserPosts/edit_comment.html"
    success_url = reverse_lazy('post:explore')

# DELETE VIEWS
    
class DeleteGameView(DeleteView):
    model = Game
    template_name = "UserPosts/delete_game.html"
    success_url = reverse_lazy('post:playpage')

class DeletePostView(DeleteView):
    model = Post
    template_name = "UserPosts/delete_post.html"
    success_url = reverse_lazy('post:explore')
    
class DeleteCommentView(DeleteView):
    model = Comment
    template_name = "UserPosts/delete_comment.html"
    success_url = reverse_lazy('post:explore')

# LIKE VIEWS
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
    return redirect(reverse('post:post-detail' , args=[str(pk)]))

def GameLikeView(request, pk):
    game = get_object_or_404(Game , id=request.POST.get('game_id'))
    liked = False
    if game.likes.filter(id=request.user.id).exists():
        game.likes.remove(request.user)
        liked = False
    else:
        game.likes.add(request.user)
        liked=True
    return redirect(reverse('post:game-detail' , args=[str(pk)]))

