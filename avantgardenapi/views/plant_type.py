"""View module for handling requests for plant types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from avantgardenapi.models import PlantType
from avantgardenapi.serializers import PlantTypeSerializer

class PlantTypeView(ViewSet):
  """Avant Garden Plant Type view"""
  
  def retrieve(self, request, pk):
    """Handles GET reqeusts for a single plant type

   Returns -> Response -- JSON serialized response
    """
    
    try:
      plant_type = PlantType.objects.get(pk=pk)
      serializer = PlantTypeSerializer(plant_type)
      return Response(serializer.data)
    except PlantType.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handles GET requests for all plant types
    Returns -> Response -- JSON serialized list of plant types"""
    
    plant_types = PlantType.objects.all()
    serializer = PlantTypeSerializer(plant_types, many=True)
    return Response(serializer.data)
