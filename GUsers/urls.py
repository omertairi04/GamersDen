from django.urls import path
from GUsers import views
from GUsers.views import UserEditView, UserRegisterView

app_name = 'GUsers'

urlpatterns = [
    path('register/',UserRegisterView.as_view() , name="register"),
    path('edit-profile/',UserEditView.as_view() , name="edit-profile"),
]
