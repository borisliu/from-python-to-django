from django.db import models

# Create your models here.
class Wiki(models.Model):
    pagename = models.CharField(max_length=20, unique=True)
    content = models.TextField()