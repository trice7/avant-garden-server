from django.db import models
from .plant_types import PlantType

class Plant(models.Model):
  name = models.CharField(max_length=50)
  image = models.CharField(max_length=300)
  type = models.ForeignKey(PlantType, on_delete=models.CASCADE)
