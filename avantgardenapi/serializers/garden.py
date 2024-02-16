from rest_framework import serializers
from avantgardenapi.models import Garden
from .comment import CommentSerializer
from .garden_plant import GardenPlantSerializer

class GardenSerializer(serializers.ModelSerializer):
  """JSON serializer for a single Garden"""
  plants = GardenPlantSerializer(read_only=True, many=True)
  comments = CommentSerializer(read_only=True, many=True)
  
  class Meta:
    model = Garden
    fields = ('id', 'name', 'image', 'user', 'public', 'plants', 'comments')
    depth = 1
    
class GardenSerializerAll(serializers.ModelSerializer):
  """JSON serializer for all gardens"""
  
  class Meta:
    model = Garden
    fields = ('id', 'name', 'image', 'user', 'public')
    depth = 1
