from django.db import models

# Create your models here.


class Classifications(models.Model):
    title = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now=True)

    updated = models.DateTimeField(auto_now=True)

    deleted = models.BooleanField(default=False)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
