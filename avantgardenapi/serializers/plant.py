from rest_framework import serializers
from avantgardenapi.models import Plant

class PlantSerializer(serializers.ModelSerializer):
  """JSON serializer for plants"""
  
  class Meta:
    model = Plant
    fields = ('id', 'name', 'image', 'type', 'description', 'grow_time', 'notes')
    depth = 1
