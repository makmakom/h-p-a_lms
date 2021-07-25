from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(null=True, default='default.jpg', upload_to='avatars/')
    interests = models.CharField(max_length=255, null=True)
