from django.urls import path
from .views import Explore , PostDetailView

app_name = "post"

urlpatterns = [
    path('explore/',Explore.as_view() , name="explore"),
    path('post/<int:pk>/',PostDetailView.as_view(), name="post-detail"),
]
