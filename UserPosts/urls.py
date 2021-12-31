from django.urls import path
from .views import AddGameView, AddPostView, CreateContent, DeleteCommentView, DeleteGameView, DeletePostView, Explore, GameDetailView, GameView, GameLikeView,LikeView, PlayPageView , PostDetailView, UpdateCommentView, UpdateGameView, UpdatePostView

app_name = "post"

urlpatterns = [
    path('explore/',Explore.as_view() , name="explore"),
    path('<int:pk>/',PostDetailView.as_view(), name="post-detail"),
    path('game/<int:pk>/',GameDetailView.as_view(), name="game-detail"),
    path('add-post/', AddPostView.as_view(),name="create_post"),
    path('create/', CreateContent,name="create"),
    path('edit/<int:pk>',UpdatePostView.as_view(),name="update-post"),
    path('delete/<int:pk>/',DeletePostView.as_view(),name="delete-post"),
    path('add-game/',AddGameView.as_view(),name="add-game"),
    path('game/<str:game>/', GameView , name="game-view"),
    path('like/<int:pk>/', LikeView , name="like_post"),
    path('like-game/<int:pk>', GameLikeView ,name="like_game"),
    path('edit/comment/<int:pk>', UpdateCommentView.as_view(),name="edit-comment"),
    path('delete/comment/<int:pk>', DeleteCommentView.as_view(),name="delete-comment"),
    path('games/', PlayPageView.as_view(), name="playpage"),
    path('edit-game/<int:pk>',UpdateGameView.as_view(),name="update-game"),
    path('delete-game/<int:pk>/',DeleteGameView.as_view(),name="delete-game"),
]
