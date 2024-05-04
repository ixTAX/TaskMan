from django.db import models

# Create your models here.
class Task(models.Model):
 title = models.CharField(max_length = 30)
 desc = models.CharField(max_length = 150)
 holder = models.CharField(max_length = 30)
