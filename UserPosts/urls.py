from django.urls import path

from . import views

app_name = "post"

urlpatterns = [
    path('explore/', views.Explore , name='explore'),
    path('create-content/', views.create_content , name="create_content"),
    path('<slug:slug>/' , views.post_details , name="detail"),
]
