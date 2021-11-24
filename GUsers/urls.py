from django.urls import path
from GUsers import views
from GUsers.views import UserRegisterView

app_name = 'GUsers'

urlpatterns = [
    path('register/',UserRegisterView.as_view() , name="register"),
#   path('login/', views.login_view , name="login"),
#   path('logout/', views.logout_view , name="logout"),
]
