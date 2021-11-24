from django.urls import path
from . import views

app_name = "gamers"

urlpatterns = [
    path('signup/', views.signup_view , name='signup'),
    path('login/', views.login_view , name='login'),
    path('logout/', views.logout_view , name="logout"),
#   path('account/<str:user>/', views.gamers_details , name="account"),
    path('accounts/<str:ouser>/', views.o_profile , name="o_profile"),
    path('update_account/', views.update_profile , name="update_profile"),
#   path('verify_account/', views.validation_page , name="verify_page"),
    path('account/<int:pk>/profile', views.ShowProfilePageView , name="show_profile_page"),
]

