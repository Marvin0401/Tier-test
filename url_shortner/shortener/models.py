from django.db import models
import uuid

# Create your models here.
class Url(models.Model):
    link = models.URLField()
    uuid = models.CharField(max_length=5)

    def __str__(self):
        return self.link
