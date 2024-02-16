"""View module for halding requests for gardens"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from avantgardenapi.models import Garden, User
from avantgardenapi.serializers import GardenSerializer, GardenSerializerAll

class GardenView(ViewSet):
  """Avant Garden Garden View"""
  
  def retrieve(self, request, pk):
    """Handle GET requests for a single garden
    
    Returns -> Response -- JSON serialized response"""
    
    try:
      garden = Garden.objects.get(pk=pk)
      serializer = GardenSerializer(garden)
      return Response(serializer.data)
    except Garden.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handles GET requests for all gardens
    
    Returns -> Response -- JSON serialized list of all gardens"""
    
    gardens = Garden.objects.all()
    serializer = GardenSerializerAll(gardens, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handle POST requests for gardens
    
    Returns -> JSON serialized garden instance with a 201 status"""
    
    user = User.objects.get(uid=request.data["uid"])
    
    garden = Garden.objects.create(
      name = request.data['name'],
      image = request.data['image'],
      user = user,
      public = request.data['public'],
    )
    
    serializer = GardenSerializer(garden)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Handles PUT requests for a garden
    
    Returns -> JSON serialized garden instance"""
    
    user = User.objects.get(uid=request.data['uid'])
    
    garden = Garden.objects.get(pk=pk)
    
    garden.name = request.data['name']
    garden.image = request.data['image']
    garden.user = user
    garden.public = request.data['public']
    
    garden.save()
    serializer = GardenSerializer(garden)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    """Handles Delete requests for a garden
    
    Returns -> Empty body with 204 status"""
    
    garden = Garden.objects.get(pk=pk)
    garden.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
