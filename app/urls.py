from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path("", views.login, name="login"),
    path("index", views.index, name="index"),
    path("create-resume", views.create_resume, name="create-resume"),
    path("resume", views.resume, name="resume"),

]
