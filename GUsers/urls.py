from django.urls import path
from GUsers import views
from GUsers.views import CreateProfilePageView, PasswordsChangeView, ShowProfilePageView, UserEditView, UserRegisterView ,EditProfilePageView
from django.contrib.auth import views as auth_views

app_name = 'GUsers'

urlpatterns = [
    path('register/',UserRegisterView.as_view() , name="register"),
    path('edit-profile/',UserEditView.as_view() , name="edit-profile"),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name="registration/change-password.html"), name="change-password")
    path('password/', PasswordsChangeView.as_view(), name="change-password"),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name="show-profile"),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name="edit-profile-page"),
    path('create_profile_page/', CreateProfilePageView.as_view(), name="create-profile-page"),

]
