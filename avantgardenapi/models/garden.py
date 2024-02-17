from django.db import models
from .user import User

class Garden(models.Model):
  name = models.CharField(max_length=50)
  image = models.CharField(max_length=300)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  public = models.BooleanField()
