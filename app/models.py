from django.db import models

# Create your models here.


def user_directory_path(instance, filename):
    return 'user/{0}/{1}'.format(instance.id, filename)


class Resume(models.Model):

    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone = models.IntegerField()
    email = models.EmailField(max_length=150)
    about_you = models.TextField(max_length=400)
    education = models.CharField(max_length=250)
    career = models.CharField(max_length=150)
    job_1_start = models.DateField()
    job_1_end = models.DateTimeField()
    job_1_details = models.CharField(max_length=250)
    job_2_start = models.DateTimeField()
    job_2_end = models.DateTimeField()
    job_2_details = models.CharField(max_length=250)
    job_3_start = models.DateTimeField()
    job_3_end = models.DateTimeField()
    job_3_details = models.CharField(max_length=250)
    references = models.CharField(max_length=250)
    image = models.ImageField(
        upload_to=user_directory_path, default='post/default.png')
