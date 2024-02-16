"""View module for handling requests for plants"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from avantgardenapi.models import Plant, PlantType
from avantgardenapi.serializers import PlantSerializer

class PlantView(ViewSet):
  """Avant Garden Plant View"""
  
  def retrieve(self, request, pk):
    """Handle GET reqeust for a single plant
    
    Returns -> Response -- JSON serialized response"""
    
    try:
      plant = Plant.objects.get(pk=pk)
      serializer = PlantSerializer(plant)
      return Response(serializer.data)
    except Plant.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handles GET requests for all plants
    
    Returns -> Response -- JSON serialized list of all plants"""
    
    plants = Plant.objects.all()
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handle Post Request for plants
    
    Returns -> JSON serialized plant staince with a 201 status"""
    
    type = PlantType.objects.get(pk=request.data['type'])
    
    plant = Plant.objects.create(
      name = request.data['name'],
      image = request.data['image'],
      type = type,
      description = request.data['description'],
      grow_time = request.data['growTime'],
      notes = request.data('notes'),
    )
    
    serializer = PlantSerializer(plant)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Handles PUT requests for a plant
    
    Returns -> JSON serialized plant instance"""
    
    type = PlantType.objects.get(pk=request.data['type'])
    plant = Plant.objects.get(pk=pk)
    
    plant.name = request.data['name']
    image = request.data['image'],
    plant.type = type
    plant.description = request.data['description']
    plant.grow_time = request.data['growTime']
    plant.notes = request.data('notes')
    
    plant.save()
    serializer = PlantSerializer(plant)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    """Handles Delete requests for a plant
    
    Returns -> Empty body with 204 status"""
    
    plant = Plant.objects.get(pk=pk)
    plant.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
