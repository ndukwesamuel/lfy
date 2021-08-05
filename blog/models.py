from django.db import models

# Create your models here.


class BlogModel(models.Model):

    name = models.CharField(max_length=100)
    body = models.TextField()
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-id",)


