from rest_framework import serializers
from avantgardenapi.models import PlantType

class PlantTypeSerializer(serializers.ModelSerializer):
  """JSON serializer for plant types"""
  
  class Meta:
    model = PlantType
    fields = ('id', 'label')
