from django.db import models
from .garden import Garden
from .user import User

class Comment(models.Model):
  content = models.TextField()
  garden = models.ForeignKey(Garden, on_delete=models.CASCADE, related_name='comments')
  user = models.ForeignKey(User, on_delete=models.CASCADE)
