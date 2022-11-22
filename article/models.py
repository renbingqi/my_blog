from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

# 博客文章数据模型

class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    title=models.CharField(max_length=100)

    body=models.TextField()

    created=models.DateTimeField(default=timezone.now)

    updated= models.DateTimeField(auto_now=True)

    delete = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title