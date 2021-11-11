from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path('explore/', views.Explore , name='explore'),
    path('create/' , views.CreateContent.create , name="create"),
    path('create-post/', views.CreateContent.create_post , name="create_post"),
    path('add-clip/',views.CreateContent.add_clip , name="add-clip"),
    path('add-a-game/', views.CreateContent.add_game , name="add-game"),
    path('<slug:slug>/' , views.post_details , name="detail"),
]
