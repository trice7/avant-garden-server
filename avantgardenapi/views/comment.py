"""View Module for handline requests for comments"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from avantgardenapi.models import Comment, User, Garden
from avantgardenapi.serializers import CommentSerializer

class CommentView(ViewSet):
  """Avant Garden Comment View"""
  
  def retrieve(self, request, pk):
    """Handle GET requests for a single comment
    
    Returns -> Response -- JSON serialized response"""
    
    try:
      comment = Comment.objects.get(pk=pk)
      serializer = CommentSerializer(comment)
      return Response(serializer.data)
    except Garden.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handles GET requests for all comments
    
    Returns -> Response -- JSON serialized list of all comments"""
    
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handle POST requests for comments
    
    Returns -> Response -- JSON serialized comment with 201 status"""
    
    user = User.objects.get(uid=request.data["uid"])
    garden = Garden.objects.get(pk=request.data["garden"])
    
    comment = Comment.objects.create(
      content = request.data["content"],
      garden = garden,
      user = user,
    )
    
    serializer = CommentSerializer(comment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Handles PUT requests for a comment
    
    Returns -> JSON serialized comment instance"""
    
    user = User.objects.get(uid=request.data["uid"])
    garden = Garden.objects.get(pk=request.data["garden"])
    comment = Comment.objects.get(pk=pk)
    
    comment.content = request.data['content']
    comment.user = user
    comment.garden = garden
    
    comment.save()
    serializer = CommentSerializer(comment)
    return Response(serializer.data)
  
  def destroy(self, request, pk):
    """Handles Delete requests for a comment
    
    Returns -> Empty body with 204 status"""
    
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
    