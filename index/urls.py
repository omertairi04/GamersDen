from django.urls import path

app_name = "index"

from . import views

urlpatterns = [
    # FOR YOU PAGE
    path('', views.index , name = "index"),
    path('welcome/', views.welcome, name="welcome"),
    path('about/', views.about ,name="about"),
    path('contact/', views.contact ,name="about"),
]