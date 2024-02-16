from rest_framework import serializers
from avantgardenapi.models import GardenPlant

class GardenPlantSerializer(serializers.ModelSerializer):
  """JSON serializer for a gardens plants"""
  
  class Meta:
    model = GardenPlant
    fields = ('id', 'plant', 'quantity', 'planted')
    depth = 1
