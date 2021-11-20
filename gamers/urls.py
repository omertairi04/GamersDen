from django.urls import path

from . import views

app_name = "gamers"

urlpatterns = [
    path('signup/', views.signup_view , name='signup'),
    path('login/', views.login_view , name='login'),
    path('logout/', views.logout_view , name="logout"),
    path('account/<username>/', views.gamers_details , name="account"),
    path('update_account/', views.update_profile , name="update_profile"),
   # path('verify_account/', views.validation_page , name="verify_page")

]

