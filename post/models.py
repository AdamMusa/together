from django.db import models


class Post(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()
    creat_at = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.title
# Create your models here.
