from django.urls import path
from .views import AddGameView, AddPostView, CreateContent, DeleteCommentView, DeletePostView, Explore, GameView, LikeView , PostDetailView, UpdateCommentView, UpdatePostView
app_name = "post"

urlpatterns = [
    path('explore/',Explore.as_view() , name="explore"),
    path('<int:pk>/',PostDetailView.as_view(), name="post-detail"),
    path('add-post/', AddPostView.as_view(),name="create_post"),
    path('create/', CreateContent,name="create"),
    path('edit/<int:pk>',UpdatePostView.as_view(),name="update-post"),
    path('delete/<int:pk>/',DeletePostView.as_view(),name="delete-post"),
    path('add-game/',AddGameView.as_view(),name="add-game"),
    path('game/<str:game>/', GameView , name="game-view"),
    path('like/<int:pk>/', LikeView , name="like_post"),
    path('edit/comment/<int:pk>', UpdateCommentView.as_view(),name="edit-comment"),
    path('delete/comment/<int:pk>', DeleteCommentView.as_view(),name="delete-comment"),
]
