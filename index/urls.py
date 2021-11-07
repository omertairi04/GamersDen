from django.urls import path

app_name = "index"

from . import views

urlpatterns = [
    path('', views.index , name = "index"),
    path('about/', views.about ,name="about"),
    path('contact/', views.contact ,name="about"),
]