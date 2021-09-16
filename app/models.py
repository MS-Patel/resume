from django.db import models
from django.conf import settings
from django.db.models.fields.related import ForeignKey

# Create your models here.


def user_directory_path(instance, filename):
    return 'user/{0}/{1}'.format(instance.username_id, filename)


class Resume(models.Model):
    username = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, unique=False)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=150)
    about_you = models.TextField(max_length=400)
    education = models.CharField(max_length=250)
    career = models.CharField(max_length=150)
    job_1_start = models.DateField(null=True)
    job_1_end = models.DateField(null=True)
    job_1_details = models.CharField(max_length=250, null=True)
    job_2_start = models.DateField(null=True)
    job_2_end = models.DateField(null=True)
    job_2_details = models.CharField(max_length=250, null=True)
    job_3_start = models.DateField(null=True)
    job_3_end = models.DateField(null=True)
    job_3_details = models.CharField(max_length=250, null=True)
    references = models.CharField(max_length=250, null=True)
    image = models.ImageField(
        upload_to=user_directory_path, default="user/default.jpg")

    def __str__(self):
        return self.title
