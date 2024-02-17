"""View module for halding requests for gardens plants"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from avantgardenapi.models import Garden, Plant, GardenPlant
from avantgardenapi.serializers import GardenPlantSerializer

class GardenPlantView(ViewSet):
  """Avant Garden: Garden Plant View"""
  
  def retrieve(self, request, pk):
    """Handles GET requests for a single garden plant
    
    Returns -> Response __ JSON serialized response"""
    
    try:
      garden_plant = GardenPlant.objects.get(pk=pk)
      serializer = GardenPlantSerializer(garden_plant)
      return Response(serializer.data)
    except GardenPlant.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handles GET request for all garden plants
    
    Returns -> Response -- JSON serialized list of all garden plants"""
    
    garden_plants = GardenPlant.objects.all()
    serializer = GardenPlantSerializer(garden_plants, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handle POST request for garden plants
    
    Returns -> JSON serialized garden plant instance with 201 status"""
    
    plant = Plant.objects.get(pk=request.data['plant'])
    garden = Garden.objects.get(pk=request.data['garden'])
    
    garden_plant = GardenPlant.objects.create(
      garden = garden,
      plant = plant,
      quantity = request.data['quantity']
    )
    
    serializer = GardenPlantSerializer(garden_plant)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Handles PUT request for a garden plant
    
    Returns -> JSON serialized garden instance"""
    
    plant = Plant.objects.get(pk=request.data['plant'])
    garden = Garden.objects.get(pk=request.data['garden'])
    
    garden_plant = GardenPlant.objects.get(pk=pk)
    garden_plant.garden = garden
    garden_plant.plant = plant
    garden_plant.quantity = request.data['quantity']
    
    garden_plant.save()
    serializer = GardenPlantSerializer(garden_plant)
    return Response(serializer.data)
  
  def destroy(self, request, pk):
    """Handles Delete requests for a garden plant
    
    Returns -> Empty body with a 204 status"""
    
    garden_plant = GardenPlant.objects.get(pk=pk)
    garden_plant.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
