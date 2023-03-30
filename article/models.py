from django.db import models
from django.contrib.auth.models import User

from classifications.models import Classifications
# Create your models here.

# 博客文章数据模型

class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    title=models.CharField(max_length=100)

    body=models.TextField()

    created = models.DateTimeField(auto_now=False)

    updated= models.DateTimeField(auto_now=False)

    deleted = models.BooleanField(default=False)

    hot=models.IntegerField(default=0)

    classifications = models.ForeignKey(Classifications,on_delete=models.CASCADE)

    temp = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title