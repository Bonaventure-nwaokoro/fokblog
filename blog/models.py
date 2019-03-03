from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field",upload_to='imgdb')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

# class Comment(models.Model):
#     name = models.CharField(max_length=100)
#     body = models.TextField()
#     pub_date = models.DateTimeField(default=timezone.now)
#     article = models.ForeignKey(Post)
    


