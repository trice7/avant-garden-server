from rest_framework import serializers
from avantgardenapi.models import Comment

class CommentSerializer(serializers.ModelSerializer):
  """JSON serializer for Comments"""
  
  class Meta:
    model = Comment
    fields = ('id', 'content', 'user', 'date')
    depth = 1
