from django.db import models

# Create your models here.
class task(models.Model):
    item = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)