from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    image = models.ImageField(upload_to='media/',default='default.png')

    def __str__(self):
        return self.user.username

