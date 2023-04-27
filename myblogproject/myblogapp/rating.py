from django.db import models
from django.contrib.auth.models import User
from .post import Post

class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    class Meta:
        unique_together = ('post', 'user')
