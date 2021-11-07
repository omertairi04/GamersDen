from django.urls import path

from . import views

name = 'play'

urlpatterns = [
    path('', views.playpage , name="playpage")
]
