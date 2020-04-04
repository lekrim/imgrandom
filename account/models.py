from django.db import models
from django.contrib.auth.models import User
from randimg.models import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    album = models.ManyToManyField(Image, related_name='profile')

    def __str__(self):
        return f'{self.user.username} profile'
