from django.urls import path
from user.views import UserLogin, UserRegistration 

urlpatterns = [
    path('regi/',UserRegistration.as_view()),
    path('',UserLogin.as_view()),
]