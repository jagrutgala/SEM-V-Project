from django.urls import path
from . import views

urlpatterns= [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("home/", views.home, name="home"),
    path("questions/", views.questions, name="questions"),
    path("history/", views.history, name="history"),
    path("error/<str:err>", views.error, name="error"),
]