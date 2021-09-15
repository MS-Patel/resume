from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path("", views.home, name="home"),
    path("create-resume", views.create_resume, name="create-resume"),
    path("resume", views.resume, name="resume"),

]
