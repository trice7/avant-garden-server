from django.db import models
from .garden import Garden
from .plant import Plant

class GardenPlant(models.Model):
  garden = models.ForeignKey(Garden, on_delete=models.CASCADE, related_name='plants')
  plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  planted = models.DateField(auto_now_add=True)
