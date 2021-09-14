from django.urls import path
from . import views

urlpatterns= [
    path("", views.home, name="index"),
    path("questions/", views.questions, name="questions"),
    path("error/<str:err>", views.error, name="error"),
]