from django.db import models

# Create your models here.
class project(models.Model):
    title = models.CharField(max_length=100)
    detail=models.CharField(max_length=1000)