
from os import name
from django.urls import path
from app import views

urlpatterns = [
    path("", views.login, name="login"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("index", views.index, name="index"),
    path("create-resume", views.create_resume, name="create-resume"),
    path("resume", views.resume, name="resume"),

]