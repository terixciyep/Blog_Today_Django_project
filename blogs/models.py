from django.db import models
from django.utils import timezone
from users.models import Users


class Category(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории')

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField(max_length=1000)
    comment_author = models.ForeignKey(Users, on_delete=models.CASCADE)
    blod_id = models.ForeignKey(Blog, on_delete=models.CASCADE)