from django.db import models

class Garden(models.Model):
  name = models.CharField(max_length=50)
  image = models.CharField(max_length=300)
