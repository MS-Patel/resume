from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


def user_directory_path(instance, filename):
    return 'user/avatars/{0}/{1}'.format(instance.username_id, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    avatar = models.ImageField(
        upload_to=user_directory_path, default='user/avatar.jpg')
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username


@ receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwrgs):
    if created:
        Profile.objects.create(user=instance)
